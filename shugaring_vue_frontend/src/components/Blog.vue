<template>
  <v-container grid-list-xl my-5>
    <v-layout row wrap>

      <v-flex 
        v-for="item in articles"
        :key="item.title"
        sm8 offset-sm2
        md6 offset-md0
      >
        <v-card>
          <v-img
            :src="item.image"
            aspect-ratio="2.5"
          ></v-img>
 
          <v-card-title primary-title>
            <h4 class="title mb-0">{{ item.title }}</h4>
          </v-card-title>

          <v-card-actions>
            <v-btn 
              flat 
              color="primary"
              :to="{ path: '/blog/', name: 'BlogArticle', params: { id: item.id }}"
            >
              Читать статью
            </v-btn>
          </v-card-actions>
          
        </v-card>
      </v-flex>

    </v-layout>
  </v-container>
</template>

<script>
import { mapGetters } from 'vuex'

export default {

  metaInfo: {
    title: 'Статьи о шугаринге | Шугаринг в Заполярном'
  },

  computed: {
    ...mapGetters(['articles'])
  },

  beforeMount () {
    this.$store.dispatch('getArticles')
  }
}
</script>

<style scoped>

</style>
