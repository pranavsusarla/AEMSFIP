<template>
    <div class="container">
        <h5>Welcome!</h5>
        <div>
            <span v-if="skills != ''"><h5 class="">My skills: {{ skills }}</h5></span>
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