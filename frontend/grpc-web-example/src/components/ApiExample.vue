<script setup>
import { ref } from 'vue'
// import proto from '../api/example_bib_app_pb'
const proto = require('../api/example_bib_app_pb');

console.log(proto)

let items = ref([])

defineProps({
  msg: {
    type: String,
    required: true
  }
})

</script>

<template>
  <div class="greetings">
    <h1 class="green">gRPC Web Example</h1>
    <button>Create element with grpc-web</button>
    <h3>Elements existings: </h3>
    <ul>
      <li v-for="item in items">{{ item.name }}</li>
    </ul>
  </div>
</template>


