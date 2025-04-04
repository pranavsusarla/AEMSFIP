<template>
  <div>
    <div class="container d-flex justify-content-center align-items-center">
        <nav class="nav navbar">
            <router-link to='/company-page/company-home' class="nav-link">Company Home</router-link>
            <router-link to='/company-page/my-jobs' class="nav-link">My Jobs</router-link>
            <router-link to='/company-page/job-posting' class="nav-link">Post a Job</router-link>
            <router-link to='/company-page/match-jobs' class="nav-link">Match Jobs</router-link>
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
  