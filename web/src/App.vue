<template>
  <div class="app">
    <DiagramStyling />
    <h1>{{ title }}</h1>
    Enter the number of divisions that you want to divide your paper into:
    <DivisionInput />
    <RefList />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import DivisionInput from './components/DivisionInput.vue';
import RefList from './components/RefList.vue';
import DiagramStyling from './components/DiagramStyling.vue';

@Options({
  components: {
    // HelloWorld,
    DivisionInput,
    RefList,
    DiagramStyling,
  },
})
export default class App extends Vue {
  public title = "DivisionFinder by FreakyFee, based on Robert Lang's ReferenceFinder";
}
</script>

<style>
#app {
  font-family: "Comic Sans MS", "Comic Sans", cursive;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  margin-top: 60px;
  
}
body {background: #100;}
</style>
