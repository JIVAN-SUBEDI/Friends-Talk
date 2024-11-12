import { createRouter, createWebHistory } from "vue-router";
import home from "./components/home.vue";
import Login from "./components/Login.vue";
import otp from "./components/otp.vue"
import store from "./store";
import profile from "./components/profile.vue";
import friendsSearch from "./components/friendsSearch.vue";
import profileView from "./components/profileView.vue";
import friendRequest from "./components/friendRequest.vue";
import friends from "./components/friends.vue";
import postView from "./components/postView.vue";
// import axiosInstance from "./axios";
const routes = [
  {
    name: "home",
    path: '/',
    component: home,
    meta: { requiresAuth: true },
  },
  {
    name: "login",
    path: '/login',
    component: Login,
    meta: { guestOnly: true },

  },
  {
    name: "profile",
    path: '/profile',
    component: profile,
    meta: { requiresAuth: true },

  },
  {
    name: "otp",
    path: '/otp-verify/:email',
    component: otp,
    props: true,
    meta: { guestOnly: true },
  },
  {
    name: "friend search",
    path: '/search',
    component: friendsSearch,
    meta: { requiresAuth: true },
    beforeEnter: (to, from, next) => {
      const query = to.query.query;
      if (query && query.trim() !== '') {
        next();

        store.dispatch('performSearch', query);
      } else {
        next('/'); // Redirect to homepage or another page if the query is empty
      }
    }
  },
  {
    name: "profile view",
    path: '/profile/view/:id',
    component: profileView,
    meta: { requiresAuth: true },
    props: true, // Enable props to pass data to the component
    beforeEnter: (to, from, next) => {
      const id = to.params.id; // Get the 'id' parameter from the route

      if (id && id.trim() !== '') {
        store.dispatch('fetchUser',id);
        next();
      } else {
        next('/'); // Redirect to homepage if 'id' is invalid or empty
      }
    },


  },
  {
    name: "Friend Request",
    path: '/friends/request',
    component: friendRequest,
    meta: { requiresAuth: true },
  },
  {
    name: "Friend ",
    path: '/friends',
    component: friends,
    meta: { requiresAuth: true },
  },
  {
    name:"postview",
    path:"/post/:id",
    component:postView,
    meta: { requiresAuth: true },
  }
]
const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});
router.beforeEach((to, from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    // If route requires auth and user is not authenticated, redirect to login
    if (!store.state.isAuth) {
      next('/login');
    } else {
      next();
    }
  } else if (to.matched.some((record) => record.meta.guestOnly)) {
    // If route is guest-only and user is authenticated, redirect to dashboard
    if (store.state.isAuth) {
      next('/');
    } else {
      next();
    }
  } else {
    next();
  }
});
export default router;