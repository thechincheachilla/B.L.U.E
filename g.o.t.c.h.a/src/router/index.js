import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Legislators from "../views/Legislators.vue";
import Legislation from "../views/Legislation.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/legislators",
    name: "Legislators",
    component: Legislators
  },
  {
    path: "/legislation",
    name: "Legislation",
    component: Legislation
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
