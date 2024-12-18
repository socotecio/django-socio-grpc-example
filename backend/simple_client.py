
from example_bib_app.grpc import example_bib_app_pb2_grpc, example_bib_app_pb2
import asyncio
import grpc


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        # create Author gRPC client
        author_client = example_bib_app_pb2_grpc.AuthorControllerStub(channel)

        res = await author_client.List(example_bib_app_pb2.AuthorListRequest())
        for author in res.results:
            print(author.name_first, author.name_last)

if __name__ == "__main__":
    asyncio.run(main())