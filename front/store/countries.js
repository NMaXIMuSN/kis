export const state = () => ({
  countries: [],
})

export const mutations = {
  setCountries(state, list) {
    state.countries = list
  },
}

export const actions = {
  async fetchCountries({ commit }) {
    await this.$axios({
      url: '/country_list',
      methods: 'get',
    })
      .then(({data}) => {
        commit('setCountries', data)
      })
  },
}

