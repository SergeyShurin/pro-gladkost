<template>
  <v-container fluid>
    <v-layout class="black--text">
      <v-flex xs10 offset-xs1 sm8 offset-sm2>
        <v-card class="my-5">
          <v-img
            :src="good.image"
            aspect-ratio="1.5"
            contain
          ></v-img>
          <v-card-title primary-title>
            <div class="card">
              <h3 class="headline mb-5">{{ good.name }}</h3>
              <h3 class="title grey--text mb-3">{{ good.price }} руб</h3>
              <div>{{ good.description }}</div>
            </div>
          </v-card-title>
          <v-card-actions>
            <v-btn
              slot="activator"
              small
              block
              color="primary"
              :to="{ path: '/goods'}"
            >
              Все товары
            </v-btn>
            <v-btn
              small
              flat
              color="primary"
              @click.prevent="addToCart(good.id)"
            >
              В корзину
            </v-btn>
          </v-card-actions>

        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {

  metaInfo: {
    title: 'Товары | Шугаринг в Заполярном'
  },

  props: ['id'],

  computed: {
    ...mapGetters(['good'])
  },

  methods: {
    ...mapActions(['addToCart'])
  },

  beforeMount () {
    this.$store.dispatch('getGoodId', this.id)
  }
}
</script>

<style scoped>

</style>
