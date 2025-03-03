import { createRouter, createWebHistory } from 'vue-router';
import CompanyLogin from '@/components/CompanyLogin.vue';
import EmployeeLogin from '@/components/EmployeeLogin.vue';
import JobPosting from '@/components/JobPosting.vue';
import SkillUpload from '@/components/SkillUpload.vue';
import JobMatching from '@/components/JobMatching.vue';
import HomePage from '@/components/HomePage.vue';
import CompanyPage from '@/components/CompanyPage.vue';
import EmployeePage from '@/components/EmployeePage.vue';

const routes = [
  { path: '/', component: HomePage},
  { path: '/company-login', component: CompanyLogin },
  { path: '/employee-login', component: EmployeeLogin },
  { path: '/job-matching', component: JobMatching },
  { path: '/company-page', component: CompanyPage , children:[
    { path: 'job-posting', component: JobPosting}
  ]},
  { path: '/employee-page', component: EmployeePage, children:[
    { path: 'skill-upload', component: SkillUpload }
  ]}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;