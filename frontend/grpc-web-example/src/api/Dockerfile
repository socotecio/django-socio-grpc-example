FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /tmp

ENV PROTOC_VERSION 21.11
ENV GRPC_WEB_VERSION 1.5.0
ENV JS_PROTO_V 3.21.2
ENV BASE_URL https://github.com/protocolbuffers

RUN wget ${BASE_URL}/protobuf/releases/download/v${PROTOC_VERSION}/protoc-${PROTOC_VERSION}-linux-x86_64.zip
RUN unzip protoc-${PROTOC_VERSION}-linux-x86_64.zip -d /usr/local && chmod +x /usr/local/bin/protoc
RUN wget ${BASE_URL}/protobuf-javascript/releases/download/v${JS_PROTO_V}/protobuf-javascript-${JS_PROTO_V}-linux-x86_64.zip
RUN unzip protobuf-javascript-${JS_PROTO_V}-linux-x86_64.zip -d ./protobuf-javascript
RUN mv ./protobuf-javascript/bin/protoc-gen-js /usr/local/bin/
RUN chmod +x /usr/local/bin/protoc-gen-js

RUN wget https://github.com/grpc/grpc-web/releases/download/${GRPC_WEB_VERSION}/protoc-gen-grpc-web-${GRPC_WEB_VERSION}-linux-x86_64
RUN mv protoc-gen-grpc-web-${GRPC_WEB_VERSION}-linux-x86_64 /usr/local/bin/protoc-gen-grpc-web && chmod +x /usr/local/bin/protoc-gen-grpc-web

WORKDIR /grpc-api

COPY ./ .
VOLUME /grpc-api


ENV DIR ./
ENV OUT_DIR ./

CMD protoc -I=$DIR example_bib_app.proto \
    --js_out=import_style=commonjs:$OUT_DIR \
    --grpc-web_out=import_style=commonjs,mode=grpcwebtext:$OUT_DIR