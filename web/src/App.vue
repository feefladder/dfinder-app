<template>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <DiagramsContainer />
  <input type="number" min="3" step="2" max="99" value="23" v-model="divisions">
  <div class="container" v-html="diagrams.response">
  </div>
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
  text-align: left;
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
