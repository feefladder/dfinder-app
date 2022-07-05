<template>
  <div class="diagram-container">
  <Diagram 
    v-for="(diagram, i) in instructions.diagrams"
    :key="i"
    :diagram="diagram" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import Diagram from "./Diagram.vue";

@Options({
  props: ['instructions'],
  components: {
      Diagram,
  }
})
export default class CycleInstructions extends Vue {}
</script>