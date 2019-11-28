<script>

	import axios from 'axios'
	export default {
		name: 'registro',
		data() {
			return {
				form: {
					email: '',
					codigo: '',
					apellidos: '',
					nick: '',
					nombre: '',
					contrasena: '',
					plan: '',

					//			food: null,
					tipoUsuario: ''
				},
				//			foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],

				show: true
			}
		},
		methods: {
			onSubmit() {
				var nombres_form = String(this.form.nombre)
				var apellidos_form = String(this.form.apellidos)
				var username_form = String(this.form.nick)
				var email_form = String(this.form.email)
				var password_form = String(this.form.contrasena)
				var codigo_estudiante_form = String(this.form.codigo)
				var plan_form = String(this.form.plan)

				//	alert(JSON.stringify(this.form))

				const host = 'http://localhost:8000'
				const baseURL = '/api_usuarios/1.0/'
				let user = ''
				if (this.form.tipoUsuario == 'docente') {
					user = 'crear_docente/'
				} else if (this.form.tipoUsuario == 'estudiante') {
					user = 'crear_estudiante/'
				}
				alert(this.form.nombre)
				axios({
					method: 'post',
					url: host + baseURL + user,
					data: {
						nombres: nombres_form,
						apellidos: apellidos_form,
						username: username_form,
						email: email_form,
						password: password_form,
						codigo_estudiante: codigo_estudiante_form,
						plan: plan_form
					}
				})
			},
			onReset(evt) {
				evt.preventDefault()
				// Reset our form values
				this.form.email = ''
				this.form.nombre = ''
				this.form.apellidos = ''
				this.form.codigo = ''
				this.form.nick = ''
				this.form.contrasena = ''
				this.form.plan = ''
				//			this.form.food = null
				this.form.tipoUsuario = []
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

	<div>
		<div class="sombra redondeado_ border" id="registro">
			<div class="negrita_ titulo_ centrar">
				<h5>Registro</h5>
			</div>
			<br>
			<b-form @submit="onSubmit" @reset="onReset" v-if="show">

					<b-form-group id="input-group-2">
						<b-form-input id="input-2"
						              v-model="form.nombre"
						              required
						              placeholder="Ingrese sus nombres"></b-form-input>
					</b-form-group>
					<b-form-group  id="input-group-3">
						<b-form-input id="input-3"
						              v-model="form.apellidos"
						              required
						              placeholder="Ingrese sus apellidos"></b-form-input>
					</b-form-group>
					<b-form-group
					              id="input-group-1"
					              label-for="input-1">
						<b-form-input id="input-1"
						              v-model="form.email"
						              type="email"
						              required
						              placeholder="Email"></b-form-input>
					</b-form-group>


				<div class="row">
					<div class="col-md-6">
						<label class=" sr-only" for="inline-form-input-username">Username</label>
						<b-input-group prepend="@" class="mb-2 mr-sm-2 mb-sm-0">
							<b-input id="inline-form-input-username" v-model="form.nick" placeholder="Username"></b-input>
						</b-input-group>
					</div>
					<b-form-group class="col-md-6" id="input-group-14">
						<b-form-radio-group id="radio-group-2" v-model="form.tipoUsuario" required name="radio-sub-component">
							<b-form-radio value="docente">Docente</b-form-radio>
							<b-form-radio value="estudiante">Estudiante</b-form-radio>
						</b-form-radio-group>

					</b-form-group>
				</div>
				<br>
				<div class="row">
					<b-form-group class="col-md-8" id="input-group-7">
						<b-form-input id="input-5"
						              v-model="form.codigo"
						              required
						              placeholder="Código"></b-form-input>
					</b-form-group>
					<b-form-group class="col-md-4" id="input-group-8">
						<b-form-input id="input-6"
						              v-model="form.plan"
						              required
						              placeholder="Plan"></b-form-input>
					</b-form-group>

				</div>

				<div class="row">
					<b-form-group class="col-md-6" id="input-group-10">
						<b-input type="password"
						         id="text-password"
						         v-model="form.contrasena"
						         aria-describedby="password-help-block"
						         placeholder="Contraseña">
						</b-input>
					</b-form-group>
					<b-form-group class="col-md-6" id="input-group-11">
						<b-input type="password"
						         id="text-password-2"
						         aria-describedby="password-help-block"
						         placeholder="Repetir contraseña"></b-input>
					</b-form-group>
				</div>

				<br>
				<div class="centrar row">
					<b-button class="col-md-6 boton1_" type="submit">Registrar</b-button>
				</div>

			</b-form>
			<!-- <b-card class="mt-3" header="Form Data Result">
						<pre class="m-0">{{ form }}</pre>
					</b-card> -->

		</div>
	</div>

</template>

<style>

	#registro {
		background-color: #ffffff;
		padding: 2em;
	}

</style>
