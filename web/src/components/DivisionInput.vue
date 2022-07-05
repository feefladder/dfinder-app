<template>
  <form @submit.prevent="calcDivisions" method="get">
      <input type="number" min="1" name="divisions" v-model="nDivisions"/>
      <input type="submit" value="Find References">
  </form>
</template>

<script lang="ts">
import {Vue} from 'vue-class-component';
import store from '../store';

export default class DivisionInput extends Vue {
    public nDivisions = 5;

    public calcDivisions(): void {
        while (this.nDivisions % 2 == 0){this.nDivisions = this.nDivisions/2}
        store.dispatch("calcDivisions", this.nDivisions);
    }
}
</script>