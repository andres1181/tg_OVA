<script>

	export default {
		name: 'falsoVerdadero',
		props: {
			pregunta: {
				type: String,
				require: true,
				default: 'X'
			},
			respuesta: {
				type: String,
				require: true,
				default: 'falso'
			}
		},
		data() {
			return {
				selected: 'null'
				// ,
				//				options: [opcionIncorrecta, opcionCorrecta]
			}
		}
		// ,
		// methods: {
		// 	aleatorio() {
		// 		var tam = options.length
		//
		// 		for (var i = 0; i < tam; i++) {
		// 			aleatorio = Math.floor(Math.random() * options.length)
		// 			seleccion = options[aleatorio]
		// 			trace(seleccion)
		// 			options.splice(aleatorio, 1)
		// 		}
		// 	}
		// },
		//
		// created() {
		// 	this.aleatorio()
		// }
	}

</script>

<template>

	<div>
		<b-form-group :label="pregunta">
			<b-form-radio v-model="selected" name="some-radios" value="verdadero">Verdadero</b-form-radio>
			<b-form-radio v-model="selected" name="some-radios" value="falso">Falso</b-form-radio>
		</b-form-group>
		<div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
		<div class="mt-3" v-if="selected === respuesta">Esto es: <strong>Correcto!</strong></div>
		<div class="mt-3" v-else-if="selected != respuesta">Esto es: <strong>Incorrecto :-(</strong></div>
	</div>

</template>
