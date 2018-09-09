<template>
  <section>
    <v-parallax
      src="http://drasler.ru/wp-content/uploads/2018/03/%D0%9F%D1%80%D0%B8%D0%BA%D0%BE%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%B8-%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D0%BD%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9-%D1%81%D1%82%D0%BE%D0%BB-1366%D1%85768-%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-1.jpg"
    >
      <v-layout
        align-center
        column
        justify-center
        class="black--text"
      >
        <img 
            src="../assets/logo_green_white.png" 
            class="primary--text" 
            alt="PROГЛАДКОСТЬ" 
            width="300"
          >
        <v-btn
            class="primary mt-5"
            large
            to="/enrol"
          > 
          Записаться
          </v-btn>
      </v-layout>
    </v-parallax>

    <section>
        <v-layout
          column
          wrap
          class="my-5"
          align-center
        >
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap>
                <v-flex v-for="item in items" :key="item.title" xs12 sm6 md3>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="primary--text text--lighten-2">$vuetify.icons.{{ item.icon }}</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">{{ item.title }}</div>
                    </v-card-title>
                    <v-card-text>
                      {{ item.text }}
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
    </section>

    <v-carousel hide-delimiters>
      <v-carousel-item
        v-for="(item,i) in items_carousel"
        :key="i"
        :src="item.src"
        reverse-transition="fade_carousel"
        transition="fade_carousel"
      >
        <v-container fill-height>
          <v-layout
            align-center
            column
            justify-center
            text-xs-center
            fill-height
            class="white--text"
            height="700"
          >
            <h1 class="display-2 font-weight-thin mb-3">{{ item.title }}</h1>
            <h4 class="subheading text">{{ item.text }}</h4>
            <v-btn
              class="primary mt-5"
              large
              :to="{path: item.to}"
            > 
            {{ item.button }}
            </v-btn>
          </v-layout>
        </v-container>
      </v-carousel-item>
    </v-carousel>

    <section>
        <v-layout
          column
          wrap
          class="my-5"
          align-center
        >
          <v-flex xs12>
            <v-container grid-list-xl>
              <v-layout row wrap>
                <v-flex v-for="item in items2" :key="item.title" xs12 sm6 md3>
                  <v-card class="elevation-0 transparent">
                    <v-card-text class="text-xs-center">
                      <v-icon x-large class="primary--text text--lighten-2">$vuetify.icons.{{ item.icon }}</v-icon>
                    </v-card-text>
                    <v-card-title primary-title class="layout justify-center">
                      <div class="headline text-xs-center">{{ item.title }}</div>
                    </v-card-title>
                    <v-card-text>
                      {{ item.text }}
                    </v-card-text>
                  </v-card>
                </v-flex>
              </v-layout>
            </v-container>
          </v-flex>
        </v-layout>
    </section>

  </section>
</template>

<script>
export default {
  data () {
    return {
      items: [
        {
          text: 'Каждый наш гость - личность, и мы прикладываем все силы, чтобы Вы понимали, что мы работаем только для Вас.',
          title: 'Индивидуальный подход',
          icon: 'heart'
        },

        {
          text: 'Все мастера работают по единым стандартам, и Вы сразу замечаете разницу в обслуживании с другими салонами.',
          title: 'Качество',
          icon: 'thumbs'
        },

        {
          text: 'Каждое действие мастер сопровождает объяснением и Вы понимаете, почему это нужно делать именно так, а не иначе.',
          title: 'Информация',
          icon: 'info'
        },

        {
          text: 'Наши цены соответствуют результату , а "вкусные" дисконтные программы позволяют Вам получать скидки и подарки. И тем самым экономить, но не на качестве!',
          title: 'Стоимость',
          icon: 'rouble'
        }
      ],

      items2: [
        {
          text: 'Любите ли Вы гладкую кожу и чистую работу так, как любим её мы? Настолько гладкую, что ни единого предательского волоска. Настолько чистую, что ни одного пропущенного мастером участка. Профессионализм – это качество.',
          title: 'Эффективность',
          icon: 'chart'
        },

        {
          text: 'Вы поймёте это сразу, едва переступив порог нашей студии. Чистый кабинет, одноразовые материалы для каждого гостя - это только самая малость тех правил, которых мы придерживаемся.',
          title: 'Чистый шугаринг',
          icon: 'ok' },

        {
          text: 'Мы не работаем на поток. Главное - качество и сервис. Мастер всегда свеж, опрятен и приятен в общении. Кабинет сияет чистотой. Процедура будет выполнена правильно и качественно, без спешки, а Ваше настроение станет только лучше.',
          title: 'То что Вы искали',
          icon: 'search'
        },

        {
          text: 'Мы ценим то, что Вы выбрали нас, и всегда стремимся к максимально эффективному результату. Если Вам что то не понравилось скажите нам. Ваши отзывы и пожелания позволяют нам становиться лучше.',
          title: 'Взаимные отношения',
          icon: 'users'
        }
      ],

      items_carousel: [
        {
          src: 'https://oboi.ws/filters/lomo_17_12401_oboi_zelenyj_firewatch_1920x1080.jpg',
          title: 'Почему стоит выбрать Нас?',
          text: 'Вы доверяете нам потому, что мы делаем шугаринг правильно, чисто и безопасно.',
          button: 'О Нас',
          to: '/about'
        },
        {
          src: 'https://wallpaper.wiki/wp-content/uploads/2017/05/Full-HD-Grass-Wallpapers.jpg',
          title: 'Ваши преимущества у нас',
          text: 'Делаем красиво. Везде.',
          button: 'Прайс услуг',
          to: '/price'
        },
        {
          src: 'http://oboi-na.ru/files/2009/05/05/nature/travka.jpg',
          title: 'Гибкость',
          text: 'Время работы студии шугаринга с 10 до 22. Но в жизни бывают разные моменты. Для Вас мы готовы задержаться на столько времени, сколько понадобится чтобы сделать Вас счастливой.',
          button: 'Записаться',
          to: '/enrol'
        }
      ]
    }
  }
}
</script>

<style scoped>
.text {
  max-width: 500px;
}

.fade_carousel-enter-active, .fade_carousel-leave-active {
  transition-property: opacity;
  transition-duration: 1s;
}
.fade_carousel-enter, .fade_carousel-leave-active {
  opacity: 0
}
</style>
