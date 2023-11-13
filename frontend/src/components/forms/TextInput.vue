<template>
  <input type="text" :id="field.id" :name="field.name" v-model="inputValue"
         class="block rounded-lg py-2 px-4 text-lg w-full
         border border-stone-200 text-stone-600 focus:border-stone-300
         focus:outline-none focus:ring focus:ring-lime-300 focus:ring-offset-2">
</template>

<script setup>
import {computed} from "vue";

defineProps({
  field: {
    type: Object,
    default: () => ({}),
  },
  modelValue: String,
})

const inputValue = computed({
  get() {
    return this.modelValue;
  },
  set(val) {
    this.$emit('input', val);
  }
})
</script>