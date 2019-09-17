import Vue from 'vue'
import Router from 'vue-router'

import list-ova from '@/components/ova/list-ova'
import component_ova from '@/components/ova/component_ova'


Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/ovas',
            name: 'list-ova',
            component: list-ova
        },
        {
            path: '/ovas/ova',
            name: 'component_ova',
            component: component_ova
        }
    ],

    mode: 'history'
})
