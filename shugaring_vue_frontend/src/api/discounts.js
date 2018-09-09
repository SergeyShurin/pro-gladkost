import { HTTP } from './common'

export const Discounts = {

  list () {
    return HTTP.get('/discount/').then(response => {
      return response.data
    })
  },

  id (id) {
    return HTTP.get('/discount/' + id + '/').then(response => {
      return response.data
    })
  }
}
