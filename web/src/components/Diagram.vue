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
