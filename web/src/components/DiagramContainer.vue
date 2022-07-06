<template>
  <div class="diagram-container">
    <div class="diagram-list">
      <Diagram 
        v-for="(diagram, i) in instruction.diagrams"
        :key="i"
        :diagram="diagram"
        :verbal="instruction.verbal[i]"/>
    </div>
    <div class="verbal-instr">
      <button @click="toggleAllVerbalInstructions">Verbal instructions</button>
      <div class="all-verbal-instructions" v-if="showVerbalInstructions">
        <div v-for="(verbal, i) in instruction.verbal" :key="i">{{verbal}}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component'
import Diagram from './Diagram.vue';

@Options({
  props: ['instruction', 'showVerbalInstructions'],
  components: {
    Diagram,
  },
  methods: {
    toggleAllVerbalInstructions() : void {
        this.showVerbalInstructions = !this.showVerbalInstructions;
    }
  }
})
export default class Ref extends Vue {
    public showVerbalInstructions = false;
}
</script>

<style scoped>
.diagram-list{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>