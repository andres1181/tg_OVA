<script>

	import axios from 'axios'
	export default {
		name: 'evaluarCodigo2',
		// props: {
		// 	fuente: {
		// 		type: String,
		// 		default: ''
		// 	},
		// 	salida: {
		// 		type: String,
		// 		default: ''
		// 	}
		// },
		data() {
			return {
				posts: [],
				form: {
					codigoFuente: 'LALalSLsldSDJKL',
					salidaEsperada: 'Hola Mundo'
					// codigoFuente: this.fuente,
					// salidaEsperada: this.salida
				},
				selected: '',
				show: true,
				codLenguaje: 'cpp'
			}
		},
		methods: {
			enviarCodigo: function() {
				var mensaje = document.getElementById('mensaje')
				var fuente = this.form.codigoFuente //this.form.codigoFuente //btoa(this.form.codigoFuente)
				var lenguaje = this.codLenguaje //btoa(this.codLenguaje)
				var salida = this.salidaEsperada //btoa(this.salidaEsperada)
				axios
					//	.post('https://judge0.p.rapidapi.com/submissions', {
					.post('http://api.paiza.io/runners/create', {
						// headers: {
						// 	'content-type': 'application/x-www-form-urlencoded',
						// 	'x-rapidapi-host': 'paiza-io.p.rapidapi.com',
						// 	'x-rapidapi-key': 'cd7a56d70dmsh276272def56419ep1313e3jsn52fbad167a86'
						// },
						params: {
							language: lenguaje,
							source_code: fuente
						},
						data: {
							// source_code: fuente,
							// language_id: lenguaje,
							// //	cpu_time_limit: '1',
							// expected_output: salida
						}
					})
					.then(response => {
						// if (response.status == 201) {
						// 	mensaje.innerHTML = 'El nuevo Post ha sido almacenado con id: '
						// }else {
						// 	mensaje.innerHTML = 'No hay Post ha sido almacenado con id: '
						// }
						console.log(response)

						// let status_id = response.data.status.id
						// if (status_id == '3') {
						// 	//mensaje.innerHTML = 'Correcto'
						// 	this.selected = 'Correcto'
						// } else if (status_id !== '3') {
						// 	//	mensaje.innerHTML = 'Hubo un error'
						// 	this.selected = 'Hubo un error'
						// } else {
						// 	this.selected = 'Hubo un error extraño'
						// }
					})
					.catch(e => {
						console.log(e)
						console.log(e.response)
					})
			},
			onSubmit(evt) {
				evt.preventDefault()
				alert(JSON.stringify(this.form))
			},
			onReset(evt) {
				evt.preventDefault()
				// Reset our form values
				this.form.codigoFuente = ''
				//		this.form.salidaEsperada = ''
				//			this.form.unidad = ''
				// Trick to reset/clear native browser form validation state
				this.show = false
				this.$nextTick(() => {
					this.show = true
				})
			}
		}
	}

</script>

<template>

	<div class="">
		<b-form @submit="onSubmit" @reset="onReset" @change="enviarCodigo" v-if="show">
			<h5>Crear codigo 3</h5>
			<br>
			<b-form-group id="input-group-1" label="Enunciado:">
				<b-form-textarea id="fuente"
				                 v-model="form.codigoFuente"
				                 required
				                 placeholder="Escriba el enunciado de la pregunta en este cuadro de texto"
				                 rows="3">

				</b-form-textarea>
				<br>
				<!-- <b-form-input id="respuesta"
								              v-model="form.salidaEsperada"
								              type="text"
								              required
								              placeholder="Ingrese la salida esperada"></b-form-input>
								<br> -->

			</b-form-group>
			<!-- <div class="mt-3">Selected: <strong>{{ selected }}</strong></div> -->
			<div>
				<b-button type="change">Comprobar</b-button>
				<b-button type="reset" variant="danger">Limpiar</b-button>
			</div>

		</b-form>
		<div id="mensaje"></div>
	</div>

</template>

<style>

</style>
