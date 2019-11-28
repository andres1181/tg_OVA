<script  type="text/javascript">

	import OpcionMultiple from '@/components/preguntas/opcionMultiple.vue'

	export default {
		name: 'crearOM',
		components: {
			OpcionMultiple
		},
		data() {
			return {
				form: {
					enunciado: '',
					respuestaCorrecta: '',
					opcion1: '',
					opcion2: '',
					opcion3: '',
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
				alert(JSON.stringify(this.form))
			},
			onReset(evt) {
				evt.preventDefault()
				// Reset our form values
				this.form.enunciado = ''
				this.form.respuestaCorrecta = ''
				this.form.opcion1 = ''
				this.form.opcion2 = ''
				this.form.opcion3 = ''
				this.form.unidad = ''
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
		<b-form @submit="onSubmit" @reset="onReset" v-if="show">
			<h5>Crear pregunta opción múltiple</h5>
			<br>
			<b-form-group id="input-group-1" label="Enunciado:">
				<b-form-textarea id="enunciadoq"
				                 v-model="form.enunciado"
				                 required
				                 placeholder="Escriba el enunciado de la pregunta en este cuadro de texto"
				                 rows="3"
				                 no-resize>
				</b-form-textarea>
				<br>
				<b-form-input id="opcion_Correcta"
				              v-model="form.respuestaCorrecta"
				              type="text"
				              required
				              placeholder="Ingrese aquí la opcion correcta"></b-form-input>
				<br>
				<b-form-input id="opcion1"
				              v-model="form.opcion1"
				              type="text"
				              required
				              placeholder="Ingrese aquí una opción INCORRECTA"></b-form-input>
				<br>
				<b-form-input id="opcion_2"
				              v-model="form.opcion2"
				              type="text"
				              required
				              placeholder="Ingrese aquí una opción INCORRECTA"></b-form-input>
				<br>
				<b-form-input id="opcion_3"
				              v-model="form.opcion3"
				              type="text"
				              required
				              placeholder="Ingrese aquí una opción INCORRECTA"></b-form-input>
			</b-form-group>
			<!-- <div class="mt-3">Selected: <strong>{{ selected }}</strong></div> -->
			<b-form-group id="input-group-3">
				<b-form-radio-group id="radio-group-2" v-model="form.unidad" required name="radio-sub-component">
					<b-form-radio value="punteros">Punteros</b-form-radio>
					<b-form-radio value="polimorfismo">Polimorfismo</b-form-radio>
					<b-form-radio value="estilo">Estilo de programación</b-form-radio>
				</b-form-radio-group>
			</b-form-group>
			<div>
				<b-button type="submit">Guardar</b-button>
				<b-button type="reset" variant="danger">Limpiar</b-button>
			</div>

		</b-form>

		<b-card class="mt-3" header="Form Data Result">
			<pre class="m-0">{{ form }}</pre>
		</b-card>
	</div>

</template>

<style>

</style>
