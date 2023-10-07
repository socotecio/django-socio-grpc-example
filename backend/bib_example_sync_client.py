
import grpc
from async_example_bib_app.grpc import async_example_bib_app_pb2_grpc, async_example_bib_app_pb2

def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = async_example_bib_app_pb2_grpc.AuthorControllerStub(channel)
        
        response = stub.List(async_example_bib_app_pb2.AuthorListRequest())
        print("Response received :")
        print(response)
            
if __name__ == "__main__":
    main()
