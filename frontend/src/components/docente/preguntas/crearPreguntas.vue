<script>

	import Vue from 'vue'
	import axios from 'axios'

  import falsoVerdadero from '@/components/docente/preguntas/crear_FV.vue'
  import crearOM from '@/components/docente/preguntas/crear_OM.vue'
  import arrastrarSoltar from '@/components/docente/preguntas/crear_AyS.vue'
  import enlazar from '@/components/docente/preguntas/crear_Enlazar.vue'
	import crearCompletar from '@/components/docente/preguntas/crear_Completar.vue'

	export default {
		components: {
			falsoVerdadero,
      crearOM,
      arrastrarSoltar,
      enlazar,
			crearCompletar
		},
		data() {
			return {
				subtemas: [],
				componenteActual: 'falsoVerdadero'
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
										<b-button block href="#" v-on:click="componenteActual = 'falsoVerdadero'" variant="info">Falso y Verdadero</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'crearOM'" variant="info">Opción Múltiple</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'arrastrarSoltar'" variant="info">Arrastrar y Soltar</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'enlazar'" variant="info">Enlazar</b-button>
									</b-card-header>
								</b-card>
								<b-card no-body class="mb-1">
									<b-card-header header-tag="header" class="p-1" role="tab">
										<b-button block href="#" v-on:click="componenteActual = 'crearCompletar'" variant="info">Completar</b-button>
									</b-card-header>
								</b-card>
							</div>
						</div>
					</div>
				</div>
				<div align="left" class="col-md-9 CajaPadre">
					<div class="rounded CajaHijo">
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
		height: 520px;
		padding-top: 50px !important;
		position: absolute;
	}
	.CajaHijo {
		width: 100%;
		height: 500px;
		position: relative;
		background-color: #ffffff;
		padding: 5%;
		overflow: scroll;
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
