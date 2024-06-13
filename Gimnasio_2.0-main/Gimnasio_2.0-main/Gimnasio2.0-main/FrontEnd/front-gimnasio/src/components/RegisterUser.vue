<template>
  <div class="min-h-screen bg-gray-100 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
    <div class="max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden md:max-w-2xl">
      <div class="bg-white py-8 px-4 shadow sm:rounded-lg sm:px-10">
        <h1 class="text-2xl xl:text-2xl font-extrabold pb-8">Datos de persona</h1>
        <hr class="pb-8"/>
        <Persona></Persona>
        <h1 class="text-2xl xl:text-2xl font-extrabold pb-8">Datos de acceso</h1>
        <hr class="pb-8"/>
        <Usuario></Usuario>
        <RouterLink to="/">
          <div class="w-full flex justify-center">
          <button type="submit" class="text-white bg-red-700 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-red-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-red-600 dark:hover:bg-red-700 dark:focus:ring-red-800">
          Cancelar
          </button>
        </div>
        </RouterLink>
      </div>
    </div>
  </div>           
</template>

<script>
import Persona from './Persona.vue'
import Usuario from './Usuario.vue'
export default {
  components: {
    Persona,
    Usuario
  }
}
</script>