<template>
  <v-container grid-list-xl my-5>
    <v-layout row wrap>
      
      <v-flex 
        v-for="item in goods" 
        :key="item.title" 
        xs8 offset-xs2
        sm6 offset-sm0
        md4 offset-md0
      >
        <v-card>
          <v-img
            :src="item.image"
            aspect-ratio="1.5"
            contain
          ></v-img>

          <v-card-title primary-title>
            <div>
              <h4 class="mb-0">{{ item.name }}</h4>
              <br>
              <span class="grey--text">{{ item.price }} руб.</span>
            </div>
          </v-card-title>

          <v-card-actions>

            <v-btn
              slot="activator"
              small
              block
              color="primary"
              :to="{ path: '/goods/', name: 'GoodsDetail', params: { id: item.id }}"
            >
              Подробнее
            </v-btn>
            <v-btn
              small
              flat 
              color="primary"
              @click.prevent="addToCart(item.id)"
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
    title: 'Каталог товаров | Шугаринг в Заполярном'
  },

  data: () => ({
    query: ''
  }),

  computed: {
    ...mapGetters(['goods']),

    computedList: function (good) {
      var vm = this
      return this.goods.filter(function (good) {
        return good.name.toLowerCase().indexOf(vm.query.toLowerCase()) !== -1
      })
    }
  },

  methods: {
    ...mapActions(['addToCart'])
  },

  beforeMount () {
    this.$store.dispatch('getGoods')
  }
}
</script>

<style scoped>

</style>
