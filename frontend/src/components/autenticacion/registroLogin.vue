<script>

	import axios from 'axios'

	import registro from '@/components/autenticacion/registro/registro.vue'
	import login from '@/components/autenticacion/login/login.vue'

	export default {
		components: {
			registro,
			login
			// Slide
		},
		data() {
			return {
				subtemas: [],
				componenteLogin: 'login',
				componenteRegistro: 'registro'
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

		created() {
			this.getsubtemas()
		}
	}

</script>

<template>

	<div>
		<div id="nave">
			<component :is="componenteLogin"></component>
			<!-- <bar-nave></bar-nave> -->
		</div>
		<div class="container-fluid">
			<div class="row justify-content-md-center fondo">
				<div align="left" class="col-md-4 hijo">

						<component :is="componenteRegistro"></component>

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

	.padre {
		width: 90%;
		height: 100%;
		padding-top: 50px !important;
		position: absolute;
		/* left: 5%;
																										  right: 5%; */
	}
	.hijo {
		width: 100%;
		height: 90%;
		position: relative;
		padding: 6%;
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
