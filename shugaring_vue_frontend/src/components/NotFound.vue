<template>

		<v-img :src="`http://www.rabstol.net/uploads/gallery/main/200/rabstol_net_forest_36.jpg`">
		  <v-layout
		    align-center
		    column
		    justify-center
		    text-xs-center
		    fill-height
		    class="white--text"
		    height="700"
		  >
		    <h1 class="display-2 font-weight-thin mb-3"> 404 Not Found </h1>
		    <h4 class="subheading text"> Страница, которую вы пытаетесь найти, не найдена. </h4>
		    <v-btn
		      class="primary mt-3"
		      :to="{path: '/'}"
		    > 
		     На главную 
		    </v-btn>
		  </v-layout>
	  </v-img>

</template>

<script>
export default {
  metaInfo: {
    title: 'Ошибка 404 | Шугаринг в Заполярном'
  }
}
</script>



<style>


</style>