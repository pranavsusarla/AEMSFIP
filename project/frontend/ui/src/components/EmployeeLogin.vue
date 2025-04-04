<template>
<div>
    <div class="container d-flex justify-content-center bg-light">
  <div class="card p-4 shadow-lg rounded-4" style="width: 400px;">
    <h3 class="text-center text-primary mb-4 fw-bold">
      <i class="bi bi-person-badge-fill me-2"></i>Employee Login
    </h3>

    <form @submit.prevent="login">
      <div class="mb-3">
        <label for="email" class="form-label fw-semibold">Email address</label>
        <input
          v-model="email"
          type="email"
          id="email"
          class="form-control form-control-lg"
          placeholder="Enter your email"
          required
        />
      </div>

      <div class="mb-3">
        <label for="password" class="form-label fw-semibold">Password</label>
        <input
          v-model="password"
          type="password"
          id="password"
          class="form-control form-control-lg"
          placeholder="Enter your password"
          required
        />
      </div>

      <button type="submit" class="btn btn-primary w-100 fw-semibold py-2">
        Login
      </button>
    </form>
  </div>
</div>

<!-- Include Bootstrap Icons CDN if not already done -->
<link
  href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css"
  rel="stylesheet"
/>
</div>
  </template>
  
  <script>
  export default {
    data() {
      return { email: "", password: "" };
    },
    methods: {
      login() {
        console.log("Employee logged in:", this.email);
        fetch('http://127.0.0.1:5000/login', {
          method:'POST',
          headers: { 
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
          body: JSON.stringify({
            'email': this.email,
            'password': this.password
          })
        })
        .then(resp => resp.json())
        .then(data => {
          console.log(data);
          if(data.message == "Login successful"){
            this.$store.commit('loginUser', data.token);
            this.$router.push("/employee-page/employee-home");
          }else{
            this.$router.push("/employee-login")
          }
        })

      },
    },
  };
  </script>
  