<script>

	import axios from 'axios'
	export default {
    data() {
      return {
        codigoFuente: '',
        salidaEsperada: '',
        codLenguaje: ''
      }
    },
		methods: {
			postSub(e) {
        e.preventDefault();
				axios({
					method: 'POST',
					url: 'https://api.judge0.com/submissions/?base64_encoded=false&wait=false',
					headers: {
						'content-type': 'application/json',
						'x-rapidapi-host': 'judge0.p.rapidapi.com',
						'x-rapidapi-key': 'cd7a56d70dmsh276272def56419ep1313e3jsn52fbad167a86',
						accept: 'application/json'
					},
					datos: {
						source_code: this.codigoFuente,
						language_id: this.codLenguaje,
            expected_output: this.salidaEsperada,
					}
				})
					.then(response => {
						let descripcion = datos.status.description

					})
					.catch(error => {
						console.log(error)
					})
			},

			getSub() {
				const axios = require('axios')

				axios({
					method: 'GET',
					url: 'https://judge0.p.rapidapi.com/submissions/7a44be92-1923-47ea-800d-2c5e51465949',
					headers: {
						'content-type': 'application/octet-stream',
						'x-rapidapi-host': 'judge0.p.rapidapi.com',
						'x-rapidapi-key': 'cd7a56d70dmsh276272def56419ep1313e3jsn52fbad167a86'
					}
				})
					.then(response => {
						console.log(response)
					})
					.catch(error => {
						console.log(error)
					})
			}
		}
	}

</script>

<template>

	<div class="">

	</div>

</template>

<style>

</style>
