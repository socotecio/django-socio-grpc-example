import asyncio
import grpc
from sync_example_bib_app.grpc import sync_example_bib_app_pb2_grpc, sync_example_bib_app_pb2


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = sync_example_bib_app_pb2_grpc.QuestionControllerStub(channel)

        queue = asyncio.Queue()

        async def generate_requests():
            while True:
                yield await queue.get()

        await queue.put(input("Give question\n"))

        async for response in stub.Stream(generate_requests()):
            print("Response received :", flush=True)
            print(response.response, flush=True)
            request = sync_example_bib_app_pb2.QuestionStreamRequest(
                question_text=input("Give question\n")
            )
            await queue.put(request)


if __name__ == "__main__":
    asyncio.run(main())
