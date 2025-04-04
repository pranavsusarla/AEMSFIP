<template>
    <div class="container mt-5 w-50">
      <div class="card p-4 shadow">
        <h3 class="text-center mb-4">Upload Your Skills</h3>
        <form @submit.prevent="uploadSkills">
          <div class="mb-3">
            <label class="form-label">Skills</label>
            <input v-model="skills" type="text" class="form-control" placeholder="Enter skills (comma separated)" required />
          </div>
          <br>
          <button type="submit" class="btn btn-success w-100">Submit</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return { skills: "", resume: null };
    },
    methods: {
      uploadSkills() {
        console.log("Skills uploaded:", this.skills);
        fetch('http://127.0.0.1:5000/upload-skills', {
          method: "POST",
          headers: { 
                "Authorization": "Bearer " + localStorage.token,
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
          body: JSON.stringify({
            'skills': this.skills
          })
        })
        .then(resp => resp.json())
        .then(data => {
          console.log(data);
          alert('Skills Uploaded Successfully');
          this.$router.push('/employee-page')
        })
      },
    },
  };
  </script>
  