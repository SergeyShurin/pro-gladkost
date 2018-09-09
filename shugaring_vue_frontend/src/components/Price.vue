<template>
  <v-container class="prices">
    <v-layout column wrap>
      <div class="mt-5">
        <v-btn
          color="blue lighten-2"
          @click="for_man = true; for_woman = false"
        >
          Мужской
        </v-btn>
        <v-btn
          color="pink lighten-3"
          @click="for_woman = true; for_man = false"
        >
          Женский
        </v-btn>
      </div>

      <table>

        <thead>
         <tr>
            <td></td>
            <td></td>
            <td></td>
            <td id='man'>
              .
            </td>
            <td id='woman'>
              .
            </td>
          </tr>
        </thead>

        <transition name="fade">

          <template v-if="for_woman">
            <transition name="fade">
              <tbody>
                <tr v-for="item in price" v-if="item.price_woman">
                  <td valign="top" id='title'>{{ item.title }}
                  </td>
                  <td valign="top">
                    <div id="color" class="color pink lighten-3"></div>
                  </td>
                  <td valign="top">
                    <div class="circle pink lighten-3"></div>
                  </td>
                  <td valign="top" id='woman'>{{ item.price_woman }} руб.<br>
                    <span>{{ item.time }} мин.</span>
                  </td>
                </tr>
              </tbody>
            </transition>
          </template>

          <template v-else>
            <tbody>
              <tr v-for="item in price" v-if="item.price_man">
                <td valign="top" id='title'>{{ item.title }}
                </td>
                <td valign="top">
                  <div id="color" class="color blue lighten-2"></div>
                </td>
                <td valign="top">
                  <div class="circle blue lighten-2"></div>
                </td>
                <td valign="top" id='man'>{{ item.price_man }} руб.<br>
                  <span>{{ item.time }} мин.</span>
                </td>
              </tr>
            </tbody>
          </template>

        </transition>

      </table>

    </v-layout>
  </v-container>
</template>

<script>

import { mapGetters } from 'vuex'

export default {

  data: () => ({
    for_man: false,
    for_woman: true
  }),

  metaInfo: {
    title: 'Услуги | Шугаринг в Заполярном'
  },

  computed: {
    ...mapGetters(['price'])
  },

  beforeMount () {
    this.$store.dispatch('getPrice', this.id)
  }
}
</script>

<style scoped>

.prices td {
  height: 100px;
}

.prices td span {
  color: grey;
  font-size: 0.8em;
}

.prices thead #man,
.prices thead #woman {
  color: transparent;
}

.prices td:nth-child(1) {
  text-align: right;
  padding-right: 30px;
  width: 50%;
}

.prices td:nth-child(2) {
  margin: 0;
  padding: 0;
  position: relative;
}

.prices td:nth-child(3) {
  margin: 0;
  padding: 0;
  position: relative;
}

.prices td:nth-child(4) {
  margin: 0;
  padding-left: 30px;
  width: 50%;
}

.prices {
  display: flex;
  text-align: center;
}

.prices .circle {
  position: absolute;
  top: -5px;
  right: -11px;
  width: 0;
  height: 0;
  padding: 10px;
  margin: 0px;
  border-radius: 20px;
}

.prices .color {
  position: absolute;
  width: 5px;
  height: 100%;
}

.prices tbody tr:last-child td .color {
  height: 0;
}

.prices #man {
  text-align: left;
}

.prices #woman {
  text-align: left;
}

.fade-enter-active, .fade-leave-active {
  transition-property: opacity;
  transition-duration: .25s;
}

.fade-enter-active {
  transition-delay: .25s;
}

.fade-enter, .fade-leave-active {
  opacity: 0
}

</style>
