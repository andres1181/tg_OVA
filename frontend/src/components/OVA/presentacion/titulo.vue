<script>

</script>

<template>
<div class="">
  <div v-if="type === 'grande'">
    <h3>{{titulo}}</h3>
  </div>
  <div v-else-if="type === 'mediano'">
    <h2>{{titulo}}</h2>
  </div>
  <div v-else-if="type === 'pequeño'">
    <h1>{{titulo}}</h1>
  </div>
</div>


</template>

<style>

</style>
