<script>

	import Vue from 'vue'
	import axios from 'axios'


	// Vue.component('Leccion', { template: require('./component_screen.html') })

	export default {
		// components: {
		// 	Leccion
		// },
		name: 'menuLecciones',
		props: {
			subtema: {
				type: String,
				default: '' // whatever you want as default
			}
		},
		data() {
			return {
				componente: 'introduccion'
			}
		}
	}

</script>

<template >

	<!-- <div>
		<br>
		<div>
			<div class="row">
				<div align="left" class="col-md-6">
					<span><h6>{{subtema}}</h6></span>
				</div>
				<div class="col-md-6" align="right">
					<button v-on:click="componente = 'Leccion'" name="button" class="btn btn-dark rounded">Ir</button>
				</div>
			</div>
			<br>
			<div class="row">
				<div align="left" class="col-md-6">
					<h6>Actividades</h6>
				</div>
				<div class="col-md-6" align="right">
					<button type="button" name="button" class="btn btn-dark rounded">Ir</button>
				</div>
			</div>
		</div>
		<br>
		<hr>
	</div> -->

</template>

<style>

</style>
