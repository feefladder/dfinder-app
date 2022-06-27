<template>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <DiagramsContainer />
  <input type="number" v-model="divisions" placeholder="23" value="23">
  <!-- <button class="md-fab">GO!</button> -->
  <div class="container" v-html="diagrams.response">
  </div>
  <svg height='180px' width='1800px'> <g class='diagram' transform=' translate(25,25)' > <title>Fold the right edge to the left edge, making line A</title> <path d='M0 150 L 0 0 L 150 0 L 150 150 L 0 150' fill='#fd9' stroke='black' stroke-width='2'/> <line x1='-0' y1='0' x2='150' y2='0' stroke='darkgray' stroke-width='.5'/> <line x1='0' y1='0' x2='0' y2='150' stroke='darkmagenta' stroke-width='2'/> <line x1='150' y1='150' x2='150' y2='0' stroke='darkmagenta' stroke-width='2'/> <line x1='75' y1='150' x2='75' y2='0' stroke='green' stroke-width='.5' stroke-dasharray='2'/> <path d='M 150 75Q 75 30 0 75' fill='none' stroke='green' stroke-width='1' marker-start='url(#unfold_arrow)' marker-end='url(#arrow)'/> <text x='75' y='75'>A</text> </g> <g class='diagram' transform='translate(205,25)' > <title>Bring the bottom right corner to line A, making line B</title> <path d='M0 150 L 0 0 L 150 0 L 150 150 L 0 150' fill='#fd9' stroke='black' stroke-width='2'/> <line x1='-0' y1='0' x2='150' y2='0' stroke='darkgray' stroke-width='.5'/> <line x1='0' y1='0' x2='0' y2='150' stroke='darkgray' stroke-width='.5'/> <line x1='150' y1='150' x2='150' y2='0' stroke='darkgray' stroke-width='.5'/> <line x1='75' y1='150' x2='75' y2='0' stroke='darkmagenta' stroke-width='2'/> <line x1='-0' y1='0' x2='150' y2='86.6025' stroke='green' stroke-width='.5' stroke-dasharray='2'/> <circle r='1' cx='0' cy='0' stroke='rgb(128,64,64)' stroke-width='3'/> <circle r='1' cx='150' cy='0' stroke='rgb(128,64,64)' stroke-width='3'/> <path d='M 150 0Q 73.5289 42.4519 75 129.904' fill='none' stroke='green' stroke-width='1' marker-start='url(#unfold_arrow)' marker-end='url(#arrow)'/> <text x='75' y='75'>A</text> <text x='75' y='43.3013'>B</text> </g></svg> 
</template>

<script>
import ProjectRepository from '@/repositories/ProjectRepository'
import HelloWorld from './components/HelloWorld.vue'
import DiagramsContainer from './components/DiagramsContainer.vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    DiagramsContainer,
  },
  data() {
    return {
      divisions: 0,
      diagrams: "stuff",
    }
  },
  methods: {
    async getDivisionDiagrams() {
      this.diagrams = await ProjectRepository.getDiagrams(this.divisions)
    }
  },
  watch: {
    divisions() {
      this.getDivisionDiagrams()
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
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
.l_mountain {
  stroke: green;
  stroke-width: .5;
  stroke-dasharray: 3 2 2 2;
}
.l_arrow {
  stroke: darkgreen;
  stroke-width: .5;
}
</style>
