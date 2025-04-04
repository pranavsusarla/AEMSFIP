<template>
    <div class="container d-flex justify-content-center align-items-center">
      <div class="card p-4 shadow" style="width: 400px;">
        <h3 class="text-center mb-3">Employee Login</h3>
        <form @submit.prevent="login">
          <div class="mb-3">
            <label class="form-label">Email</label>
            <input v-model="email" type="email" class="form-control" required />
          </div>
          <div class="mb-3">
            <label class="form-label">Password</label>
            <input v-model="password" type="password" class="form-control" required />
          </div>
          <button type="submit" class="btn btn-primary w-100">Login</button>
        </form>
      </div>
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
          this.$store.commit('loginUser', data.token);
        })
        this.$router.push("/employee-page/employee-home");
      },
    },
  };
  </script>
  