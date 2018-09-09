import axios from 'axios'
import Cookies from 'js-cookie'

var token = Cookies.get('csrftoken')

export const HTTP = axios.create({
  baseURL: 'http://pro-gladkost.ru/api/v1/',
  headers: {'X-CSRFToken': token}
  // baseURL: 'http://127.0.0.1:8000/api/v1/'
})
