<script>

	import { Hooper, Slide, Navigation as HooperNavigation, Pagination as HooperPagination } from 'hooper'
	import 'hooper/dist/hooper.css'

	import conceptos from '@/components/ova/presentacion/polimorfismo/conceptos.vue'

	export default {
		name: 'introduccion',
		components: {
			Hooper,
			Slide,
			conceptos,
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
					<h3 class="titulo_">Introducción</h3>
					<p>Uno de los elementos más importantes de la programación orientada a objetos es el polimorfismo y aunque en un principio
						este puede ser parecer complicado de entender, no es tan complicado.
						<br> Esta unidad tiene como objetivos: <br>
						<ol>

							<li value="1">Comprender el concepto de polimorfismo y su uso en la construcción de algoritmos.</li>
							<li>Conocer las caracteristicas, usos y diferencias los tipos de polimorfismo utilizados en C++. </li>
							<li>Comprender el funcionamiento del polimorfismo en la implementación de algoritmos en el lenguaje de programación C++. </li>

						</ol>
					</p>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">¿Qué es el Polimorfismo?</h3>
					<p>En su significado general, el polimorfismo se refiere a la cualidad que tiene algo de tomar múltiples formas o diferentes
						estados. El polimorfismo es un concepto utilizado en diferentes áreas, tales como la quimica, biologia, bioquimica,
						genetica e informática. <br> Etimológicamente la palabra polimorfismo tiene origen en el griego: <br>
						<span class="negrita_">Poli (Muchos)  + Morfo (Forma) +  Ismo( Actividad)</span>
					</p>
				</div>
			</slide>
			<slide  id="Conceptos">
				<div class="slide_">
					<h3 class="titulo_">¿Qué es el Polimorfismo?</h3>
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos.
						Sin embargo, antes de explicar en qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios para entender el funcionamiento de los diferentes tipos de polimorfismo.
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
					<p>En esta unidad estudiaremos el polimorfismo en la Programación Orientada a Objetos.
						Sin embargo, antes de explicar en qué consiste cada tipo de polimorfismo, en la sección 'Conceptos Previos', daremos un repaso a algunos conceptos necesarios para entender el funcionamiento de los diferentes tipos de polimorfismo.
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
