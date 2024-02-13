import asyncio
import grpc
from datetime import datetime
from example_bib_app.grpc import example_bib_app_pb2_grpc, example_bib_app_pb2

def read_in_chunks(file, chunk_size=1024, filename="", book_id=""):
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield example_bib_app_pb2.FileChunk(filename=filename, book_id=book_id, data=data)


# Performs a client-streaming call
async def update_image(stub, image_file_path, filename="", book_id=""):
    chunk_size = 4 * 1024  # Set chunk size as needed

    with open(image_file_path, 'rb') as file:
        chunk_iterator = read_in_chunks(file, chunk_size, filename=filename, book_id=book_id)
        try:
            response = await stub.UpdateImage(chunk_iterator)
            print(f"Update status: {response.success}")
        except grpc.aio.AioRpcError as error:
            print(f"Update failed with error: {error}")
   
    return "success"



async def main():
     image_filename = "./les_miserables.jpg"

     async with grpc.aio.insecure_channel("localhost:50051") as channel:
        print("book image client started")
        publisher_client = example_bib_app_pb2_grpc.PublisherControllerStub(channel)
        stub = example_bib_app_pb2_grpc.BookControllerStub(channel)

        publisher_response = await publisher_client.Create(
            example_bib_app_pb2.PublisherRequest(
                name="Penguin Classics",
                address="London",
                city="London",
                state_province="London",
                country="UK",
                website="https://www.penguin.co.uk/",
            )
        )

        res = await publisher_client.List(example_bib_app_pb2.PublisherListRequest())
        publisher_list = res.results

        print(f"publishers: {publisher_list}")


        book_dict = {
            "title": "Les Miserables",
            #"authors": ["Victor Hugo"],
            #"categories": ["Fiction"],
            "isbn": "978-0140444308",
            #"publisher": "Penguin Classics",
            "publisher": publisher_list[0].publisher_id,
            "publication_date": datetime(1862, 1, 1).strftime('%Y-%m-%d') ,
        }
        # Create a book
        book = example_bib_app_pb2.BookRequest(**book_dict)
        response = await stub.Create(book)
        print(f"book created: {response.book_id}")

        book_id = response.book_id

        filename = book.title.lower() + ".jpg"

        # Upload the image

        response = await update_image(stub, image_filename, filename=filename, book_id=book_id)
        
        print(f"book image client received:{ response}" ) # response.message

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
