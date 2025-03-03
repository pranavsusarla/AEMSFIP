import { createStore } from 'vuex'

export default createStore({
  state: {
    login: false,
    token: ""
  },
  getters: {
  },
  mutations: {
    loginUser: function(state, token){
      state.login = true;
      state.token = token;
    },
    logoutUser: function(state){
      state.login = false;
      state.token = "";
    }
  },
  actions: {
  },
  modules: {
  }
})
