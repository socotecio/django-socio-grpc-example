import asyncio
import grpc
from datetime import datetime
from example_bib_app.grpc import example_bib_app_pb2_grpc, example_bib_app_pb2

async def upload_file(stub, file_path):
    with open(file_path, 'rb') as file:
        tasks = []
        for chunk in read_in_chunks(file):
            print(f"Uploading chunk of size {len(chunk)}")
            # Create a FileChunk message and send it to the server
            #task = 
            task = stub.UploadFile(example_bib_app_pb2.FileChunk(data=chunk))
            #loop.create_task(response)
            
            #print(f"Upload status: {response.success}")
            #print(f"Upload status: {response}")
            tasks.append(task)
        res = await asyncio.gather(*tasks, return_exceptions=True)
    print(res)

def read_in_chunks(file, chunk_size=1024):
    while True:
        data = file.read(chunk_size)
        if not data:
            break
        yield data #example_bib_app_pb2.FileChunk(data=data)

async def main():
   channel = grpc.aio.insecure_channel('localhost:50051')
   stub = example_bib_app_pb2_grpc.FileUploadControllerStub(channel)
   await upload_file(stub, '/tmp/pics/les_miserable.jpg')


if __name__ == '__main__':
    asyncio.run(main())
