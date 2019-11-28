<script  type="text/javascript">

	export default {
		name: 'falsoVerdadero',
		data() {
			return {
				form: {
					enunciado: '',
					respuesta: null,
					unidad: ''
				},
				selected: null,
				options: [{ value: 'falso', text: 'Falso' }, { value: 'verdadero', text: 'Verdadero' }],
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
				this.form.respuesta = null
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
			<h5>Crear pregunta Verdadero/Falso</h5>
			<br>
			<b-form-group id="input-group-1" label="Enunciado:">
				<b-form-textarea id="enunciado"
				                 v-model="form.enunciado"
				                 placeholder="Escriba el enunciado de la pregunta en este cuadro de texto"
				                 rows="3"
				                 no-resize>
				</b-form-textarea>
			</b-form-group>
			<b-form-group id="input-group-2" label="Respuesta:" label-for="input-3">
				<b-form-select id="respuesta" v-model="form.respuesta" :options="options"></b-form-select>
			</b-form-group>
			<!-- <div class="mt-3">Selected: <strong>{{ selected }}</strong></div> -->
			<b-form-group id="input-group-3">
				<b-form-radio-group id="radio-group-2" v-model="form.unidad" name="radio-sub-component">
					<b-form-radio value="punteros">Punteros</b-form-radio>
					<b-form-radio value="polimorfismo">Polimorfismo</b-form-radio>
					<b-form-radio value="estilo">Estilo de programación</b-form-radio>
        </b-form-radio-group>
			</b-form-group>
			<div>
				<b-button type="submit" variant="primary">Guardar</b-button>
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
