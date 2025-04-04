<template>
    <div class="container mt-4">
      <h2 class="mb-4">Generate Job Matches</h2>
  
      <!-- Dropdown to select a job -->
      <div class="mb-4">
        <label for="jobSelect" class="form-label">Select a Job:</label>
        <select v-model="selectedJobId" class="form-select" id="jobSelect">
          <option disabled value="">Select a job</option>
          <option v-for="job in jobs" :key="job.id" :value="job.id">
            {{ job.title }}
          </option>
        </select>
        <button @click="generateMatches" class="btn btn-primary mt-2" :disabled="!selectedJobId">
          Generate Matches
        </button>
      </div>
  
      <!-- Display matching employees -->
      <div v-if="matches.length > 0">
        <h3 class="mb-3">Best Matching Employee</h3>
        <ul class="list-group">
          <li v-for="match in matches" :key="match.employee_id" class="list-group-item">
            <div class="d-flex justify-content-between align-items-center">
              <div>
                <h5 class="mb-1">Employee Email: {{ match.employee_name }}</h5>
                <h5 class="mb-1">Employee ID: {{ match.employee_id }}</h5>
                <small class="text-muted">Similarity Score: {{ match.similarity_score.toFixed(2) }}</small>
              </div>
              <div>
                <span class="badge bg-primary">Skills: {{ match.skills }}</span>
              </div>
            </div>
          </li>
        </ul>
      </div>
  
      <!-- Display message if no matches are found -->
      <div v-else-if="selectedJobId && matches.length === 0" class="alert alert-warning" role="alert">
        No matches found for this job.
      </div>
    </div>
  </template>

<script>
export default {
  name: 'MatchJobs',
  data() {
    return {
      jobs: [], // List of all jobs fetched from the backend
      selectedJobId: '', // Selected job ID from the dropdown
      matches: [], // List of matching employees
    };
  },
  mounted() {
    this.fetchJobs(); // Fetch all jobs when the page loads
  },
  methods: {
    // Fetch all jobs from the backend
    fetchJobs() {
    fetch('http://127.0.0.1:5000/post-job', {
          headers: {
            "Authorization": "Bearer " + localStorage.token,
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
          },
    })
    .then(resp => resp.json())
    .then(data => {
        this.jobs = data.jobs;
    })
    },

    // Generate matches for the selected job
    generateMatches() {
      if (!this.selectedJobId) return;
        fetch(
          `http://127.0.0.1:5000/match-employees/${this.selectedJobId}`,
          {
            headers: {
              "Authorization": "Bearer " + localStorage.token,
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
          }
        )
        .then(resp => resp.json())
        .then(data => {
            this.matches = data.matches;
        })
    },
  },
};
</script>