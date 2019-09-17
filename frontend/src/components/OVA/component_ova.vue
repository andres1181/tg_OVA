<script>



</script>

<template>
<div>


	<!-- <div id="uno">
		<MenuPrin>This is a small message!</MenuPrin>
		<MenuPrin>Another one</MenuPrin>
	</div> -->
	<div id="nave">
		<bar-nave></bar-nave>
	</div>
	<div class="row">
		<div id="app" class="col-md-3 ui grid">
			<div class="four wide column">
				<div class="ui fluid inverted vertical menu">
					<h4 class="ui teal icon header center aligned">
						<i class="instagram icon"></i>
						<div class="content">
							Insta tags
						</div>
					</h4>
					<div role="tablist">
						<b-card no-body class="mb-1">
							<b-card-header header-tag="header" class="p-1" role="tab">
								<b-button block href="#" v-b-toggle.accordion-1 variant="info">Introducción</b-button>
							</b-card-header>
							<b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
								<b-card-body>
									<b-card-text>I start opened because <code>visible</code> is <code>true</code></b-card-text>
									<b-card-text>AAAA</b-card-text>
								</b-card-body>
							</b-collapse>
						</b-card>

						<b-card no-body class="mb-1">
							<b-card-header header-tag="header" class="p-1" role="tab">
								<b-button block href="#" v-b-toggle.accordion-2 variant="info">Actividades</b-button>
							</b-card-header>
							<b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
								<b-card-body>
									<b-card-text>AAAAAAAA</b-card-text>
								</b-card-body>
							</b-collapse>
						</b-card>

						<b-card no-body class="mb-1">
							<b-card-header header-tag="header" class="p-1" role="tab">
								<b-button block href="#" v-b-toggle.accordion-3 variant="info">Evaluación</b-button>
							</b-card-header>
							<b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
								<b-card-body>
									<b-card-text>aaaaa</b-card-text>
								</b-card-body>
							</b-collapse>
						</b-card>
						<b-card no-body class="mb-1">
							<b-card-header header-tag="header" class="p-1" role="tab">
								<b-button block href="#" v-b-toggle.accordion-3 variant="info">Resumen</b-button>
							</b-card-header>
							<b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
								<b-card-body>
									<b-card-text>Resumen</b-card-text>
								</b-card-body>
							</b-collapse>
						</b-card>
					</div>
				</div>
			</div>
		</div>
		<div class="container col-md-9">
			<h2>sgesdhsryjsryj</h2>
		</div>
	</div>
</div>
</template>

<style >

	.vertical.menu {
		height: 100vh;
		padding-top: 20px;
	}

	#content {
		padding-top: 20px;
	}

</style>
