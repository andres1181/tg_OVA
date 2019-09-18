<script>

	import Vue from 'vue'
	import axios from 'axios'


	export default {
		data() {
			return {
				subtemas: [],
				componenteActual: 'introduccion',
				// toggle_I: true,
				// toggle_E: false,
				// toggle_R: false,
				// toggle_L: false,
				// toggle_A: false
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
		},
			// 	ocultar() {
			// 		if (toggle_I) {
			// 			toggle_E: false
			// 			toggle_R: false
			// 			toggle_L: false
			// 		} else if (toggle_E) {
			// 			toggle_I: false
			// 			toggle_R: false
			// 			toggle_L: false
			// 		} else if (toggle_R) {
			// 			toggle_I: false
			// 			toggle_E: false
			// 			toggle_L: false
			// 		} else if (toggle_L) {
			// 			toggle_I: false
			// 			toggle_E: false
			// 			toggle_R: false
			// 		}
			// 	}
			// },

			created() {
				// var toggle_I= true
				// var toggle_E= false
				// var toggle_R= false
				// var toggle_L= false
				this.getsubtemas()
				// this.ocultar()
			}
		}


	Vue.component('evaluacion', {
		template: require('./component_evaluacion.html')
		// `<div>A custom component! xcxc</div>`
	})

	Vue.component('introduccion', {
		template: require('./component_introduccion.html')
		// `<div>A custom component! xcxc</div>`
	})
	Vue.component('actividades', {
		template: require('./component_introduccion.html')
		// `<div>A custom component! xcxc</div>`
	})
	Vue.component('resumen', {
		template: require('./component_resumen.html')
		// `<div>A custom component! xcxc</div>`
	})
	Vue.component('evaluacion', {
		template: require('./component_evaluacion.html')
		// `<div>A custom component! xcxc</div>`
	})

</script>

<template>

	<div>

		<!-- <div id="uno">
																	<MenuPrin>This is a small message!</MenuPrin>
																	<MenuPrin>Another one</MenuPrin>
																</div> -->
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
									<!-- <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
																							<b-card-body>
																								<b-card-text>I start opened because <code>visible</code> is <code>true</code></b-card-text>
																								<b-card-text>AAAA</b-card-text>
																							</b-card-body>
																					</b-collapse> -->
								</b-card>

								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-b-toggle.accordion-2 variant="info">Lecciones</b-button>
									</b-card-header>
									<b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
										<b-card-body>
											<div v-for="sub in subtemas" data-spy="scroll">
												<leccion :subtema="sub.titulo" :numero="sub"></leccion>
											</div>
										</b-card-body>
									</b-collapse>
								</b-card>

								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'evaluacion'" variant="info">Evaluación</b-button>
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
		height: auto;
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
div h3,h2,h1,h4, h5, h6 {
	text-align: center;
}
</style>
