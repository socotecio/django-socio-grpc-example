
# This is an example of how to use the filter functionality of the backend.

import asyncio
import grpc
import json

from example_bib_app.grpc import example_bib_app_pb2_grpc, example_bib_app_pb2

async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        author_client = example_bib_app_pb2_grpc.AuthorControllerStub(channel)
        publisher_client = example_bib_app_pb2_grpc.PublisherControllerStub(channel)
        book_client = example_bib_app_pb2_grpc.BookControllerStub(channel)

        # we recommend to start with an dictionary and convert it into a string, whenever this 
        filter_as_dict = {"name_last": "Doe"}
        metadata = (("filters", (json.dumps(filter_as_dict))),)
        response = await author_client.List(example_bib_app_pb2.AuthorListRequest(), metadata=metadata)

        print("Filter as dict:--------------------\n", filter_as_dict)
        print("Response (from JSON string) received :\n", response)

        # although one could use a filter string (in JSON format) to send a filter like:
        filter_as_str = '{"name_last": "Doe"}'
        metadata = (("filters", (filter_as_str)),) 
        response = await author_client.List(example_bib_app_pb2.AuthorListRequest(), metadata=metadata)

        print("Filter as string:----------------\n", filter_as_str)
        print("Response (from string) received :\n", response)

        # publisher filter
        print("Publisher filter:----------------\n")
        filter_as_dict = {"name": "Doe"}
        metadata = (("filters", (json.dumps(filter_as_dict))),)
        response = await publisher_client.List(example_bib_app_pb2.PublisherListRequest(), metadata=metadata)

        print("Response (from JSON string) received :\n", response)

        # book search
        print("Book search:----------------\n")
        search_as_dict = {"title": "book 1"}
        metadata = (("search", (json.dumps(search_as_dict))),)
        response = await book_client.List(example_bib_app_pb2.BookListRequest(), metadata=metadata)

        print("Response (from JSON string) received :\n", response)


    
            
if __name__ == "__main__":
    asyncio.run(main())
