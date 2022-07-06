<template>
  <DiagramContainer :instruction="instructions" />
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import DiagramContainer from "./DiagramContainer.vue";

@Options({
  props: ['instructions'],
  components: {
      DiagramContainer,
  }
})
export default class CycleInstructions extends Vue {}
</script>