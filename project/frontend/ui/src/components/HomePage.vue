<template>
<div>
  <div class="header text-center">
    <h4 class="mt-2">Expert Matching and Relevancy Scoring System</h4>
    <h5 class="fw-bold">Major Project Team - 01</h5>
  </div>

  <div class="container section">
    <div class="row justify-content-center">
      <div class="col-lg-10">
        <div class="card shadow-lg border-0 rounded-4">
          <div class="card-body p-4">
            <h4 class="text-primary fw-bold mb-3">Project Overview</h4>
            <p class="lead text-muted">
              Our project, <strong>Expert Matching and Relevancy Scoring System</strong>, is a web-based platform that automates the process of matching candidates to job roles based on their skills. It leverages natural language processing (NLP) and similarity scoring techniques to compare job requirements with employee skill sets. The system then identifies the best-fit candidates and automatically notifies both the employer and the potential employee via email, enhancing efficiency in hiring and reducing manual effort.
            </p>
            <p class="text-muted">
              Features include role-based authentication, skill uploads, intelligent matching algorithms, and HTML email alerts. It's built using <strong>Flask</strong> for the backend, <strong>Vue 3</strong> for the frontend, and utilizes <strong>JWT for authentication</strong>.
            </p>

            <h5 class="mt-4 fw-bold text-secondary">Team Members</h5>
            <div class="row row-cols-1 row-cols-md-2 g-3 mt-2">
              <div class="col">
                <div class="card team-card border-primary shadow-sm">
                  <div class="card-body text-center">
                    <h6 class="card-title fw-bold">Nikhil K</h6>
                    <p class="card-text text-muted">21071A6932</p>
                  </div>
                </div>
              </div>
              <div class="col">
                <div class="card team-card border-primary shadow-sm">
                  <div class="card-body text-center">
                    <h6 class="card-title fw-bold">Pranav S</h6>
                    <p class="card-text text-muted">21071A6957</p>
                  </div>
                </div>
              </div>
              <div class="col">
                <div class="card team-card border-primary shadow-sm">
                  <div class="card-body text-center">
                    <h6 class="card-title fw-bold">Rohit Y S</h6>
                    <p class="card-text text-muted">21071A6963</p>
                  </div>
                </div>
              </div>
              <div class="col">
                <div class="card team-card border-primary shadow-sm">
                  <div class="card-body text-center">
                    <h6 class="card-title fw-bold">Aadarsh B</h6>
                    <p class="card-text text-muted">22075A6901</p>
                  </div>
                </div>
              </div>
            </div>

            <h5 class="mt-4 fw-bold text-secondary">Project Guide</h5>
            <div class="alert alert-info text-center mt-3" role="alert">
              Dr. Kousar Nikhath
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="footer">
    <p class="mb-0">© 2025 Major Project - All Rights Reserved</p>
  </div>
</div>

</template>

<script>
    export default {
        name: 'HomePage'
    }
</script>

<style scoped>
body {
      background: linear-gradient(to right, #f7f9fc, #e2eafc);
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .header {
      background-color: #0d6efd;
      color: white;
      padding: 40px 0;
      border-bottom: 5px solid #0a58ca;
    }
    .section {
      padding: 40px 20px;
    }
    .team-card {
      transition: transform 0.3s ease;
    }
    .team-card:hover {
      transform: scale(1.03);
    }
    .footer {
      background-color: #0d6efd;
      color: white;
      text-align: center;
      padding: 20px;
      margin-top: 40px;
    }
</style>