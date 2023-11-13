<template>
  <div class="lg:w-1/2 xl:w-1/3">
    <h1>Sign Up</h1>

    <form>
      <div class="form-control">
        <label for="username">E-mail</label>
        <input type="text" id="username" v-model="formFields.username">
      </div>
      <div class="form-control">
        <label for="first_name">First name</label>
        <input type="text" id="first_name" v-model="formFields.first_name">
      </div>
      <div class="form-control">
        <label for="last_name">Last name</label>
        <input type="text" id="last_name" v-model="formFields.last_name">
      </div>
      <div class="form-control">
        <button class="btn btn-primary">Submit</button>
      </div>
    </form>

    {{ formFields }}
  </div>
</template>

<script setup>
  import {ref} from "vue";

  const formFields = ref({
    username: "",
    first_name: "",
    last_name: "",
  })
</script>