<script setup>
import { ref, onMounted } from 'vue'
import { AuthorController } from '../gen/example_bib_app_pb.js'

import { createClient } from "@connectrpc/connect";
import { createGrpcWebTransport } from "@connectrpc/connect-web";

// The transport defines what type of endpoint we're hitting.
// In our example we'll be communicating with a gRPC-web endpoint.
// See https://connectrpc.com/docs/web/choosing-a-protocol
const transport = createGrpcWebTransport({
  baseUrl: "http://localhost:9001",
});

// Here we make the client itself, combining the service
// definition with the transport.
// See https://connectrpc.com/docs/web/using-clients
const authorClient = createClient(AuthorController, transport);

let items = ref([])

const fetchAuthors = async () => {
  const res = await authorClient.list({})
  console.log(res)
  items.value = res.results
}

onMounted(async() => {
  await fetchAuthors()
})

async function createAuthor() {
  const res = await authorClient.create({
    nameFirst: "TestFirst",
    nameLast: "TestLast",
    birthDate: "2000-01-01"    
  })
  console.log(res)
  await fetchAuthors()
}

/**
 * If you need to match an exact schema:
 * import { create } from "@bufbuild/protobuf";
 * import { AuthorRequestSchema } from '../gen/proto/example_bib_app_pb.js'
 * const request = create(AuthorRequestSchema, {
 *   nameFirst: "TestFirst",
 *   nameLast: "TestLast",
 *   birthDate: "2000-01-01",
 * });
 * const res = await authorClient.create(request)
 */

</script>

<template>
  <div class="greetings">
    <h1 class="green">gRPC Web Example</h1>
    <button @click="createAuthor">Create element with grpc-web</button>
    <h3>Existings Authors: </h3>
    <ul>
      <li v-for="item in items">{{ item.nameFirst }} {{ item.nameLast }} {{ item.birthDate }}</li>
    </ul>
  </div>
</template>


