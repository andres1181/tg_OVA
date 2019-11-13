<script>

	import axios from 'axios'




	export default {
		name: 'Screen',

		data() {
			return {
				slide: 0,
				sliding: null
			}
		},

		methods: {
			onSlideStart(slide) {
				this.sliding = true
			},
			onSlideEnd(slide) {
				this.sliding = false
			}
			// getSlides() {
			// 	const path = 'http://localhost:8000/api_ova/1.0/Slide/'
			// 	axios
			// 		.get(path)
			// 		.then(response => {
			// 			this.slides = response.data
			// 		})
			// 		.catch(error => {
			// 			console.log(error)
			// 		})
			// }
		},
	}

</script>

<template >
	<div>
		<div>
		    <b-carousel
		      id="carousel-1"
		      v-model="slide"
		      :interval="0"
		      controls
		      indicators
		      background="#ababab"
		      img-width="1024"
		      img-height="480"
		      style="text-shadow: 1px 1px 2px #333;"
		      @sliding-start="onSlideStart"
		      @sliding-end="onSlideEnd"
		    >

		      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
		      <b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
		        <div class="">
							<h3>Polimorfismo</h3>
							<p>En su significado general, el polimorfismo se refiere a la cualidad que tiene algo de tomar múltiples formas o diferentes estados. El polimorfismo es un concepto utilizado en diferentes áreas, tales como la quimica, biologia, bioquimica, genetica e informática. <br>
							  Etimológicamente la palabra polimorfismo tiene origen en el griego: <br>
							  <span>Poli (Muchos)  + Morfo (Forma) +  Ismo( Actividad)</span>
							</p>
		        </div>
		      </b-carousel-slide>
					<b-carousel-slide caption="Blank Image" img-blank img-alt="Blank image">
						<div class="">
							<h3>Polimorfismo</h3>
							<p>En su significado general, el polimorfismo se refiere a la cualidad que tiene algo de tomar múltiples formas o diferentes estados. El polimorfismo es un concepto utilizado en diferentes áreas, tales como la quimica, biologia, bioquimica, genetica e informática. <br>
								Etimológicamente la palabra polimorfismo tiene origen en el griego: <br>
								<span>Poli (Muchos)  + Morfo (Forma) +  Ismo( Actividad)</span>
							</p>
						</div>
					</b-carousel-slide>
					<b-carousel-slide>
							<h3>Polimorfismo</h3>
							<p>En su significado general, el polimorfismo se refiere a la cualidad que tiene algo de tomar múltiples formas o diferentes estados. El polimorfismo es un concepto utilizado en diferentes áreas, tales como la quimica, biologia, bioquimica, genetica e informática. <br>
								Etimológicamente la palabra polimorfismo tiene origen en el griego: <br>
								<span>Poli (Muchos)  + Morfo (Forma) +  Ismo( Actividad)</span>
							</p>
					</b-carousel-slide>
		    </b-carousel>
		  </div>
    <br>
    <div class="" align="center">
      <button type="button" name="button" class="btn btn-dark rounded">Empezar Quiz</button>
			<button type="button" name="button">Hola</button>
    </div>
</div>

</template>

<style>
b-carousel-slide {
  color: #FF5733;
}
#caru {
}
#slide-caru{
  height: inherit;
  background:#FFFFFF;
}
</style>
