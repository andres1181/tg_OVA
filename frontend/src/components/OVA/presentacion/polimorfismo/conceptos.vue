<script>

	import { Hooper, Slide, Navigation as HooperNavigation, Pagination as HooperPagination } from 'hooper'
	import 'hooper/dist/hooper.css'

	export default {
		name: 'conceptos',
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
			<slide>
				<div class="slide_">
					<h2 class="titulo_">Conceptos previos</h2>
					<p> Los conceptos importantes de la programación orientada a objetos que debemos tener en cuenta en el polimorfismo son:
						<br>
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
					<h3 class="titulo_">1. Herencia</h3>
					<p>La herencia permite la transferencia de código desde una clase <span class="negrita_">Base</span> a una o más clases
						<span class="negrita_">Derivadas</span>. En C++ en una clase hija la herencia se declara mediante dos puntos <span class="negrita_">":"</span>,
						así:
					</p>
					<p>
						<span>class <span class="negrita_">NombreClaseDerivada </span> <span class="subrayar_ negrita_">:</span> <span class="subrayar_">public</span>					<span class="negrita_">NombreClaseBase </span>{ ... }</span>
					</p>
					<p>
						<span>Los dos puntos significan que la clase derivada podra utilizar todos los <span class="subrayar_">miembros</span>					de la clase base que sean publicos.</span>
					</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h4 class="titulo_">Ejemplo:</h4>
					<p>Supongamos que tenemos las clases <span class="negrita_">EstudiantePregrado</span> y <span class="negrita_">EstudianteMaestria</span>;
						estas clases tienen muchos atributos en común como <em>Edad, Código, Nombres y Apellidos</em>. La clases también pueden
						tener en común la función <span class="negrita_"> ObtenerPromedio() </span>.
						<br>
					</p>
					<div class="">
						<img src="" alt="">
						<img src="" alt="">
					</div>
					<p>Podríamos escribir en cada una de las clases estos atributos y métodos, pero eso sería costoso e innecesario</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h4 class="titulo_">Ejemplo:</h4>
					<p>En cambio, podríamos crear una clase base llamada <span class="negrita_">Estudiante</span>, la cual implemente todo lo
						que las clases <span class="negrita_">EstudiantePregrado</span> y <span class="negrita_">EstudianteMaestria</span>tienen
						en común. De esta forma evitamos repetir código innecesario.
					</p>
					<div class="">
						<img src="" alt="">
					</div>

				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h4 class="titulo_">Ejemplo:</h4>
					<p>En C++ la implementacion de la clase base quedaria parecida a esto:
					</p>
					<div class="">
						<img src="" alt="">
					</div>

				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h4 class="titulo_">Ejemplo:</h4>
					<p>Las clases derivadas <span class="negrita_">EstudiantePregrado</span> y <span class="negrita_">EstudianteMaestria</span>					quedarian así:
					</p>
					<div class="">
						<img src="" alt="">
						<img src="" alt="">
					</div>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Pregunta</h3>
					<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
						aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
						Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
						occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
					</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Funciones virtuales</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
					</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Constructores virtuales</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
					</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Destructores virtuales</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos. Sin embargo, antes de explicar en
						qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios
						para entender el funcionamiento de los diferentes tipos de polimorfismo.
						<br> Los conceptos que debemos tener en cuenta para comprender el polimorfismo son: <br>
					</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Clases abstractas</h3>
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
