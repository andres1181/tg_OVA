import Vue from 'vue'

Vue.component('bar-nave', {
  template: require('./componentmenunav/menunav.html')
  // `<div>A custom component! xcxc</div>`
})

Vue.component('leccion', {
  template: require('./component_leccion/menu_lecciones.html'),
  props: ['subtema', 'numero', 'estado']
  // `<div>A custom component! xcxc</div>`
})

new Vue({
     el: '#app'
})
