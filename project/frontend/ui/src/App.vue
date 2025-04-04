<template>
  <div>
    <!-- Navigation Bar -->
<nav class="navbar navbar-expand-lg navbar-dark shadow-sm bg-primary bg-gradient">
  <div class="container">
    <template v-if="!$store.state.login">
    <router-link to="/" class="navbar-brand fw-bold fs-4 text-white">
      <i class="bi bi-briefcase-fill me-2"></i>Job Matcher
    </router-link>

    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link class="nav-link text-white fw-semibold" to="/company-login">
              Company Login
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link text-white fw-semibold" to="/employee-login">
              Employee Login
            </router-link>
          </li>
      </ul>
    </div>
    </template>
    <template v-else>
      <router-link to="#" class="navbar-brand fw-bold fs-4 text-white">
      <i class="bi bi-briefcase-fill me-2"></i>Job Matcher
    </router-link>

    <button
      class="navbar-toggler"
      type="button"
      data-bs-toggle="collapse"
      data-bs-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <button class="nav-link text-white fw-semibold btn btn-link" @click="clickLogout">
              Logout
            </button>
          </li>
      </ul>
    </div>
    </template>
  </div>
</nav>

<!-- Bootstrap Icons CDN (optional, for the icon in the brand name) -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css" rel="stylesheet">

    <!-- Main Router View -->
    <div class="mt-4">
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
