<script>

</script>

<template>
<div class="">
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

      <b-carousel-slide id="slide-caru"v-for="sl in slides" :key="sl.id" :caption="sl.contenido" :img-src="sl.imagen">
        <!-- Fallback content -->
      </b-carousel-slide>
    <!-- </div> -->


  </b-carousel>
</div>


</template>

<style>

</style>
