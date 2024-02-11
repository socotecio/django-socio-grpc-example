import asyncio
import grpc
from datetime import datetime
from example_bib_app.grpc import example_bib_app_pb2_grpc, example_bib_app_pb2

def read_in_chunks(file, chunk_size=1024):
        while True:
            data = file.read(chunk_size)
            if not data:
                break
            yield example_bib_app_pb2.FileChunk(data=data)


# Performs a client-streaming call
async def upload_file(stub, file_path):
    chunk_size = 4 * 1024  # Set chunk size as needed

    with open(file_path, 'rb') as file:
        chunk_iterator = read_in_chunks(file, chunk_size)
        try:
            response = await stub.UploadFile(chunk_iterator)
            print(f"Upload status: {response.success}")
        except grpc.aio.AioRpcError as error:
            print(f"Upload failed with error: {error}")
   
    return "success"



async def main():
     image_filename = "/tmp/pics/les_miserables.jpg"

     async with grpc.aio.insecure_channel("localhost:50051") as channel:
        print("book image client started")
        stub = example_bib_app_pb2_grpc.FileUploadControllerStub(channel)
        response = await upload_file(stub, image_filename)
        
        print(f"book image client received:{ response}" ) # response.message

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
