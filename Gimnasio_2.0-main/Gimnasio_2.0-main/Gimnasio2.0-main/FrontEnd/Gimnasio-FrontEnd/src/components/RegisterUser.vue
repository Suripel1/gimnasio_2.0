<template>
        <div id="login-popup" tabindex="-1"
    class="bg-black/50 overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-[999] h-full items-center justify-center popup flex">
    <div class="relative p-4 w-full max-w-md h-full md:h-auto">
        <div class="relative bg-white rounded-lg shadow popup-body">
            <button type="button"
                class="absolute top-3 right-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center popup-close">
                <svg aria-hidden="true" class="w-5 h-5" fill="#c6c7c7" viewBox="0 0 20 20"
                    xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                        d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                        cliprule="evenodd"></path>
                </svg>
                <span class="sr-only">Cerrar</span>
            </button>
            <div class="p-5">
                <h3 class="text-2xl mb-0.5 font-medium"> </h3>
                <p class="mb-4 text-sm font-normal text-gray-800"> </p>
                <div class="mb-7 text-center">
                    <p class="mb-3 text-2xl font-semibold leading-5 text-slate-900">
                        Registrar Usuario
                    </p>
                    <p class="mt-2 text-sm leading-4 text-slate-600">
                        Completa los campos
                    </p>
                </div>
                <div>
                    <div class="flex w-full flex-col gap-2">
                    </div>
                    <div class="flex w-full items-center gap-2 py-6 text-sm text-slate-600">
                       
                        <div class="h-px w-full bg-slate-200"></div>
                    </div>
                    <form class="w-full">
                        
                        <lavel for="" class= "font-medium">Datos Personales</lavel>
                        <br>
                        <br>
                        <input name="email" type="email" autocomplete="email" required=""
                        class="block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Nombre Completo" value="">
                        
                        <input name="password" type="email" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Primer Apellido" value="">
                        
                        <input name="password" type="email" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Segundo Apellido" value="">
                        
                        <input name="password" type="email" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Titulo de Cortesia" value="">

                        <select id="countries" class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1">
                        <option selected>Selecciona Genero</option>
                        <option value="">Hombre</option>
                        <option value="">Mujer</option>
                        <option value="">Otro</option>
                       
                        </select>
                        
                        <input name="password" type="date" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="" value="">
                        
                        <select id="countries" class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1">
                        <option selected>Selecciona Tipo de Sangre</option>
                        <option value="">AB+</option>
                        <option value="">AB-</option>
                        <option value="">O+</option>
                        <option value="">0-</option>
                        </select>

                        <br>
                        <lavel for="" class= "font-medium">Fotografia</lavel>
                        <br>
                        <input name="password" type="file" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Fotografia" value="">
                        <br>  
                        
                        <lavel for="" class= "font-medium">Datos de Acceso</lavel>
                        <br>
                        <input name="password" type="email" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Correo" value="">
                        
                        <input name="password" type="password" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Contraseña" value="">

                        
                        <input name="password" type="password" autocomplete="current-password" required=""
                        class="mt-2 block w-full rounded-lg border border-gray-300 px-3 py-2 shadow-sm outline-none placeholder:text-gray-400 focus:ring-2 focus:ring-black focus:ring-offset-1"
                        placeholder="Confirmar Contraseña" value="">


                        <br>
                        <br>   
                        <a href="/Menu">
                        <button type="submit" 
                            class="inline-flex w-full items-center justify-center rounded-lg bg-black p-2 py-3 text-sm font-medium text-white outline-none focus:ring-2 focus:ring-black focus:ring-offset-1 disabled:bg-gray-400">Registrar</button>
                        </a>
                        
                        </form>
                </div>
                <div class="mt-6 text-center text-sm text-slate-600">

                </div>
            </div>
        </div>
    </div>
</div>
</template>