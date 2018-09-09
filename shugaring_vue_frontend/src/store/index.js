import Vue from 'vue'
import Vuex from 'vuex'
import { Goods } from '../api/goods'
import { Articles } from '../api/articles'
import { Discounts } from '../api/discounts'
import { Price } from '../api/price'
import * as types from './mutation-types'
Vue.use(Vuex)
const debug = process.env.NODE_ENV !== 'production'

const state = {
  allGoods: [],
  allArticles: [],
  allDiscount: [],
  allPrice: [],
  added: [],
  good: [],
  article: [],
  discount: []
}

const getters = {
  goods: state => state.allGoods,
  articles: state => state.allArticles,
  discounts: state => state.allDiscount,
  price: state => state.allPrice,
  cartProducts: state => {
    return state.added.map(({ id, quantity }) => {
      const product = state.allGoods.find(p => p.id === id)
      return {
        name: product.name,
        price: product.price,
        id: product.id,
        quantity
      }
    })
  },
  cartProductsAdded: state => {
    return state.added.map(({ id, quantity }) => {
      const product = state.allGoods.find(p => p.id === id)
      return {
        name: product.id,
        quantity
      }
    })
  },
  good: state => state.good,
  article: state => state.article,
  discount: state => state.discount
}

const mutations = {

  [types.SET_GOODS] (state, { goods }) {
    state.allGoods = goods
  },

  [types.SET_ARTICLES] (state, { articles }) {
    state.allArticles = articles
  },

  [types.SET_DISCOUNT] (state, { discounts }) {
    state.allDiscount = discounts
  },

  [types.SET_PRICE] (state, { price }) {
    state.allPrice = price
  },

  [types.REMOVE_FROM_CART] (state, { id }) {
    const remove = state.added.find(p => p.id === id)
    remove.quantity--
    if (remove.quantity <= 0) {
      const good = state.added.find(p => p.id === id)
      const index = state.added.indexOf(good)
      state.added.splice(index, 1)
    }
  },

  [types.CLEAN_ALL_CART] (state) {
    state.added = []
  },

  [types.ADD_TO_CART] (state, { id }) {
    const record = state.added.find(p => p.id === id)
    if (!record) {
      state.added.push({
        id,
        quantity: 1
      })
    } else {
      record.quantity++
    }
  },

  [types.GOOD_ID] (state, { goods }) {
    state.good = goods
  },

  [types.ARTICLE_ID] (state, { article }) {
    state.article = article
  },

  [types.DISCOUNT_ID] (state, { discount }) {
    state.discount = discount
  },

  [types.SET_VK_COMMENTS] (state, { comments }) {
    state.vkComments = comments.items.reverse()
  }
}

const actions = {

  getGoods  ({ commit }) {
    Goods.list().then(goods => {
      commit(types.SET_GOODS, { goods })
    })
  },

  getArticles  ({ commit }) {
    Articles.list().then(articles => {
      commit(types.SET_ARTICLES, { articles })
    })
  },

  getDiscounts  ({ commit }) {
    Discounts.list().then(discounts => {
      commit(types.SET_DISCOUNT, { discounts })
    })
  },

  getPrice  ({ commit }) {
    Price.list().then(price => {
      commit(types.SET_PRICE, { price })
    })
  },

  cleanAllCart ({ commit }) {
    commit(types.CLEAN_ALL_CART)
  },

  addToCart ({ commit }, id) {
    commit(types.ADD_TO_CART, { id })
  },

  removeFromCart ({ commit }, id) {
    commit(types.REMOVE_FROM_CART, { id })
  },

  getGoodId  ({ commit }, id) {
    Goods.id(id).then(goods => {
      commit(types.GOOD_ID, { goods })
    })
  },

  getArticleId  ({ commit }, id) {
    Articles.id(id).then(article => {
      commit(types.ARTICLE_ID, { article })
    })
  },

  getDiscountId  ({ commit }, id) {
    Discounts.id(id).then(discount => {
      commit(types.DISCOUNT_ID, { discount })
    })
  }

}

// one store for entire application
export default new Vuex.Store({
  state,
  strict: debug,
  getters,
  actions,
  mutations
})
