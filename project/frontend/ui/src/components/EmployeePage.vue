<template>
    <div>
        <div class="container d-flex justify-content-center align-items-center">
        <nav class="nav navbar">
            <router-link to='/employee-page' class="nav-link">Employee Home</router-link>
            <router-link to='/employee-page/skill-upload' class="nav-link">Upload your Skills</router-link>
        </nav>
    </div>
    <span v-if="skills != ''">My skills: {{ skills }}</span>
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
        mounted(){
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
</script>

<style scoped>

</style>