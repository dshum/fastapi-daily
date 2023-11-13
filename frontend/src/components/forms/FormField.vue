<template>
  <div class="my-6">
    <label class="block mb-2 font-bold text-stone-400" v-bind:for="field.id">{{ field.title }}</label>
    <component :is="type" :field="field" v-model="inputValue"></component>
  </div>
</template>

<script setup>
import {computed} from "vue";

defineProps(["field", "modelValue"])

const inputValue = computed({
  get() {
    return this.modelValue;
  },
  set(val) {
    this.$emit('input2', val);
  }
})
</script>