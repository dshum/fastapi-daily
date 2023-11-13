<template>
  <div class="login">
    <h1 class="text-4xl font-title text-rose-400">Login</h1>

    <div class="my-4 w-full max-w-sm">
      <form class="space-y-4">
        <div class="form-control">
          <label class="label">
            <span class="label-text">E-mail</span>
          </label>
          <input type="text" class="input input-bordered" autocomplete="email"/>
        </div>

        <div class="form-control">
          <label class="label">
            <span class="label-text">Password</span>
          </label>
          <input type="password" class="input input-bordered" autocomplete="password"/>
        </div>
        <a href="#" class="text-xs text-gray-600 hover:underline hover:text-blue-600">Forget Password?</a>

        <div class="form-control">
          <button type="submit" class="btn rounded-full">Login</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>

</script>