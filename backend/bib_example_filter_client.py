
import grpc
import json

from async_example_bib_app.grpc import async_example_bib_app_pb2_grpc, async_example_bib_app_pb2

def main():
    with grpc.insecure_channel("localhost:50051") as channel:
        author_client = async_example_bib_app_pb2_grpc.AuthorControllerStub(channel)

        #filter_as_dict = {"name_last": "Doe"}
        #metadata = (("filters", (json.dumps(filter_as_dict))),)

        filter_as_dict = '{"name_last": "Doe"}'
        metadata = (("filters", (filter_as_dict)),) 

        response = author_client.List(async_example_bib_app_pb2.AuthorListRequest(), metadata=metadata)

        print("Response received :")
        print(response)
            
if __name__ == "__main__":
    main()
