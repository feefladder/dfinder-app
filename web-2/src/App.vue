<template>
  <div class="app">
    <h1>{{ title }}</h1>
    <DivisionInput />
    <RefList />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
// import HelloWorld from './components/HelloWorld.vue';
import DivisionInput from './components/DivisionInput.vue';
import RefList from './components/RefList.vue';

@Options({
  components: {
    // HelloWorld,
    DivisionInput,
    RefList,
  },
})
export default class App extends Vue {
  public title = "DivisionFinder by FreakyFee, based on Robert Lang's ReferenceFinder";
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
</style>
