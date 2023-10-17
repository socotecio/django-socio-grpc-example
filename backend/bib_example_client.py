# CRUD operations on Author entity


import asyncio
import grpc
from example_bib_app.grpc import example_bib_app_pb2_grpc, example_bib_app_pb2


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = example_bib_app_pb2_grpc.AuthorControllerStub(channel)
        
        queue = asyncio.Queue()

        async def generate_requests():
            while True:
                yield await queue.get()

        await queue.put(input("List Authors ? (type enter to continue ....) \n"))

        async for response in stub.List(generate_requests()):
            print("Response received :", flush=True)
            print(response.response, flush=True)
            request = example_bib_app_pb2.AuthorListRequest()
            await queue.put(request)

        # async for response in stub.Stream(generate_requests()):
        #     print("Response received :", flush=True)
        #     print(response.response, flush=True)
        #     request = example_bib_app_pb2.AuthorStreamRequest(
        #         author_id=input("Give author id\n")
        #     )
        #     await queue.put(request)


if __name__ == "__main__":
    asyncio.run(main())
