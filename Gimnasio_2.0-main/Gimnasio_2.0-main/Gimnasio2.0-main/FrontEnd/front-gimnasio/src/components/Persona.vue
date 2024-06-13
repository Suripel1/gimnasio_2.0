<template>
    <div class="container text-center">
  <div class="row">
    <div class="col">
        <div class="container text-center">
        <div class="row">
            <div class="col">
            Column
            </div>
            <div class="col">
                <form action="#">
                            <div>
                                <label for="Nombre"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Nombre</label>
                                <input type="text" name="nombre" id="nombre"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="nombre" required="">
                            </div>
                            <div>
                                <label for="Primer Apellido"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Primer
                                    apellido</label>
                                <input type="text" name="papellido" id="papellido"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="papellido" required="">
                            </div>
                            <div>
                                <label for="Segundo Apellido"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Segundo
                                    apellido</label>
                                <input type="text" name="sapellido" id="sapellido"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="sapellido">
                            </div>
                            <div>
                                <label for="titulo"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Titulo de
                                    cortesía</label>
                                <input type="text" name="titulo" id="titulo"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="Mr." required="">
                            </div>
                            <div>
                                <label for="fechan"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Fecha de
                                    nacimiento</label>
                                <input type="date" name="fechan" id="fechan"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            </div>
                            <div>
                                <label for="foto"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Foto</label>
                                <input type="file" name="titulo" id="titulo"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="Mr." required="">
                            </div>
                            <div>
                                <label for="genero"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Selecciona el
                                    genero</label>
                                <select id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option>Selecciona genero</option>
                                    <option>Hombre</option>
                                    <option>Mujer</option>
                                    <option>Otro</option>
                                </select>
                            </div>
                            <div>
                                <label for="sangre"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Selecciona tipo
                                    de sangre</label>
                                <select id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option>Selecciona tipo de sangre</option>
                                    <option>A+</option>
                                    <option>A-</option>
                                    <option>B+</option>
                                    <option>B-</option>
                                    <option>AB+</option>
                                    <option>AB-</option>
                                    <option>O+</option>
                                    <option>O-</option>
                                </select>
                            </div>
                        <div class="w-full flex justify-end mb-4">
                            <button type="submit"
                                class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
                                Registrar
                            </button>
                        </div>
                    </form>
            </div>
            <div class="col">
            Column
            </div>
        </div>
        </div>

    </div>
    </div>
    <div class="row">
    <div class="col">
        <ListarPersonas />
    </div>
  </div>
</div>
    
</template>
<script>
import ListarPersonas from './ListarPersonas.vue'
export default {
    components: {
        ListarPersonas
    }
}
</script>