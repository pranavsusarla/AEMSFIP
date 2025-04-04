<template>
    <div class="container my-5 p-4 shadow rounded bg-light">
        <div class="text-center mb-4">
            <h2 class="text-primary fw-bold">Welcome!</h2>
        </div>

        <div v-if="skills && skills.length" class="alert alert-success text-center">
            <h5 class="mb-0">
                My Skills: {{ skills }}
            </h5>
        </div>

        <div v-else class="text-center text-muted">
            <p>No skills uploaded yet.</p>
        </div>
    </div>

</template>

<script>
    export default {
        name: 'EmployeeHome',
        data(){
            return{
                skills: ''
            }
        },
        methods: {
            async showSkills() {
                try {
                    const response = await fetch('http://127.0.0.1:5000/upload-skills', {
                        headers: { 
                            "Authorization": "Bearer " + localStorage.token,
                            "Content-Type": "application/json",
                            "Access-Control-Allow-Origin": "*"
                        }
                    });
                    const data = await response.json();
                    console.log(data);
                    this.skills = data.skills;
                } catch (error) {
                    console.error("Error fetching skills:", error);
                }
            }
        },
        mounted() {
            this.showSkills();
        }

    }
</script>

<style scoped>

</style>