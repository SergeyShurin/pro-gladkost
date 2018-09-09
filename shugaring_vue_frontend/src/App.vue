<template>
  <v-app class="mt-5">
    <v-toolbar fixed>
      <v-toolbar-side-icon 
        class="hidden-md-and-up"
        @click="drawer = !drawer"
      >
      </v-toolbar-side-icon>
      <v-toolbar-title>
        <span class="primary--text">PRO</span>ГЛАДКОСТЬ
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn 
          v-for="item in items"
          flat
          :key="item.title"
          :to="{path: item.to}"
        >
          {{ item.title }}
        </v-btn>
      </v-toolbar-items>
      <v-toolbar-items class="hidden-sm-and-down">
        <v-btn
          flat
          href="https://vk.com/topic-65101820_30760692?offset=60"
          target="blank"
        >
          Отзывы
        </v-btn>
      </v-toolbar-items>
    </v-toolbar>

    <v-content>
      <transition name="fade">
        <router-view/>
      </transition>
    </v-content>

    <v-navigation-drawer
      v-model="drawer"
      absolute
      disable-resize-watcher
    >
      <v-toolbar flat>
        <v-list>
          <v-list-tile>
            <v-list-tile-title class="title">
              <span class="primary--text">PRO</span>ГЛАДКОСТЬ
            </v-list-tile-title>
          </v-list-tile>
        </v-list>
      </v-toolbar>

      <v-divider></v-divider>

      <v-list dense class="pt-0">
        <v-list-tile
          v-for="item in items"
          :key="item.title"
          :to="{path: item.to}"
        >
          <v-list-tile-action>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

        <v-list-tile
          href="https://vk.com/topic-65101820_30760692?offset=60"
          target="blank"
        >
          <v-list-tile-action>
            <v-icon>rate_review</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Отзывы</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>

      </v-list>
    </v-navigation-drawer>

    <footer>
      <v-container
        grid-list-xl
        fluid
        class="secondary"
      >
        <v-layout
          row
          wrap
          justify-center
        >
          <v-flex xs12 sm4>
            <v-card class="elevation-0 transparent primary--text">
              <v-card-title primary-title class="layout justify-center">
                <div class="headline">Follow us</div>
              </v-card-title>
              <v-card-text class="pa-0 ma-0">
                <p class="text-xs-center ma-0">Подпишись и следи за новостями.</p>
              </v-card-text>
              <v-card-text>
                <p class="text-xs-center ma-0">
                  <v-btn 
                    flat
                    icon
                    href="https://vk.com/sugaring51.olga"
                    target="blank"
                  >
                    <v-icon class="primary--text">$vuetify.icons.vk</v-icon>
                  </v-btn>
                  <v-btn 
                    flat
                    icon
                    href="https://vk.com/sugaring51.olga"
                    target="blank"
                  >
                    <v-icon class="primary--text">$vuetify.icons.inst</v-icon>
                  </v-btn>
                </p>
              </v-card-text>
            </v-card>
          </v-flex>
          <v-flex xs12 sm4 offset-sm1>
            <v-card class="elevation-0 transparent primary--text">
              <v-card-title primary-title class="layout justify-center">
                <div class="headline">Contact us</div>
              </v-card-title>
              <v-list class="transparent">
                <v-list-tile>
                  <v-list-tile-action>
                    <v-icon class="primary--text">phone</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title class="primary--text">+7(953)-154-54-54</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
                <v-list-tile>
                  <v-list-tile-action>
                    <v-icon class="primary--text">place</v-icon>
                  </v-list-tile-action>
                  <v-list-tile-content>
                    <v-list-tile-title class="primary--text">Юбилейная 6, Заполярный</v-list-tile-title>
                  </v-list-tile-content>
                </v-list-tile>
              </v-list>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
      
    </footer>

    <transition name="cart">
      <v-btn
        v-if='show'
        class="cart"
        large
        fab
        bottom
        right
        fixed
        color="primary"
        :to="{ path: '/cart'}"
      >
        <v-icon>shopping_cart</v-icon>
      </v-btn>
    </transition>

  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: false,
      items: [
        { to: '/', title: 'Главная', icon: 'home' },
        { to: '/about', title: 'О Нас', icon: 'account_circle' },
        { to: '/blog', title: 'Полезно знать', icon: 'library_books' },
        { to: '/price', title: 'Услуги', icon: 'group' },
        { to: '/shares', title: 'Акции', icon: 'monetization_on' },
        { to: '/enrol', title: 'Запись', icon: 'list_alt' },
        { to: '/goods', title: 'Товары', icon: 'shopping_cart' },
        { to: '/cart', title: 'Корзина', icon: 'add_shopping_cart' }
      ]
    }
  },

  computed: {
    itemsInCart () {
      let cart = this.$store.getters.cartProducts
      return cart.reduce((accum, item) => accum + item.quantity, 0)
    },
    show () {
      if (this.itemsInCart === 0) {
        return false
      } else {
        return true
      }
    }
  }
}
</script>

<style scoped>
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

.cart-enter-active, .cart-leave-active {
  transition-property: all;
  transition-duration: .5s;
}

.cart-enter, .cart-leave-active {
  opacity: 0;
  transform: scale(0);
}

</style>