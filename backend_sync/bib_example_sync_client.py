
import grpc

from sync_example_bib_app.grpc import sync_example_bib_app_pb2_grpc, sync_example_bib_app_pb2

def main():
    with grpc.insecure_channel("localhost:9082") as channel:
        stub = sync_example_bib_app_pb2_grpc.AuthorControllerStub(channel)
        
        response = stub.List(sync_example_bib_app_pb2.AuthorListRequest())
        print("Response received :")
        print(response)
            
if __name__ == "__main__":
    main()