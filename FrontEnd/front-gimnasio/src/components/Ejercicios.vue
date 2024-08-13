<template>
    <div class="container">
        <!-- Botón para mostrar el formulario -->
        <div class="row mb-4">
            <div class="col text-center">
                <button @click="mostrarFormulario = !mostrarFormulario" class="btn btn-danger">
                    {{ mostrarFormulario ? 'Ocultar' : 'Registrar' }} Ejercicio
                </button>
            </div>
        </div>

        <!-- Formulario que se muestra u oculta basado en la variable mostrarFormulario -->
        <div v-if="mostrarFormulario" class="row">
            <div class="col-md-6">
                <form action="#">
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="nombre" class="form-label">Nombre</label>
                                <input type="text" name="nombre" id="nombre" class="form-control" placeholder="nombre" required>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="descripcion" class="form-label">Descripción</label>
                                <input type="text" name="descripcion" id="descripcion" class="form-control" placeholder="descripción" required>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="video" class="form-label">Video</label>
                                <input type="file" name="video" id="video" class="form-control">
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="tipo" class="form-label">Tipo</label>
                                <select id="tipo" class="form-select" required>
                                    <option>Selecciona Tipo</option>
                                    <option>Aeróbico</option>
                                    <option>Resistencia</option>
                                    <option>Flexibilidad</option>
                                    <option>Fuerza</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="estatus" class="form-label">Estatus</label>
                                <select id="estatus" class="form-select" required>
                                    <option>Selecciona estatus</option>
                                    <option>Activo</option>
                                    <option>Inactivo</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="dificultad" class="form-label">Dificultad</label>
                                <select id="dificultad" class="form-select" required>
                                    <option>Selecciona dificultad</option>
                                    <option>Básico</option>
                                    <option>Intermedio</option>
                                    <option>Avanzado</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="fechar" class="form-label">Fecha de registro</label>
                                <input type="date" name="fechar" id="fechar" class="form-control">
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="fechaa" class="form-label">Fecha de actualización</label>
                                <input type="date" name="fechaa" id="fechaa" class="form-control">
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="recomendaciones" class="form-label">Recomendaciones</label>
                                <input type="text" name="recomendaciones" id="recomendaciones" class="form-control" placeholder="recomendaciones" required>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <label for="restricciones" class="form-label">Restricciones</label>
                                <input type="text" name="restricciones" id="restricciones" class="form-control" placeholder="restricciones" required>
                            </div>
                        </div>
                    </div>
                    <div class="d-flex justify-content-end">
                        <button type="submit" class="btn btn-danger">
                            Registrar
                        </button>
                    </div>
                </form>
            </div>
            <div class="col-md-6">
                <!-- Esta columna se dejó vacía para que el formulario ocupe solo la mitad de la pantalla -->
            </div>
        </div>

        <!-- Nueva fila para que ListarEjercicios ocupe toda la pantalla -->
        <div class="row mt-4">
            <div class="col">
                <ListarEjercicios />
            </div>
        </div>
    </div>
</template>

<script>
import ListarEjercicios from './ListarEjercicios.vue';

export default {
    components: {
        ListarEjercicios,
    },
    data() {
        return {
            mostrarFormulario: false,  // Estado que controla la visibilidad del formulario
        };
    },
};
</script>
