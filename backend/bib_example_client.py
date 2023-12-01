# CRUD operations on Author entity


import asyncio
import grpc
from datetime import datetime
from example_bib_app.grpc import example_bib_app_pb2_grpc, example_bib_app_pb2


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        # create Author gRPC client
        author_client = example_bib_app_pb2_grpc.AuthorControllerStub(channel)
        publisher_client = example_bib_app_pb2_grpc.PublisherControllerStub(channel)
        publ_cat_client = example_bib_app_pb2_grpc.PublicationCategoryControllerStub(channel)

        book_client = example_bib_app_pb2_grpc.BookControllerStub(channel)

        # Create
        for i in range(10):
            author_response = await author_client.Create(
                example_bib_app_pb2.AuthorRequest(
                    name_first="John",
                    name_last=f"Doe{i}",
                    birth_date=datetime.now().strftime("%Y-%m-%d"),
                )
            )
            print("author create response:", author_response)  # flush=True

        last_author_id = author_response.author_id

        # Read
        res = await author_client.List(example_bib_app_pb2.AuthorListRequest())
        res.results
        for author in res.results:
            print(author.name_first, author.name_last)

        # Update
        author_response = await author_client.Update(
            example_bib_app_pb2.AuthorRequest(
                author_id=last_author_id,
                name_first="Jane",
                name_last="Doll",
                birth_date=datetime.now().strftime("%Y-%m-%d"),
            )
        )
        print("author update response:", author_response)  # flush=True


        # Create three Publisher

        publisher_response = await publisher_client.Create(
            example_bib_app_pb2.PublisherRequest(
                name="O'Reilly",
                address="",
                city="",
                state_province="",
                country="",
                website="https://www.oreilly.com/",
            )
        )
        print("publisher create response:", publisher_response)

        publisher_response = await publisher_client.Create(
            example_bib_app_pb2.PublisherRequest(
                name="Springer",
                address="",
                city="",
                state_province="",
                country="",
                website="https://www.springer.com/",
            )
        )

        print("publisher create response:", publisher_response)

        publisher_response = await publisher_client.Create(
            example_bib_app_pb2.PublisherRequest(
                name="MIT Press",
                address="",
                city="",
                state_province="",
                country="",
                website="https://mitpress.mit.edu/",
            )
        )

        print("publisher create response:", publisher_response)

        # Create three PublicationCategories

        publication_category_response = await publ_cat_client.Create(
            example_bib_app_pb2.PublicationCategoryRequest(
                name="Book",
            )
        )
        print("publication category create response:", publication_category_response)
        
        publication_category_response = await publ_cat_client.Create(
            example_bib_app_pb2.PublicationCategoryRequest(
                name="Journal",
            )
        )

        print("publication category create response:", publication_category_response)

        publication_category_response = await publ_cat_client.Create(
            example_bib_app_pb2.PublicationCategoryRequest(
                name="Magazine",
            )
        )

        print("publication category create response:", publication_category_response)

        # list all categories

        res = await publisher_client.List(example_bib_app_pb2.PublicationCategoryListRequest())
        res.results
        for category in res.results:
            print(category.name)
        

        # Create ten Books

        for i in range(10):
            await book_client.Create(example_bib_app_pb2.BookRequest(title=f'book {i}', 
                                                                    authors=[author_response.author_id],
                                                                    isbn=f'isbn-{i}',
                                                                    publisher=publisher_response.publisher_id,
                                                                    publication_date=datetime.now().strftime('%Y-%m-%d')
                                                                    ))

        # Stream Read

        print("------ Async Stream Read ------")

        async for book in  book_client.Stream(example_bib_app_pb2.BookStreamRequest()):
            print(book)     


        # Delete
        # author_response = await author_client.Delete(example_bib_app_pb2.AuthorRequest(author_id=1))
        # print("author delete response:", author_response.response) #flush=True

        # queue = asyncio.Queue()

        # async def generate_requests():
        #     while True:
        #         yield await queue.get()

        # await queue.put(input("List Authors ? (type enter to continue ....) \n"))


if __name__ == "__main__":
    asyncio.run(main())
