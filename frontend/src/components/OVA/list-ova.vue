<script>

	import axios from 'axios'

	export default {
		data() {
			return {
				ovas: [],
				max: 100
			}
		},

		methods: {
			getovas() {
				const path = 'http://localhost:8000/api_ova/1.0/Objeto/'
				axios
					.get(path)
					.then(response => {
						this.ovas = response.data
					})
					.catch(error => {
						console.log(error)
					})
			}
		},

		created() {
			this.getovas()
		}
	}

</script>

<template lang="html">

	<div class="container">
		<div class="row">
			<div class="col text-left">
				<h2>Listado ovas</h2>
				<div class="col-md-12">
					<div class="row">
						<div class="col-md-4" v-for="ova in ovas">
							<b-card :title="ova.titulo"
							        img-src="https://picsum.photos/600/300/?image=25"
							        img-alt="Image"
							        img-top
							        tag="article"
							        style="max-width: 20rem;"
							        class="mb-2">
								<b-card-text>
									<b-progress :value="ova.avance" :max="max" show-progress class="mb-3"></b-progress>
								</b-card-text>
								<b-button href="/ovas/ova" variant="primary">Iniciar</b-button>
							</b-card>
						</div>
            <h1></h1>
					</div>
				</div>
			</div>
		</div>
	</div>

</template>

<style>

</style>
