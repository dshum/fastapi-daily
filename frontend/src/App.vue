<template>
  <header class="bg-gray-800 text-white">
    <div class="container">
      <nav class="flex justify-between items-center h-16 font-navbar">
        <div>
          <router-link to="/" class="flex gap-2 text-xl font-logo text-rose-400">
            <font-awesome-icon :icon="['fas', 'bookmark']"/>
            <span>Daily</span>
          </router-link>
        </div>
        <div>
          <ul class="flex items-center gap-6">
            <li><a href="#">Dashboard</a></li>
            <li><a href="#">About</a></li>
          </ul>
        </div>
        <div>
          <router-link to="/register"><button class="bg-sky-600 text-white py-2 px-4 rounded-full">Sign Up</button></router-link>
        </div>
      </nav>
    </div>
  </header>

  <div class="container my-8">
    <router-view/>
  </div>
</template>

<script setup>
const isLogged = false
</script>
