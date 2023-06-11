import LoginPage from "pages/LoginPage.vue";
import IndexPage from "pages/IndexPage.vue";

const routes = [
  {
    path: '/',
    component: IndexPage,
  },
  {
    path: '/login',
    component: LoginPage,
  }
]

export default routes
