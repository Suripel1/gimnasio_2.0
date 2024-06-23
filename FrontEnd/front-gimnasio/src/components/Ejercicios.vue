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
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Nombre</label>
                                <input type="text" name="nombre" id="nombre"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="nombre" required="">
                            </div>
                            <div>
                                <label for="Descripcion"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Descripcion</label>
                                <input type="text" name="descripcion" id="descripcion"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="descripcion" required="">
                            </div>
                            <div>
                                <label for="video"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Video</label>
                                <input type="file" name="titulo" id="titulo"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="Mr." required="">
                            </div>
                            <div>
                                <label for="tipo"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">
                                    Tipo</label>
                                <select id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option>Selecciona Tipo</option>
                                    <option>Aerobico</option>
                                    <option>Resistencia</option>
                                    <option>Flexibilidad</option>
                                    <option>Fuerza</option>
                                </select>
                            </div>
                            <div>
                                <label for="estatus"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Estatus</label>
                                <select id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option>Selecciona estatus</option>
                                    <option>Activo</option>
                                    <option>Inactivo</option>
                                </select>
                            </div>
                            <div>
                                <label for="dificultad"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Difucultad</label>
                                <select id="countries"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
                                    <option>Selecciona dificultad</option>
                                    <option>Basico</option>
                                    <option>Intermedio</option>
                                    <option>Avanzado</option>
                                </select>
                            </div>
                            <div>
                                <label for="fechar"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Fecha de
                                    registro</label>
                                <input type="date" name="fechar" id="fechar"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            </div>
                            <div>
                                <label for="fechaa"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Fecha de
                                    actualizacion</label>
                                <input type="date" name="fechaa" id="fechaa"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500">
                            </div>

                            <div>
                                <label for="recomendaciones"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Recomendaciones</label>
                                <input type="text" name="recomendaciones" id="recomendaciones"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="recomendaciones" required="">
                            </div>
                            <div>
                                <label for="restricciones"
                                    class="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-900">Restricciones</label>
                                <input type="text" name="restricciones" id="restricciones"
                                    class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-600 focus:border-blue-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-900 dark:focus:ring-blue-500 dark:focus:border-blue-500"
                                    placeholder="restricciones" required="">
                            </div>
                        <div class="w-full flex justify-end mb-4">
                            <button type="submit"
                                class="text-gray-900 bg-red-600 hover:bg-red-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
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
        <ListarEjercicios />
    </div>
  </div>
</div>
    
</template>
<script>
import ListarEjercicios from './ListarEjercicios.vue'
export default {
    components: {
        ListarEjercicios
    }
}
</script>