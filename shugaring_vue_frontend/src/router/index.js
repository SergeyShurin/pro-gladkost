import Vue from 'vue'
import Router from 'vue-router'

import About from '@/components/About'
import Blog from '@/components/Blog'
import BlogArticle from '@/components/BlogArticle'
import Cart from '@/components/Cart'
import Contacts from '@/components/Contacts'
import Enrol from '@/components/Enrol'
import Goods from '@/components/Goods'
import GoodsDetail from '@/components/GoodsDetail'
import Home from '@/components/Home'
import NotFound from '@/components/NotFound'
import Price from '@/components/Price'
import Shares from '@/components/Shares'
import SharesArticle from '@/components/SharesArticle'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/about',
      name: 'About',
      component: About
    },
    {
      path: '/blog',
      name: 'Blog',
      component: Blog
    },
    {
      path: '/blog/:id',
      name: 'BlogArticle',
      component: BlogArticle,
      props: true
    },
    {
      path: '/cart',
      name: 'Cart',
      component: Cart
    },
    {
      path: '/contacts',
      name: 'Contacts',
      component: Contacts
    },
    {
      path: '/enrol',
      name: 'Enrol',
      component: Enrol
    },
    {
      path: '/goods',
      name: 'Goods',
      component: Goods
    },
    {
      path: '/goods/:id',
      name: 'GoodsDetail',
      component: GoodsDetail,
      props: true
    },
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound
    },
    {
      path: '/price',
      name: 'Price',
      component: Price
    },
    {
      path: '/shares',
      name: 'Shares',
      component: Shares
    },
    {
      path: '/shares/:id',
      name: 'SharesArticle',
      component: SharesArticle,
      props: true
    }
  ]
})
