
import grpc
import json

from sync_example_bib_app.grpc import sync_example_bib_app_pb2_grpc, sync_example_bib_app_pb2

def main():
    with grpc.insecure_channel("localhost:9082") as channel:
        author_client = sync_example_bib_app_pb2_grpc.AuthorControllerStub(channel)

        filter_as_dict = {"name_last": "Doe"}
        metadata = (("filters", (json.dumps(filter_as_dict))),)

        response = author_client.List(sync_example_bib_app_pb2.AuthorListRequest(), metadata=metadata)

        print("Response received :")
        print(response)
            
if __name__ == "__main__":
    main()
