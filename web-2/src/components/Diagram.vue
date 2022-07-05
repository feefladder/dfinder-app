<template>
  <div class="diagram">
      <svg width="150" height="150" viewBox="-20 -20 170 170" v-html="diagram"></svg>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'

@Options({
    props: ['diagram']
})
export default class Diagram extends Vue {}
</script>

<style>

.diagram {
  margin: 10px;
}

.pt_normal {
  stroke: black;
  stroke-width: 1;
}
.pt_hilite {
  stroke: rgb(128,64,64);
  stroke-width: 3;
}
.pt_action {
  stroke: rgb(128,0,0);
  stroke-width: 3;
}

.l_crease {
  stroke: darkgray;
  stroke-width: .5;
}
.l_edge {
  stroke: black;
  stroke-width: 2;
}
.l_hilite {
  stroke: darkmagenta;
  stroke-width: 2;
}
.l_valley {
  stroke: green;
  stroke-width: .5;
stroke-dasharray: 2;
}
</style>