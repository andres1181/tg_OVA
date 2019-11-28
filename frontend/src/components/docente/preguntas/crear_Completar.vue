<script type="text/javascript">

	export default {
		name: 'crearCompletar',
		data() {
			return {
				text: '', // Estas variables son auxiliares, poe lo tanto las debo poner afuera del form
				opcion: '', // Estas variables son auxiliares, poe lo tanto las debo poner afuera del form
				form: {
					enunciado: [],
					espacios: [],
					numEspacios: 0,
					unidad: ''
				},
				selected: null,
				//				options: [{ value: 'falso', text: 'Falso' }, { value: 'verdadero', text: 'Verdadero' }],
				show: true
			}
		},
		methods: {
			onSubmit(evt) {
				evt.preventDefault()
				//      spanTexto(this.texto)
				alert(JSON.stringify(this.form))
			},
			onReset(evt) {
				evt.preventDefault()
				// Reset our form values
				this.form.enunciado = ['']
				this.form.respuestaCorrecta = ''
				this.form.opcion = ''
				this.form.unidad = ''
				// Trick to reset/clear native browser form validation state
				this.show = false
				this.$nextTick(() => {
					this.show = true
				})
			},
			agregarTexto() {},
			spanTexto() {
				var spanT = '<span>' + this.text + ' </span>'

				this.form.enunciado.push(spanT)
			},
			spanEspacio() {
				this.form.numEspacios += 1
				var spanE = '<span> | ' + this.form.numEspacios + ' |</span>'
				this.form.enunciado.push(spanE)
				this.form.espacios.push(this.opcion)
			}
		}
	}

</script>

<template>

	<div>
		<b-form @submit="onSubmit" @reset="onReset" v-if="show">
			<div class="row">

				<div class="col-md-9">
					<b-form-group id="input-group-1">
						<b-form-input id="texto"
						              type="text"
						              v-model="text"
						              placeholder="Ingrese un texto"></b-form-input>

					</b-form-group>
				</div>
				<div align="left" class="col-md-3">
					<b-button type="submit" v-on:click="spanTexto">Agregar</b-button>
				</div>
			</div>
			<div class="row">
				<div class="col-md-9">
					<b-form-group id="input-group-2">
						<b-form-input id="texto"
						              type="text"
						              v-model="opcion"
						              placeholder="Ingrese aquí información de un espacio en blanco"></b-form-input>

					</b-form-group>
				</div>
				<div align="left" class="col-md-3">
					<b-button type="submit" v-on:click='spanEspacio'>Agregar</b-button>
				</div>

			</div>
      <div>
        <b-form-group id="input-group-3">
          <b-form-radio-group id="radio-group-1" v-model="form.unidad" required name="radio-sub-component">
            <b-form-radio value="punteros">Punteros</b-form-radio>
            <b-form-radio value="polimorfismo">Polimorfismo</b-form-radio>
            <b-form-radio value="estilo">Estilo de programación</b-form-radio>
          </b-form-radio-group>
        </b-form-group>
      </div>
		</b-form>
		<b-card class="mt-3" header="Previsualizacion">
			<pre class="m-0">{{ form }}</pre>
		</b-card>
	</div>

</template>

<style>

</style>
