<script>
import axios from 'axios'
export default {
  name: 'introduccion',
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
  }

  }

</script>

<template>
<div class="" id="caru">
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
        @sliding-end="onSlideEnd" >
    <!-- Text slides with image -->
    <!-- <div id="slide-1" v-for="sl in slides" :key="sl.id"> -->

    <!--  <b-carousel-slide id="slide-caru"v-for="sl in slides" :key="sl.id" :caption="sl.contenido" :img-src="sl.imagen"> -->
        <b-carousel-slide class="slide-caru">
        <div class="">
        <h3>Polimorfismo</h3>
        <p>En su significado general, el polimorfismo se refiere a la cualidad que tiene algo de tomar múltiples formas o diferentes estados. El polimorfismo es un concepto utilizado en diferentes áreas, tales como la quimica, biologia, bioquimica, genetica e informática. <br>
          Etimológicamente la palabra polimorfismo tiene origen en el griego: <br>
          <span>Poli (Muchos)  + Morfo (Forma) +  Ismo( Actividad)</span>
        </p>
        </div>
      </b-carousel-slide>
    <!-- </div> -->


  </b-carousel>
  <button type="button" name="button"></button>
</div>


</template>

<style>
.slide-caru{
  height: inherit;
  background:#FFFFFF;
}
</style>
