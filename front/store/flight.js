export const state = () => ({
  airportList: [],
  AirList: [],
  filters: {
    route__departure_airport__iata_code: null,
    route__arrival_airport__iata_code: null,
    flight_number: null,
    date: null,
  }
})

export const mutations = {
  setAirportList(state, list) {
    state.airportList = list
  },
  updateFilters (state, message) {
    state.filters.from = message
  },
  setAirList(state, list) {
    state.AirList = list
  },
  setFilters(state, filters) {
    state.filters = {
      route__departure_airport__iata_code: filters.from,
      route__arrival_airport__iata_code: filters.to,
      flight_number: filters.flightNumber,
      date: filters.date,
      ordering: filters.ordering
    }
  }
}

export const actions = {
  async fetchAirportList({ commit }) {
    await this.$axios({
      url: '/flight.airport_list',
      methods: 'get',
    })
      .then(({data}) => {
        commit('setAirportList', data)
      })
  },
  async fetchAirList({ commit, state }) {
    await this.$axios({
      methods: 'get',
      url: '/flight.schedules_list',
      params: state.filters,
    })
      .then(({data}) => {
        commit('setAirList', data)
      })
  },
  async canselAirList({ dispatch, state }, id) {
    await this.$axios.patch('/flight.schedule_cancel/' + id, {
      confirmed: !state.AirList.find(el => el.id === id).confirmed
    })
      .then(({data}) => {
        dispatch('fetchAirList')
      })
  }
}

