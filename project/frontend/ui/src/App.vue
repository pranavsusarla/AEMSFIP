<template>
  <div>
    <!-- Navigation Bar -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
      <div class="container">
        <div>
          <router-link to="/" class="navbar-brand">Job Matcher</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        </div>
        
        <div class="collapse navbar-collapse" id="navbarNav">
          <div v-if="!$store.state.login">
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <router-link class="nav-link text-white" to="/company-login">Company Login</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link text-white" to="/employee-login">Employee Login</router-link>
              </li>
            </ul>
          </div>
          <div v-else>
            <ul class="navbar-nav ms-auto">
              <li class="nav-item">
                <button class="nav-link text-white" @click="clickLogout">Logout</button>
              </li>
            </ul>
          </div>
        </div>
      </div>
  </nav>

    <!-- Main Router View -->
    <div class="container mt-4">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  methods: {
    clickLogout(){
      this.$store.commit('logoutUser');
      this.$router.push('/');
    }
  }
};
</script>

<style>
body {
  background-color: #f8f9fa;
}

::-webkit-scrollbar {
    display: none;
}

@import'~bootstrap/dist/css/bootstrap.css'
</style>
