<template>
  <v-container>
    <v-stepper v-model="e1">
      <v-stepper-header>
        <v-stepper-step :complete="e1 > 1" step="1">Подтвердить заказ</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="e1 > 2" step="2">Заполнить форму</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">{{ title }}</v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1" class="cart">

          <template v-if="products.length>0">
            <table v-show="products.length">
              <thead>
                <tr>
                  <td>Название</td>
                  <td></td>
                  <td>Цена</td>
                  <td></td>
                </tr>
              </thead>
              <tbody>
                <tr v-for="good in products">
                  <td id='name'>{{ good.name }}</td>
                  <td id='quantity'>x {{ good.quantity }}</td>
                  <td id='price'>{{ good.price }} р</td>
                  <td>
                    <v-btn icon small color="primary" @click.prevent="addToCart(good.id)">
                     <v-icon>add</v-icon>
                    </v-btn>
                    <v-btn icon small color="primary" @click.prevent="removeFromCart(good.id)">
                     <v-icon>remove</v-icon>
                    </v-btn>
                  </td>
                </tr>
                <tr>
                  <td><b>Всего:</b></td>
                  <td></td>
                  <td><b>{{ total }} р</b></td>
                  <td></td>
                </tr>
              </tbody>
            </table>

          <v-btn
            color="primary"
            @click="e1 = 2"
          >
            Продолжить
          </v-btn> 
        </template>
        <template v-else>
          <p class="text-xs-center">В корзине нет товаров</p>
          <v-btn
            color="primary"
            :to="{ path: '/goods'}"
          >
            К списку товаров
          </v-btn> 
        </template>

        </v-stepper-content>

        <v-stepper-content step="2">
      
          <v-form ref="form" v-model="valid" lazy-validation>
            <v-text-field
              v-model="name"
              :rules="nameRules"
              :counter="10"
              label="Имя"
              required
              hint="Имя должно содержать не более 10 символов"
            ></v-text-field>
            <v-text-field
              v-model="surname"
              :rules="surnameRules"
              :counter="10"
              label="Фамилия"
              required
              hint="Фамилия должно содержать не более 10 символов"
            ></v-text-field>
            <v-text-field
              v-model="phone"
              :rules="phoneRules"
              label="Телефон"
              required
              hint="Например +7(123)456-78-90"
              :mask="mask"
            ></v-text-field>
          </v-form>

          <v-btn
            :disabled="!valid"
            color="primary"
            @click="submit"
          >
            Продолжить
          </v-btn>

          <v-btn
            flat
            @click="e1 = 1"
          >
            Назад
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          
          <h2 class="headline my-5 text-xs-center">{{ h2top }} <br> {{ h2bottom }} </h2>

          <v-btn
            color="primary"
            :to="{ path: '/goods'}"
          >
            Вернуться к списку товаров
          </v-btn>

          <v-btn
            color="primary"
            :to="{ path: '/enrol'}"
          >
            Записаться к мастеру
          </v-btn>

        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-container>

</template>


<script>

import { mapActions, mapGetters } from 'vuex'
import { HTTP } from '../api/common.js'

export default {

  metaInfo: {
    title: 'Корзина | Шугаринг в Заполярном'
  },

  data: () => ({
    e1: 0,
    valid: false,
    name: '',
    nameRules: [
      v => !!v || 'Введите имя',
      v => v.length <= 10 || 'Имя должно содержать не более 10 символов'
    ],
    surname: '',
    surnameRules: [
      v => !!v || 'Введите фамилию',
      v => v.length <= 10 || 'Фамилия должна содержать не более 10 символов'
    ],
    phone: '',
    phoneRules: [
      v => !!v || 'Введите телефон',
      v => v.length === 11 || 'Например +7(123)456-78-90'
    ],
    mask: '+7(###) ### - ## - ##',
    title: 'Готово',
    h2top: 'Запись прошла успешно',
    h2bottom: 'Мастер свяжется с вами в ближайшее время.'
  }),

  methods: {
    ...mapActions(['addToCart', 'removeFromCart', 'postOrder', 'cleanAllCart']),

    submit () {
      if (this.$refs.form.validate()) {
        var orderData = {
          'customer_name': this.name,
          'customer_surname': this.surname,
          'phone': this.phone
        }
        orderData.order_item = this.products_added
        this.name = ''
        this.surname = ''
        this.phone = ''
        this.cleanAllCart()
        HTTP.post('/orders/', orderData)
        .catch(e => {
          this.title = 'Ошибка'
          this.h2top = 'Произошла ошибка'
          this.h2bottom = 'Повторите попытку позже или сделайте заказ по телефону +7(953)-154-54-54'
        })
        this.e1 = 3
      }
    }
  },

  computed: {
    ...mapGetters({
      products: 'cartProducts',
      products_added: 'cartProductsAdded'
    }),

    total () {
      return this.products.reduce((total, p) => {
        return total + p.price * p.quantity
      }, 0)
    }
  }
}
</script>



<style>

.cart {
  display: flex;
  justify-content: center;
}

.cart table{
  max-width: 1000px;
  width: 100%;
  margin-bottom: 25px;
}

.cart td {
  text-align: center;
}

.cart #quantity {
  padding: 0 10px 0 10px;
}

.cart thead {
  font-size: 1.1em;
  font-weight: bold;
}

.cart tbody td:nth-child(1) {
  text-align: left;
}

.cart tbody tr:last-child {
  font-size: 1.2em;
}

.form_cart {
  display: flex;
  justify-content: center;
}

.form_cart div {
  width: 1000px;
}

</style>