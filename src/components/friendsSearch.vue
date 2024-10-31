<template>
  <div>
    <navbarVue/>
    <div class="container-fluid">
      <div class="row">
        <!-- Sidebar -->
        <div class="col-md-3 bg-white p-3">
          <h4>Filter Results</h4>
          <div class="form-group">
            <label for="">City</label>
            <input type="text" class="form-control" placeholder="City" v-model="city">
            <label for="" class="mt-2">Education</label>
            <input type="text" class="form-control" placeholder="Education" v-model="education">
            <label for="" class="mt-2">Work</label>
            <input type="text" class="form-control" placeholder="Work" v-model="work">
            <button class="btn btn-primary mt-3" @click="filter">Filter</button>
          </div>
        </div>

        <!-- Main content -->
        <div class="col-md-9 bg-light" style="min-height: calc(100vh - 80px); height: auto;">
          <div v-if="results && results.results.length" class="d-flex flex-column justify-content-start align-items-center">
            <div class="d-flex mt-3 bg-white p-2 align-items-center w-80 rounded justify-content-between" v-for="user in results.results" :key="user.id">
              <router-link class="d-flex align-items-center text-decoration-none" @click="profileView(user.id)" :to="'/profile/view/'+user.id">
                <img :src="user.profile_image ? user.profile_image : require('@/assets/img/default-profile.jpg')" alt="profile" class="rounded-circle border me-2 cursor-pointer" width="80px" height="80px" />
                <div class="d-flex flex-column ms-2">
                  <h6 class="cursor-pointer text-dark hover-underline">{{ user.first_name || 'N/A' }} {{ user.last_name || '' }}</h6>
                  <span class="text-secondary text-small" v-if="user.status == 'Friend'">Friend</span>
                  <span class="text-secondary text-small" v-else-if="user.mutual_friend_count > 0">{{ user.mutual_friend_count }} Mutual friends</span>
                </div>
              </router-link>
              <button class="btn btn-primary" @click="addFriend(user.id)" v-if="user.status == 'Not Friends'"><font-awesome-icon :icon="['fas', 'user-plus']" /> <span class="ms-1">Add Friend</span></button>
              <button class="btn btn-danger" @click="deleteRequest(user.id)" v-if="user.status == 'Request Sent'"><font-awesome-icon :icon="['fas', 'trash']" /><span class="ms-1">Delete Request</span></button>
              <div v-if="user.status == 'Request Received'" class="d-flex gap-3">
                <button class="btn btn-primary" @click="acceptRequest(user.id)">Accept</button>
                <button class="btn btn-danger" @click="rejectRequest(user.id)">Reject</button>
              </div>
            </div>

            <a v-if="results.next != null" class="text-primary mt-2 cursor-pointer text-decoration-none" @click="showMore"> Show More</a>
            <div v-if="loadingMore" class="mt-2 text-secondary">Loading more...</div>
          </div>

          <div v-else class="col-12  mt-5">
            <div class="alert alert-info text-center">No friends found matching your search.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed, ref } from 'vue';
import navbarVue from './partials/navbar.vue';
import { useStore } from 'vuex';
import axiosInstance from '@/axios';
import { useRouter } from 'vue-router';

export default {
  name: "friend_search",
  components: { navbarVue },
  setup() {
    const store = useStore();
    const loadingMore = ref(false);
    const city = ref('');
    const education = ref('');
    const work = ref('');
    const results = computed(() => store.state.search || { results: [] });
    const router = useRouter();

    const showMore = async () => {
      loadingMore.value = true;
      await axiosInstance.get(results.value.next).then(resp => {
        const oldResults = results.value.results;
        const result = resp.data;
        result.results = [...oldResults, ...result.results];
        store.commit('SET_SEARCH_RESULTS', result);
      }).finally(() => {
        loadingMore.value = false;
      });
    };

    const addFriend = async (id) => {
      await axiosInstance.get(`friend-request/send/${id}/`).then(() => {
        const status = 'Request Sent';
        store.commit('UPDATE_FRIEND_STATUS', { id, status });
      });
    };

    const deleteRequest = async (id) => {
      await axiosInstance.get(`friend-request/delete/${id}/`).then(() => {
        const status = 'Not Friends';
        store.commit('UPDATE_FRIEND_STATUS', { id, status });
      });
    };

    const rejectRequest = async (id) => {
      await axiosInstance.get(`friend-request/reject/${id}/`).then(() => {
        const status = 'Not Friends';
        store.commit('UPDATE_FRIEND_STATUS', { id, status });
      });
    };

    const acceptRequest = async (id) => {
      await axiosInstance.get(`friend-request/accept/${id}/`).then(() => {
        const status = 'Friend';
        store.commit('UPDATE_FRIEND_STATUS', { id, status });
      });
    };

    const filter = async () => {
      const query = router.currentRoute.value.query.query;
      await axiosInstance.get(`search/${query}/?city=${city.value}&work=${work.value}&education=${education.value}`).then(resp => {
        store.commit('SET_SEARCH_RESULTS', resp.data);
      });
    };

    const profileView = async (id) => {
      await axiosInstance.get('profile/view/' + id).then(resp => {
        console.log(resp.data);
      });
    };

    return { results, showMore, loadingMore, addFriend, deleteRequest, rejectRequest, acceptRequest, filter, city, education, work, profileView };
  }
};
</script>

  <style scoped>
  /* Adjust the flex container to not stretch vertically */
  .d-flex {
    height: auto !important; /* Force auto height for all flex containers */
  }
  
  /* Ensure the inner content is centered horizontally, but not vertically stretched */
  .w-80 {
    width: 80%;
  }
  
  /* Adjust the image style to ensure it doesn’t stretch */
  img {
    object-fit: cover;
  }
  .hover-underline:hover{
    text-decoration: underline;
  }
  </style>
  