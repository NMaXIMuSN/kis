export const state = () => ({
  airportList: [],
  AirListTo: [],
  AirListReturn: [],
  isReturn: false,
  AfterBeforeTo: false,
  AfterBeforeFrom: false,
  filters: {
    route__departure_airport__iata_code: null,
    route__arrival_airport__iata_code: null,
    cabinType: '',
    date: null,
    return: null,
  },
})

export const mutations = {
  setFilters(state, filters) {
    state.filters = {
      route__departure_airport__iata_code: filters.from,
      route__arrival_airport__iata_code: filters.to,
      date: filters.date,
      cabinType: filters.cabinType,
      return: filters.return
    }
    state.isReturn = filters.isReturn
  },
  setAfterBeforeTo(state, value) {
    state.AfterBeforeTo = value
  },
  setAfterBeforeFrom(state, value) {
    state.AfterBeforeFrom = value
  },
  setAirListTo(state, list) {
    state.AirListTo = list
  },
  setAirListReturn(state, list) {
    state.AirListReturn = list
  },
}

export const actions = {
  async fetchAirListTo({ commit, state }, params) {
    try { 
      const { data } = await this.$axios({
        methods: 'get',
        url: '/flight.schedules_list',
        params: {...state.filters, after_before: state.AfterBeforeTo ? true : null},
      })
      
      commit('setAirListTo', data || [])
    } catch (error) {
      
    }
  },
  async fetchAirListReturn({ commit, state }, params) {
    try { 
      const { data } = await this.$axios({
        methods: 'get',
        url: '/flight.schedules_list',
        params: {
          route__departure_airport__iata_code: state.filters.route__arrival_airport__iata_code,
          route__arrival_airport__iata_code: state.filters.route__departure_airport__iata_code,
          date: state.filters.return ? state.filters.return : null,
          after_before: state.AfterBeforeFrom ? true : null,
        },
      })
      
      commit('setAirListReturn', data || [])
    } catch (error) {
      
    }
  },
  async fetchAirList({ state, dispatch }) {
    const array = [dispatch('fetchAirListTo')]

    if (state.isReturn) {
      array.push(dispatch('fetchAirListReturn'))
    }

    await Promise.all(array)
  },
}

