<script>

	import { Hooper, Slide, Navigation as HooperNavigation, Pagination as HooperPagination } from 'hooper'
	import 'hooper/dist/hooper.css'

	import OpcionMultiple from '@/components/preguntas/opcionMultiple.vue'
	import falsoVerdadero from '@/components/preguntas/falsoYverdadero.vue'

	export default {
		name: 'sobrecarga',
		components: {
			Hooper,
			Slide,
			HooperNavigation,
			HooperPagination,
			OpcionMultiple,
			falsoVerdadero
		}
	}

</script>

<template>

	<div class="">
		<hooper style="height: 480px">
			<slide id="Introduccion">
				<div class="slide_">
					<h3 class="titulo_">Sobrecarga</h3>
					<p>Es una característica de la programación orientada a objetos y puede ser aplicada a constructores o métodos. Para que
						haya sobrecarga se debe cumplir que:
					</p>
					<ol>
						<li value="1">Dos o más funciones pueden compartir un nombre.</li>
						<li>En la declaración los tipos de parámetros sean diferentes.</li>
					</ol>
					<p>Veamos un ejemplo de sobrecarga de funciones:
						<br> Supongamos que queremos construir una función que permita conocer el volumen de un cubo. Dicha función recibiria
						el valor de una de las aristas de tipo entero y esta se multiplicaria tres veces.
					</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Ejemplo sobrecarga de funciones:</h3>
					<p>Hasta hora el planteamiento es correcto, pero si una persona ingresa un tipo de dato numero que no sea entero, se presentaria
						un error. Para solucionar este error podemos recurrir a la sobrecarga de la función <em>volumen</em> por cada tipo de
						dato, asi:
					</p>
					<div class="">
						<img src="" alt="">
						<img src="" alt="">
					</div>
					<p>De esta forma se ejecutara la función que corresponda al tipo de dato ingresado por el ususario.</p>
				</div>
			</slide>
			<slide>
				<iframe height="400px"
				        width="100%"
				        src="https://repl.it/repls/EuphoricSunnyExtraction?lite=true"
				        scrolling="no"
				        frameborder="no"
				        allowtransparency="true"
				        allowfullscreen="true"
				        sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Pregunta</h3>
					<div class="">
						<!-- Se elige aleatoriamente una pregunta de cualquier tipo-->

					</div>
					<OpcionMultiple :pregunta="'Se requiere de un programa que calcule el área de una figura geométrica puede se de dos o tres dimensiones. ¿Cual de los siguientes fragmentos de código debería utilizarse para que haya Sobrecarga?:'"

					                :opcion1="'Codigo 1'"
					                :opcion2="'Codigo 2'"
					                :opcion3="'Codigo 3'"
					                :opcionCorrecta="'Codigo 4'" />
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Pregunta</h3>
					<falsoVerdadero :pregunta="'Se requiere de un programa que calcule el área de una figura geométrica puede se de dos o tres dimensiones. ¿Cual de los siguientes fragmentos de código debería utilizarse para que haya Sobrecarga?:'"

					                :respuesta="'verdadero'" />
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Ejemplo sobrecarga de constructores:</h3>
					<p>Hasta hora el planteamiento es correcto, pero si una persona ingresa un tipo de dato numero que no sea entero, se presentaria
						un error. Para solucionar este error podemos recurrir a la sobrecarga de la función <em>volumen</em> por cada tipo de
						dato, asi:
					</p>
					<div class="">
						<img src="" alt="">
						<img src="" alt="">
					</div>
					<p>De esta forma se ejecutara la función que corresponda al tipo de dato ingresado por el ususario.</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Pregunta</h3>
					<p>Hasta hora el planteamiento es correcto, pero si una persona ingresa un tipo de dato numero que no sea entero, se presentaria
						un error. Para solucionar este error podemos recurrir a la sobrecarga de la función <em>volumen</em> por cada tipo de
						dato, asi:
					</p>
				</div>
			</slide>

			<hooper-pagination slot="hooper-addons" style="color: #666"></hooper-pagination>
			<hooper-navigation slot="hooper-addons" style="background-color: #666"></hooper-navigation>

		</hooper>

	</div>

</template>

<style>

	.example-slide {
		align-items: center;
		background-color: #666;
		color: #999;
		display: flex;
		font-size: 1.5rem;
		justify-content: center;
		min-height: 10rem;
	}

</style>
