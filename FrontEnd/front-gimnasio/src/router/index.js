import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '@/components/Login.vue'
import RegisterUserView from '@/components/RegisterUser.vue'
import DashboardView from '@/components/Dashboard.vue'
import Persona from '@/components/Persona.vue'
import PiePagina from '@/components/PiePagina.vue'
import Ejercicios from '@/components/Ejercicios.vue'
import Home from '@/components/Home.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterUserView
    }
    ,
    {
      path: '/dashboard',
      name: 'dashboard',
      component: DashboardView,
      children:[
        {path:'/home', name: 'home', component:Home},
        {path:'/personas', name: 'personas', component:Persona},
        {path:'/piepagina', name: 'piepagina', component: PiePagina},
        {path:'/ejercicios', name: 'ejercicios', component: Ejercicios},
      ]
    }
  ]
})

export default router
