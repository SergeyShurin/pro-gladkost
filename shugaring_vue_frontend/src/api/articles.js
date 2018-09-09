import { HTTP } from './common'

export const Articles = {

  list () {
    return HTTP.get('/blog/').then(response => {
      return response.data
    })
  },

  id (id) {
    return HTTP.get('/blog/' + id + '/').then(response => {
      return response.data
    })
  }
}
