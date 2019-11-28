<script>

	import Vue from 'vue'
	import axios from 'axios'
	import menuLecciones from '@/components/ova/menu_lecciones.vue'
	//import Slide from '@/components/ova/component_slide.vue'
	import Screen from '@/components/ova/component_screen.vue'
	import introduccion from '@/components/ova/presentacion/polimorfismo/introduccion.vue'
	import conceptos from '@/components/ova/presentacion/polimorfismo/conceptos.vue'
	import sobrecarga from '@/components/ova/presentacion/polimorfismo/sobrecarga.vue'
	import sobreescritura from '@/components/ova/presentacion/polimorfismo/sobreescritura.vue'
	import polimorficas from '@/components/ova/presentacion/polimorfismo/polimorficas.vue'
	import genericidad from '@/components/ova/presentacion/polimorfismo/genericidad.vue'
	import evaluarCodigo from '@/components/preguntas/codigoJudge2.vue'
	import evaluarCodigo2 from '@/components/preguntas/codigoJudge3.vue'

	Vue.component('actividades', {
		template: require('./component_introduccion.html'),
		props: ['componenteLeccion', 'numero', 'estado']
	})
	Vue.component('resumen', {
		template: require('./component_resumen.html')
	})
	Vue.component('evaluacion', {
		template: require('./component_evaluacion.html')
	})

	export default {
		components: {
			menuLecciones,
			Screen,
			introduccion,
			conceptos,
			sobrecarga,
			sobreescritura,
			polimorficas,
			genericidad,
			evaluarCodigo,
			evaluarCodigo2
			// Slide
		},
		data() {
			return {
				subtemas: [],
				componenteActual: 'introduccion'
			}
		},

		methods: {
			getsubtemas() {
				const path = 'http://localhost:8000/api_ova/1.0/Subtema/'
				axios
					.get(path)
					.then(response => {
						this.subtemas = response.data
					})
					.catch(error => {
						console.log(error)
					})
			}
			// getSlides() {
			// 	const path = 'http://localhost:8000/api_ova/1.0/Slide/'
			// 	axios
			// 		.get(path)
			// 		.then(response => {
			// 			this.slides = response.data
			// 		})
			// 		.catch(error => {
			// 			console.log(error)
			// 		})
			// }
		},

		created() {
			this.getsubtemas()
		}
	}

	Vue.component('menu-lecciones', menuLecciones)

</script>

<template>

	<div>
		<div id="nave">
			<bar-nave></bar-nave>
		</div>
		<div class="container-fluid">
			<div class="row">
				<div id="app" class="col-md-3 ui grid">
					<div class="four wide column">
						<div class="ui fluid inverted vertical menu">
							<h4 class="ui teal icon header center aligned">
								<i class="instagram icon"></i>
								<div class="content">
									Menu
								</div>
							</h4>
							<div role="tablist">
								<!-- / -->
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'introduccion'" variant="info">Introducción</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'conceptos'" variant="info">Conceptos</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'sobrecarga'" variant="info">Sobrecarga</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'sobreescritura'" variant="info">Sobreescritura</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'polimorficas'" variant="info">Variables polimórficas</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'genericidad'" variant="info">Genericidad</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'evaluarCodigo2'" variant="info">Examen</b-button>
									</b-card-header>
									<b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
										<b-card-body>
											<b-card-text>aaaaa</b-card-text>
										</b-card-body>
									</b-collapse>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'resumen'" variant="info">Resumen</b-button>
									</b-card-header>
									<!-- <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
																																	<b-card-body>
																																		<b-card-text>Resumen</b-card-text>
																																	</b-card-body>
																																</b-collapse> -->
								</b-card>
							</div>
						</div>
					</div>
				</div>
				<div align="left" class="col-md-9 CajaPadre">
					<div class="border rounded shadow CajaHijo">
						<div class="">
							<h3></h3>
						</div>

						<component :is="componenteActual"></component>

						<div class="">
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>

</template>

<style >

	.vertical.menu {
		height: 100vh;
		padding-top: 20px;
	}

	#content {
		padding-top: 20px;
	}

	.CajaPadre {
		width: 90%;
		height: 100%;
		padding-top: 50px !important;
		position: absolute;
		/* left: 5%;
																								  right: 5%; */
	}
	.CajaHijo {
		width: 100%;
		height: 90%;
		position: relative;
		padding: 5%;
	}
	div~~~h3,
	h2,
	h1,
	h4,
	h5,
	h6 {
		text-align: center;
	}

</style>
