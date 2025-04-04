import { createRouter, createWebHistory } from 'vue-router';
import CompanyLogin from '@/components/CompanyLogin.vue';
import EmployeeLogin from '@/components/EmployeeLogin.vue';
import JobPosting from '@/components/JobPosting.vue';
import SkillUpload from '@/components/SkillUpload.vue';
import JobMatching from '@/components/JobMatching.vue';
import HomePage from '@/components/HomePage.vue';
import CompanyPage from '@/components/CompanyPage.vue';
import EmployeePage from '@/components/EmployeePage.vue';
import MyJobs from '@/components/MyJobs.vue';
import MatchJobs from '@/components/MatchJobs.vue';
import MyMatches from '@/components/MyMatches.vue';
import CompanyHome from '@/components/CompanyHome.vue';
import EmployeeHome from '@/components/EmployeeHome.vue';

const routes = [
  { path: '/', component: HomePage},
  { path: '/company-login', component: CompanyLogin },
  { path: '/employee-login', component: EmployeeLogin },
  { path: '/job-matching', component: JobMatching },
  { path: '/company-page', component: CompanyPage , children:[
    { path: 'company-home', component: CompanyHome },
    { path: 'job-posting', component: JobPosting},
    { path: 'my-jobs', component: MyJobs},
    { path: 'match-jobs', component: MatchJobs},
  ]},
  { path: '/employee-page', component: EmployeePage, children:[
    { path: 'employee-home', component: EmployeeHome },
    { path: 'skill-upload', component: SkillUpload },
    { path: 'my-matches', component: MyMatches }
  ]}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;