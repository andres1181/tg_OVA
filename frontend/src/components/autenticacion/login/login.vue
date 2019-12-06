<script>

	import axios from 'axios'
	export default {
		name: 'login',
		data() {
			return {
				input: {
					username: '',
					password: ''
				}
			}
		},
		methods: {
			login() {
				if (this.input.username != '' && this.input.password != '') {
					if (
						this.input.username == this.$parent.mockAccount.username &&
						this.input.password == this.$parent.mockAccount.password
					) {
						this.$emit('authenticated', true)
						this.$router.replace({ name: 'secure' })
					} else {
						console.log('The username and / or password is incorrect')
					}
				} else {
					console.log('A username and password must be present')
				}
			}
		}
	}

</script>

<template>

	<div>
		<b-navbar class="color1_ navbar_" id="barraLogin" fixed="top" toggleable="lg" type="dark" variant="info">
			<b-navbar-brand href="#">Logo</b-navbar-brand>

			<b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

			<b-collapse id="nav-collapse" is-nav>
				<!-- <b-navbar-nav>
							<b-nav-item href="#">Link</b-nav-item>
							<b-nav-item href="#" disabled>Disabled</b-nav-item>
						</b-navbar-nav> -->

				<b-navbar-nav class="ml-auto">
					<div>
						<b-form inline @submit.prevent="login">
							<label class="sr-only" for="usuario">Usuario</label>
							<b-input id="usuario"
							         class="mb-2 mr-sm-2 mb-sm-0"
							         placeholder="Código, Usuario o Correo"></b-input>

							<label class="sr-only" for="contrasena">Contraseña</label>
							<b-input-group class="mb-2 mr-sm-2 mb-sm-0">
								<b-input id="contrasena" type="password" placeholder="Contraseña"></b-input>
							</b-input-group>

							<!-- <b-form-checkbox class="mb-2 mr-sm-2 mb-sm-0">Remember me</b-form-checkbox> -->

							<b-button>Ingresar</b-button>
						</b-form>
					</div>
				</b-navbar-nav>
			</b-collapse>
		</b-navbar>
	</div>

</template>

<style>

	#barraLogin {
		/*  margin-bottom: 100px;*/
	}

</style>
