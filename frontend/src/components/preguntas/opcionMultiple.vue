<script type="text/javascript">

	var options

	export default {
		name: 'OpcionMultiple',
		props: {
			pregunta: {
				type: String,
				require: true,
				default: 'X'
			},
			opcion1: {
				type: String,
			//	require: true,
				default: 'X'
			},
			opcion2: {
				type: String,
				default: ''
			},
			opcion3: {
				type: String,
				default: ''
			},
			opcionCorrecta: {
				type: String,
				default: ''
			}
		},
		data() {
			return {
				selected: 'Null',
				opciones: []
			}
		},
		methods: {
			guardar() {
				this.opciones.push(this.opcion1)
				this.opciones.push(this.opcion2)
				this.opciones.push(this.opcion3)
				this.opciones.push(this.opcionCorrecta)
			},
			aleatorio() {
				var tam = this.opciones.length

				for (var i = 0; i < tam; i++) {
					var aleatorio = Math.floor(Math.random() * this.opciones.length)
					var seleccion = this.opciones[aleatorio]
					this.opciones.push(seleccion)
					this.opciones.splice(aleatorio, 1)
				}
			}
		},
		//
		created() {
			this.guardar(), this.aleatorio()
		}
	}

</script>

<template>

	<div>
		<b-form-group :label="pregunta">
			<b-form-radio v-model="selected" name="some-radios" :value="opciones[0]">{{opciones[0]}}</b-form-radio>
			<b-form-radio v-model="selected" name="some-radios" :value="opciones[1]">{{opciones[1]}}</b-form-radio>
			<b-form-radio v-model="selected" name="some-radios" :value="opciones[2]">{{opciones[2]}}</b-form-radio>
			<b-form-radio v-model="selected" name="some-radios" :value="opciones[3]">{{opciones[3]}}</b-form-radio>
		</b-form-group>

		<div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
		<div class="mt-3" v-if="selected === opcionCorrecta">Esto es: <strong>Correcto!</strong></div>
	</div>

</template>
