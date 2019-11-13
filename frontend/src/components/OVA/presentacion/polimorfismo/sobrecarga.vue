<script>

	import { Hooper, Slide, Navigation as HooperNavigation, Pagination as HooperPagination } from 'hooper'
	import 'hooper/dist/hooper.css'

	export default {
		name: 'sobrecarga',
		components: {
			Hooper,
			Slide,
			HooperNavigation,
			HooperPagination
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
					<h3 class="titulo_">Ejemplo</h3>
					<p>Hasta hora el planteamiento es correcto, pero si una persona ingresa un tipo de dato numero que no sea entero, se presentaria un
						error. Para solucionar este error podemos recurrir a la sobrecarga de la función <em>volumen</em> por cada tipo de dato, asi:
					</p>
					<div class="">
						<img src="" alt="">
						<img src="" alt="">
					</div>
					<p>De esta forma se ejecutara la función que corresponda al tipo de dato ingresado por el ususario.</p>
				</div>
			</slide>
			<slide id="Conceptos">
				<div class="slide_">
					<h3 class="titulo_">¿Qué es el Polimorfismo?</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
					</p>
					<ol>
						<li value="1"> Herencia</li>
						<li>Funciones virtuales</li>
						<li>Constructores virtuales</li>
						<li>Destructores virtuales</li>
						<li>Clases abstractas</li>
					</ol>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Herencia</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
					</p>
					<b-button block href="#" v-on:click="componenteActual = 'introduccion'" variant="info">Introducción</b-button>
				</div>
			</slide>
			<slide id="Sobrecarga">
				<div class="slide_">
					<h3 class="titulo_">Sobrecarga</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
					</p>
				</div>
			</slide>
			<slide id="Sobreescritura">
				<div class="slide_">
					<h3 class="titulo_">Sobreescritura</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
					</p>
				</div>
			</slide>
			<slide id="Polimorficas">
				<div class="slide_">
					<h3 class="titulo_">Variables Polimorficas</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
					</p>
				</div>
			</slide>
			<slide id="Genericidad">
				<div class="slide_">
					<h3 class="titulo_">Genericidad</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
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
