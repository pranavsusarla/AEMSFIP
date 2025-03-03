<template>
    <div class="container mt-4 mb-4">
      <div class="card shadow-sm p-4">
        <h2 class="text-center mb-4">Post a Job</h2>
        <form>
          <!-- Job Title -->
          <div class="mb-3">
            <label for="title" class="form-label">Job Title</label>
            <input type="text" class="form-control" id="title" v-model="job.title" required />
          </div>
  
          <!-- Job Description -->
          <div class="mb-3">
            <label for="description" class="form-label">Job Description</label>
            <textarea class="form-control" id="description" v-model="job.description" rows="3" required></textarea>
          </div>
  
          <!-- Required Skills -->
          <div class="mb-3">
            <label for="skills" class="form-label">Required Skills</label>
            <input type="text" class="form-control" id="skills" v-model="job.skills" placeholder="Comma-separated (e.g., Python, Vue.js)" required />
          </div>
  
          <!-- Location -->
          <div class="mb-3">
            <label for="location" class="form-label">Location</label>
            <input type="text" class="form-control" id="location" v-model="job.location" required />
          </div>
  
          <!-- Salary Range -->
          <div class="mb-3">
            <label for="salary" class="form-label">Salary Range</label>
            <input type="text" class="form-control" id="salary" v-model="job.salary" placeholder="e.g., 50,000 - 80,000 INR per month" required />
          </div>
  
          <!-- Submit Button -->
          <div class="d-grid">
            <button type="button" class="btn btn-primary" @click="submitJob">Post Job</button>
          </div>
        </form>
      </div>
    <!-- <div>
        <h4 class="">{{ message }}</h4>
    </div> -->
    </div>
  </template>
  
  <script>
  
  export default {
    data() {
      return {
        job: {
          title: "",
          description: "",
          skills: "",
          location: "",
          salary: "",
          message: ""
        },
      };
    },
    methods: {
      submitJob() {
        fetch('http://127.0.0.1:5000/post-job',{
            method: "POST",
            headers: { 
                "Authorization": "Bearer " + localStorage.token,
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            body: JSON.stringify({
                'title': this.job.title,
                'description': this.job.description,
                'location': this.job.location,
                'required_skills': this.job.skills,
                'salary_range': this.job.salary    
            })
        })
        .then(resp => resp.json())
        .then(data =>{
            console.log(data);
            this.message = data.message;
            alert('Job Successfully posted!');
            this.$router.push('/company-page');
        })
      },
    },
  };
  </script>
  
  <style scoped>
  .card {
    max-width: 600px;
    margin: auto;
    border-radius: 10px;
  }
  
  .btn-primary {
    font-weight: bold;
  }
  
  input,
  textarea {
    border-radius: 6px;
  }
  
  h2 {
    color: #007bff;
  }
  </style>
  