<template>
  <v-container fluid class="image" :style="{ backgroundImage: 'url(' + article.image + ')' }">
    <v-layout class="black--text">
      <v-flex xs10 offset-xs1 sm8 offset-sm2>
        <v-card class="my-5">
          <v-card-title primary-title>
            <div class="card">
              <h3 class="headline mb-5">{{ article.title }}</h3>
              <div>{{ article.description }}</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn block color="primary ma-3" to="/blog">Все статьи</v-btn>
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
    title: 'Статьи | Шугаринг в Заполярном'
  },

  props: ['id'],

  computed: {
    ...mapGetters(['article'])
  },

  beforeMount () {
    this.$store.dispatch('getArticleId', this.id)
  }
}
</script>

<style scoped>
.image {
  min-height: 100%;
  background-size: cover;
}
</style>
