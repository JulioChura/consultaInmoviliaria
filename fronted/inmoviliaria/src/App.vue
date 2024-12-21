<script setup>
import Form from './components/Form.vue';
</script>

<template>
  <div class="relative h-screen">
    <!-- Fondo con opacidad -->
    <div class="absolute inset-0 bg-cover bg-center" 
         style="background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQTiwfJ0sSCgYj2jQZ4m-Jo1ghX4ZdQYsR8Tg&s');">
      <div class="absolute inset-0 bg-black bg-opacity-50"></div> 
    </div>
  
    <!-- Contenido -->
    <div class="relative flex flex-col items-center justify-center h-full text-center text-gray-100">
      <!-- Título -->
      <h1 class="text-4xl md:text-6xl font-bold mb-8">
        Los mejores lugares para vivir
      </h1>
      <!-- Formulario -->
      <div class="w-full max-w-lg px-4">
        <Form />
      </div>
    </div>
  </div>
  
</template>



<style></style>