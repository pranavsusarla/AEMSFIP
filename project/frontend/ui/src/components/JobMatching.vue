<template>
    <div class="container mt-5 w-50">
      <div class="card p-4 shadow">
        <h3 class="text-center mb-4">Job Matching Results</h3>
        <button class="btn btn-primary w-100" @click="findMatches">Search for Interviewers</button>
        <div v-if="matches.length" class="mt-4">
          <h4 class="text-center">Best Matches:</h4>
          <ul class="list-group">
            <li v-for="match in matches" :key="match.id" class="list-group-item d-flex justify-content-between">
              <span>{{ match.name }}</span>
              <span class="text-muted">{{ match.skills.join(", ") }}</span>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return { matches: [] };
    },
    methods: {
      findMatches() {
        this.matches = [
          { id: 1, name: "John Doe", skills: ["Vue.js", "JavaScript"] },
          { id: 2, name: "Jane Smith", skills: ["Python", "Machine Learning"] },
        ];
      },
    },
  };
  </script>
  