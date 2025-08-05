# Building a gRPC API with buf

To build the gRPC API, we use `buf` to manage our protocol buffers and generate the necessary code for different languages. The following steps outline the process:

This will install the necessary javascript dependencies

```bash
cd frontend/grpc-web-example
npm install
```

To build the gRPC API, you need to run the following command in the `frontend/grpc-web-example` directory:

```bash
npx buf generate proto
``` 

This will generate a `example_bib_app_pb.js` file in the `frontend/grpc-web-example/src/gen` directory, which contains the gRPC API definitions.