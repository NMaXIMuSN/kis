export const state = () => ({
  list: [],
  currentOffice: 1,
  role: []
})
export const mutations = {
  setList(state, lists) {
    state.list = lists
  },
  setRole(state, roles) {
    state.role = roles
  }
}

export const actions = {
  async fetchList({commit}) {
    await this.$axios.get('office_list')
      .then(({data}) => {
        commit('setList', data)
      })
  },
  async fetchRole({commit}) {
    await this.$axios.get('role_list')
      .then(({data}) => {
        commit('setRole', data)
      })
  }
}