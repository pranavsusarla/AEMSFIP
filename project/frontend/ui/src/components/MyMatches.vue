<template>
    <div class="container mt-4 mb-4">
      <h2 class="mb-4">My Matched Jobs</h2>
  
      <div v-if="matchedJobs.length > 0">
        <ul class="list-group">
          <li v-for="job in matchedJobs" :key="job.job_id" class="list-group-item">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <h5 class="mb-1">{{ job.title }}</h5>
                <small class="text-muted">Location: {{ job.location }}</small>
              </div>
              <div>
                <span class="badge bg-primary me-2">Salary: {{ job.salary_range }}</span>
              </div>
            </div>
            <div class="mt-2">
              <p class="mb-1">{{ job.description }}</p>
              <small class="text-muted">Required Skills: {{ job.required_skills }}</small>
            </div>
          </li>
        </ul>
      </div>
  
      <div v-else class="alert alert-warning" role="alert">
        You have not been matched with any jobs yet.
      </div>
    </div>
  </template>

<script>
export default {
  name: 'MyMatches',
  data() {
    return {
      matchedJobs: [],
    };
  },
  mounted() {
    this.fetchMatchedJobs(); 
  },
  methods: {
    fetchMatchedJobs() {
        fetch('http://127.0.0.1:5000/employee/matched-jobs', {
          headers: {
            "Authorization": "Bearer " + localStorage.token,
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
          },
        })
        .then(resp => resp.json())
        .then(data => {
            this.matchedJobs = data.matched_jobs;
        })
    },
  },
};
</script>