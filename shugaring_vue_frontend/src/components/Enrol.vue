<template>
  <v-container>
    <v-stepper v-model="e1">
      <v-stepper-header>
        <v-stepper-step :complete="e1 > 1" step="1">Заполнить форму</v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step :complete="e1 > 2" step="2">{{ title }}</v-stepper-step>

      </v-stepper-header>

      <v-stepper-items>

        <v-stepper-content step="1">
      
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

            <v-select
              :items="p"
              item-text="title"
              v-model="list"
              :rules="listRules"
              :menu-props="{ maxHeight: '200' }"
              label="Выберите процедуры"
              multiple
              chips
            ></v-select>

            <v-textarea
              v-model="comment"
              label="Ваш комментарий (необязательное поле)"
              required
            ></v-textarea>

          </v-form>

          <v-btn
            :disabled="!valid"
            color="primary"
            @click="submit"
          >
            Записаться
          </v-btn>

        </v-stepper-content>

        <v-stepper-content step="2">
          
          <h2 class="headline my-5 text-xs-center">{{ h2top }} <br> {{ h2bottom }}</h2>

          <v-btn
            color="primary"
            :to="{ path: '/goods'}"
          >
            Каталог товаров
          </v-btn>

          <v-btn
            color="primary"
            href="https://vk.com/topic-65101820_30760692?offset=60"
          >
            Посмотреть отзывы
          </v-btn>

        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-container>

</template>


<script>

import { mapGetters } from 'vuex'
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
    list: [],
    listRules: [
      v => !!v || 'Выберете процедуры',
      v => v.length !== 0 || 'Поле должно содержать хотя бы один параметр'
    ],
    comment: '',
    title: 'Готово',
    h2top: 'Запись прошла успешно',
    h2bottom: 'Мастер свяжется с вами в ближайшее время.'
  }),

  methods: {

    submit () {
      if (this.$refs.form.validate()) {
        var enrolData = {
          'name': this.name,
          'surname': this.surname,
          'phone': this.phone,
          'list_procedures': this.list_procedures(this.p),
          'wish_comment': this.add_comment(),
          'list': this.list
        }
        this.name = ''
        this.surname = ''
        this.phone = ''
        this.list = []
        this.comment = ''
        HTTP.post('/enrol/', enrolData)
        .catch(e => {
          this.title = 'Ошибка'
          this.h2top = 'Произошла ошибка'
          this.h2bottom = 'Повторите попытку позже или запишитесь по телефону +7(953)-154-54-54'
        })
        this.e1 = 2
      }
    },
    add_comment () {
      if (this.comment === '') {
        return 'Пользователь не оставил комментарий'
      } else {
        return this.comment
      }
    },
    list_procedures (array) {
      var mapList = this.list.map(function (item) {
        array.forEach(function (itemArray, array) {
          if (itemArray['title'] === item) {
            item = itemArray['id']
          }
        })
        return String(item)
      })
      return mapList
    }
  },

  computed: {
    ...mapGetters({
      products: 'cartProducts',
      products_added: 'cartProductsAdded',
      p: 'price'
    }),

    total () {
      return this.products.reduce((total, p) => {
        return total + p.price * p.quantity
      }, 0)
    }
  },

  beforeMount () {
    this.$store.dispatch('getPrice', this.id)
  }
}
</script>

<style scoped>

</style>
