import Vue from 'vue'
import Router from 'vue-router'

import list_ova from '@/components/ova/list_ova.vue'
import component_ova from '@/components/ova/component_ova.vue'
import crearPreguntas from '@/components/docente/preguntas/crearPreguntas.vue'


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/ovas',
            name: 'list_ova',
            component: list_ova
        },
        {
            path: '/ovas/ova',
            name: 'component_ova',
            component: component_ova
        },
        {
            path: '/docente/crear_actividades',
            name: 'crearPreguntas',
            component: crearPreguntas
        }
    ],

    mode: 'history'
})
