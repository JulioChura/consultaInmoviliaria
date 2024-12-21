<script setup>

</script>

<template>
    <form class="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
        <h2 class="text-xl font-semibold mb-4">Formulario de Contacto</h2>
        
        
        <div class="mb-4">
          <label for="name" class="block text-sm font-medium text-gray-700">Nombre</label>
          <input type="text" id="name" name="name" class="mt-1 p-2 w-full border border-gray-300 rounded-md" />
        </div>
        
        <div class="mb-4">
          <label for="email" class="block text-sm font-medium text-gray-700">Correo Electrónico</label>
          <input type="email" id="email" name="email" class="mt-1 p-2 w-full border border-gray-300 rounded-md" />
        </div>
        
        <div class="flex justify-center">
          <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">
            Enviar
          </button>
        </div>
    </form>
</template>