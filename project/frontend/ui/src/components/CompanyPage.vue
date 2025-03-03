<template>
  <div>
    <div class="container d-flex justify-content-center align-items-center">
        <nav class="nav navbar">
            <router-link to='/company-page' class="nav-link">Company Home</router-link>
            <router-link to='/company-page/job-posting' class="nav-link">Post a Job</router-link>
        </nav>
    </div>
    <router-view></router-view>
  </div>
  </template>
  
  <script>
  export default {
    name: 'CompanyPage',
    data() {
      return { };
    },
    methods: {}
  };
  </script>
  