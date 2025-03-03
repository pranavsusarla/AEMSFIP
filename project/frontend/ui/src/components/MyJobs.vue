<template>
    <div class="container mt-4 mb-4">
        <div v-if="jobs.length !== 0">
            <h2 class="mb-4">My Jobs</h2>
            <ul class="list-group">
                <li v-for="job in jobs" :key="job.id" class="list-group-item">
                    <div class="d-flex justify-content-between align-items-center">
                        <div>
                            <h5 class="mb-1">{{ job.title }}</h5>
                            <small class="text-muted">Location: {{ job.location }}</small>
                        </div>
                        <div>
                            <span class="badge bg-primary me-2">Salary: {{ job.salary_range }}</span>
                            <span class="badge bg-success">Skills: {{ job.required_skills }}</span>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
        <div v-else class="alert alert-warning" role="alert">
            No jobs available yet
        </div>
    </div>
</template>

<script>
export default {
    name: 'MyJobs',
    data() {
        return {
            jobs: []
        }
    },
    mounted() {
        fetch('http://127.0.0.1:5000/post-job', {
            headers: { 
                "Authorization": "Bearer " + localStorage.token,
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        })
        .then(resp => resp.json())
        .then(data => {
            this.jobs = data.jobs;
        })
    }
}
</script>

<style scoped>
</style>