<template>
  <div class="diagram-howto" @click="toggleVerbal">
    <div class="diagram">
        <svg width="150" height="150" viewBox="-10 -10 170 170" v-html="diagram"></svg>
    </div>
    <div class="howto" v-if="showVerbal">
      {{verbal}}
    </div>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component'

@Options({
  props: ['diagram', 'verbal'],
  methods: {
    toggleVerbal() {
      this.showVerbal = !this.showVerbal;
    }
  }
})
export default class Diagram extends Vue {
  public showVerbal = false;
}
</script>

<style scoped>
.howto {
  margin: 15px;
}
</style>