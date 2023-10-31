export const state = () => ({
  usersList: []
})
export const mutations = {
  setUsersList(state, users) {
    state.usersList = users
  }
}

export const actions = {
  async fetchUsersList({ commit }, officeId) {
    await this.$axios.get('user_list', {
      params: {
        office_id: officeId,
      }
    })
      .then(({data}) => {
        commit('setUsersList', data)
      })
  }
}