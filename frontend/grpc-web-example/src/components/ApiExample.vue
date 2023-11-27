<script setup>
import { ref } from 'vue'
import {AuthorRequest, AuthorListRequest} from '../gen/example_bib_app_pb'
import { AuthorController } from '../gen/example_bib_app_connect'

import { createPromiseClient } from "@connectrpc/connect";
import { createGrpcWebTransport } from "@connectrpc/connect-web";

// The transport defines what type of endpoint we're hitting.
// In our example we'll be communicating with a Connect endpoint.
// If your endpoint only supports gRPC-web, make sure to use
// `createGrpcWebTransport` instead.
const transport = createGrpcWebTransport({
  baseUrl: "http://localhost:9001",
});

// Here we make the client itself, combining the service
// definition with the transport.
const authorClient = createPromiseClient(AuthorController, transport);

console.log(authorClient)

let items = ref([])

async function createAuthor() {
  const res = await authorClient.create({
    nameFirst: "TestFirst",
    nameLast: "TestLast",
    birthDate: "2000-01-01"    
  })
  console.log(res)
}

</script>

<template>
  <div class="greetings">
    <h1 class="green">gRPC Web Example</h1>
    <button @click="createAuthor">Create element with grpc-web</button>
    <h3>Elements existings: </h3>
    <ul>
      <li v-for="item in items">{{ item.name }}</li>
    </ul>
  </div>
</template>


