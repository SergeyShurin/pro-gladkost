import { HTTP } from './common'

export const Goods = {

  list () {
    return HTTP.get('/goods/').then(response => {
      return response.data
    })
  },

  id (id) {
    return HTTP.get('/goods/' + id + '/').then(response => {
      return response.data
    })
  }
}

export const Enrol = {

  add_enrol (config) {
    return HTTP.post('/enrol/', config).then(response => {
      return response.data
    })
  }
}
