<template>
    <div>
        <div class="container d-flex justify-content-center align-items-center">
        <nav class="nav navbar">
            <router-link to='/employee-page/employee-home' class="nav-link">Employee Home</router-link>
            <router-link to='/employee-page/skill-upload' class="nav-link">Upload your Skills</router-link>
            <router-link to='/employee-page/my-matches' class="nav-link">My Job Matches</router-link>
        </nav>
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
        }
    }
</script>

<style scoped>

</style>