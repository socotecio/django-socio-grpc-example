import asyncio
import grpc
from app_example.grpc import app_example_pb2_grpc, app_example_pb2


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = app_example_pb2_grpc.QuestionControllerStub(channel)

        queue = asyncio.Queue()

        async def generate_requests():
            while True:
                yield await queue.get()

        await queue.put(input("Give question\n"))

        async for response in stub.Stream(generate_requests()):
            print("Response received :", flush=True)
            print(response.response, flush=True)
            request = app_example_pb2.QuestionStreamRequest(
                question_text=input("Give question\n")
            )
            await queue.put(request)


if __name__ == "__main__":
    asyncio.run(main())
