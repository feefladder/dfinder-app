<template>
  <div class="ref">
    <div class="instruction-description">
      <h2>{{instruction.description}}</h2>
    </div>
    <DiagramContainer :instruction="instruction" />
    <button @click="FoldCycle">Fold from this ref</button>
    <div class="cycle-container">
      <CycleInstructions v-if="instruction.cycle" :instructions="instruction.cycle"/>
    </div>
  </div>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component'
import CycleInstructions from './CycleInstructions.vue';
import DiagramContainer from './DiagramContainer.vue';

@Options({
  props: ['instruction'],
  components: {
    DiagramContainer,
    CycleInstructions,
  },
  methods: {
    FoldCycle(): void {
      this.$store.dispatch('foldCycle', this.instruction.division);
      this.flag = true;
    }
  }
})
export default class Ref extends Vue {
    public flag = false;
}
</script>

<style scoped>
.diagram-container{
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>