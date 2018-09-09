import { HTTP } from './common'

export const Price = {

  list () {
    return HTTP.get('/price/').then(response => {
      return response.data
    })
  }
}
