import { createRouter, createWebHistory } from 'vue-router';
import Dashboard from '@/views/dashboard-view.vue';

const routes = [
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  // add other routes as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
