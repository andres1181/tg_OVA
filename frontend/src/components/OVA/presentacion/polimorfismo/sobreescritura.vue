<script>

	import { Hooper, Slide, Navigation as HooperNavigation, Pagination as HooperPagination } from 'hooper'
	import 'hooper/dist/hooper.css'

	export default {
		name: 'sobreescritura',
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
					<h3 class="titulo_">Sobreescritura</h3>
					<p>La sobreescritura es otro de los tipos de polimorfismo en la programación orientada a objetos y puede ser aplicada dentro
						de una <em id="jdc">jerarquia de clases</em>. Para que haya sobrecarga se debe cumplir que:
					</p>
					<p>Para sobrecargar un método:</p>
					<ol>
						<li value="1">Definir un método en la clase Base.</li>
						<li>Definir un método con el mismo nombre y tipo en la clase derivada. </li>
						<li>Los parametros que reibe el método deben ser del mismo tipo en la clase Base y en la clase Derivada</li>
						<li>El comportamiento interno del método debe ser diferente en la clase derivada</li>
					</ol>
				</div>
				<b-tooltip target="jdc" triggers="hover">
					¡Cuando utilizas <b>Herencia</b>!
				</b-tooltip>
			</slide>
			<slide>
				<div class="slide_">
					<h4 class="titulo_">Ejemplo:</h4>
					<p>Supongamos que tenemos una clase base llamada <span class="negrita_">Persona</span> y dos clases derivadas llamadas
						<span class="negrita_">Estudiante</span> y <span class="negrita_">Docente</span>; queremos mostrar los datos personales
						del <span class="negrita_" id="est">Estudiante</span> y el <span class="negrita_" id="doc">Docente</span>, pero estos
						se diferencian en algunas cosas.
					</p>
					<div class="">
						<img src="" alt="">
						<img src="" alt="">
						<img src="" alt="">
					</div>
					<p>En la clase base <span class="negrita_">Persona</span> definiremos un metodo llamado <span class="negrita_">imprimirDatos()</span>,
						el cual vamos a sobreescribir en las clases <span class="negrita_">Estudiante</span> y <span class="negrita_">Docente</span>.</p>
				</div>
				<b-tooltip target="est" triggers="hover">
					<p>Los datos de <b>Estudiante</b> son: Nombres, Apellidos, Código, Correo, Edad, Promedio y Semestre</p>
				</b-tooltip>
				<b-tooltip target="doc" triggers="hover">
					<p>Los datos de <b>Docente</b> son: Nombres, Apellidos, Código, Correo, Salario y Experiencia</p>
				</b-tooltip>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Ejemplo de sobreescritura:</h3>
					<p>El metodo <span class="negrita_">imprimirDatos()</span> en la clase base <span class="negrita_">Persona</span> solo retorna
						un mensaje.
						<div class="">
							<img src="" alt="">
						</div>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Ejemplo de sobreescritura:</h3>
					<p>El metodo <span class="negrita_">imprimirDatos()</span> en la clase <span class="negrita_">Estudiante</span> retorna
						los datos del estudiante.
						<div class="">
							<img src="" alt="">
						</div>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Ejemplo de sobreescritura:</h3>
					<p>El metodo <span class="negrita_">imprimirDatos()</span> en la clase <span class="negrita_">Docente</span> retorna
						los datos del docente.
						<div class="">
							<img src="" alt="">
						</div>
				</div>
			</slide>
			<slide>
				<div class="slide_">
					<h3 class="titulo_">Pregunta</h3>
					<p>Hasta ahora el planteamiento es correcto, pero si una persona ingresa un tipo de dato númerico que no sea entero, se presentaria un
						error. Para solucionar esto podemos recurrir a la sobrecarga de la función <em>volumen</em> por cada tipo de dato, asi:
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
