<script>

export default {
  name: 'Slide',
  props: {
    contenido: {
      type: String,
      default: '' // whatever you want as default
    }
  }
}
</script>

<template>

	<div id="contenido-L" class="">
		<span>{{contenido}}</span>
	</div>

</template>

<style>

</style>
