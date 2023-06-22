import asyncio
import datetime
import grpc
from app_example.grpc import app_example_pb2_grpc, app_example_pb2


async def main():
    async with grpc.aio.insecure_channel("localhost:50051") as channel:
        stub = app_example_pb2_grpc.QuestionControllerStub(channel)

        request = app_example_pb2.QuestionRequest(
            question_text=input("Give question\n"),
            date_published=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        )
        response = await stub.Create(request)

        print(f"Created message <{response.id}>")


if __name__ == "__main__":
    asyncio.run(main())
