<template>
  <div >
    <div class="card border-0 mt-3">
      <div class="card-body">
      
            <router-link to="/profile" class="d-flex nav-link align-items-center p-1" >
              <img
              :src="user.profile_image ? user.profile_image : require('@/assets/img/default-profile.jpg')"                alt=""
                class="rounded-circle border me-2"
                width="40px"
                height="40px"
              />
              <span class="ms-2">{{ user.first_name +' ' +user.last_name}}</span>
            </router-link>
            <router-link to="/friends" class="d-flex nav-link align-items-center  mt-2 " >
                <font-awesome-icon :icon="['fas', 'users']"  class="text-custom"/>
              <span class="ms-3">Friends</span>
          </router-link>
            <router-link to="/friends/request" class="d-flex nav-link align-items-center  mt-2 " >
                <font-awesome-icon :icon="['fas', 'user-plus']" class="text-custom" />
              <span class="ms-3">Friends request</span>
            </router-link>
            <a href="#" class="d-flex nav-link align-items-center  mt-2 " >
                <div class="navbar-items">

                    <font-awesome-icon :icon="['fas', 'message']" class="text-custom" />
                    <span class="count"
            >9+</span
          >
                </div>
              <span class="ms-3">Message</span>
            </a>
            <a href="#" class="d-flex nav-link align-items-center  mt-2 " >
              <div class="navbar-items">
                <font-awesome-icon :icon="['fas', 'bell']" class="text-custom" />
                    <span class="count"
            >9+</span
          >
                </div>
              <span class="ms-3">Notifications</span>
            </a>
            <a href="#" class="d-flex nav-link align-items-center  mt-2 " >
                <font-awesome-icon :icon="['fas', 'gear']" class="text-custom" />
              <span class="ms-3">Settings</span>
            </a>
            
      </div>
    </div>
  </div>
</template>
<script>

import { computed } from 'vue';
import { useStore } from 'vuex';
export default {
  name: "left_section",
  setup(){
    const store = useStore();
    const user = computed(()=>store.state.user);
    return{user}
  }
 
};
</script>
<style scoped>
svg{
    font-size: 1.4rem;

}
a{
    height: 50px;
    height: 50px;
    padding: 1rem;
    border-radius: 5px;
}
.text-custom{
    color :#636c72;
}
a:hover{
    background: #f2f2f2;
}
.navbar-items{
    position:relative;
}
.count {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  background: red;
  font-size: 0.6rem;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  position: absolute;
  top: -5px;
  right: -5px;
}
</style>