<template>
  <div class="refs">
    <Ref
        v-for="(instruction, i) in $store.state.Instructions  "
        :key="i"
        :instruction="instruction" />
  </div>
</template>

<script lang="ts">
import {Options, Vue} from 'vue-class-component'
import Ref from './Ref.vue'

@Options({
  components: { Ref }
})
export default class RefList extends Vue {}
</script>