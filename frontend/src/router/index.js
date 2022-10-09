import { createRouter, createWebHistory } from "vue-router";
import MangaAllView from "../components/MangaAllView.vue";
import MangaView from "../components/MangaView.vue";
import HomeView from '../components/HomeView.vue';
import AboutView from '../components/AboutView.vue';
import LoginView from '../components/LoginView.vue';
import ProfileView from '../components/ProfileView.vue';
import RegisterView from '../components/RegisterView.vue';

const routes = [
    {
        path: "",
        name: "Home",
        component: HomeView,
    },
  {
    path: "/login",
    name: "login",
  },
  {
    path: "/manga",
    name: "manga",
    component: MangaAllView,
  },
  {
    path: "/manga/:id",
    component: MangaView,
  },
  {
    path:"/about",
    name: "about",
    component: AboutView,
  },
  {
    path:"/login",
    name: "login",
    component: LoginView,
  },
  {
    path:"/profile",
    name: "profile",
    component: ProfileView,
  },
  {
    path:"/register",
    name: "register",
    component: RegisterView,
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
