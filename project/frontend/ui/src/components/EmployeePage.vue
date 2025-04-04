<template>
    <div>
        <div class="container d-flex justify-content-center align-items-center">
        <nav class="nav navbar">
            <router-link to='/employee-page' class="nav-link">Employee Home</router-link>
            <router-link to='/employee-page/skill-upload' class="nav-link">Upload your Skills</router-link>
            <router-link to='/employee-page/my-matches' class="nav-link">My Job Matches</router-link>
        </nav>
    </div>
    <div class="container">
        <h5>Welcome!</h5>
        <div>
            <button class="btn btn-success" @click="showSkills">Show my Skills</button>
            <span v-if="skills != ''"><h5 class="m-3">My skills: {{ skills }}</h5></span>
        </div>
    </div>
    <router-view></router-view>
</div>
</template>

<script>
    export default {
        name: 'EmployeePage',
        data(){
            return{
                skills: ""
            }
        },
        methods:{
            showSkills(){
            fetch('http://127.0.0.1:5000/upload-skills', {
                headers: { 
                    "Authorization": "Bearer " + localStorage.token,
                    "Content-Type": "application/json",
                    "Access-Control-Allow-Origin": "*"
                }
            })
            .then(resp => resp.json())
            .then(data => {
                console.log(data);
                this.skills = data.skills;
            })
        }
        }
    }
</script>

<style scoped>

</style>