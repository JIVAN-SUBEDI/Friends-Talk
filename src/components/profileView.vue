<template>
  <div>
    <navbarVue />
    <div class="container mt-3">
      <div class="cover-image bg-light rounded">
        <!-- Preview Image or Default Image -->
        <img :src="profile.cover_image ? profile.cover_image : require('@/assets/img/default-cover.png')" alt="Cover Photo Preview" class="rounded" />
      </div>
      <div class="d-flex justify-content-between ps-2 pe-2">
        <div class="d-flex align-items-center">
          <div class="image-container">
            <img 
              :src="profile.profile_image ? profile.profile_image : require('@/assets/img/default-profile.jpg')"
              alt=""
            />
          </div>
          <div class="d-flex flex-column ms-3">
            <h5>
              {{ profile.first_name + " " + profile.last_name }}
            </h5>
            <span class="text-secondary">{{ profile.friends?.length || 0 }} Friends</span>
          </div>
        </div>
        <div class="d-flex align-items-center">
          <!-- Conditional buttons based on friendship status -->
          <button class="btn edit-btn" v-if="profile.status == 'Friend'">
            <font-awesome-icon :icon="['fas', 'message']" />
            <span class="ms-2">Message</span>
          </button>
          <button class="btn btn-danger ms-2" v-if="profile.status == 'Request Sent'" @click="deleteRequest(profile.id)">
            <font-awesome-icon :icon="['fas', 'trash']" />
            <span class="ms-2">Delete Request</span>
          </button>
          <button class="btn btn-primary ms-2" v-if="profile.status == 'Not Friends'" @click="addFriend(profile.id)">
            <font-awesome-icon :icon="['fas', 'user-plus']" />
            <span class="ms-2">Add Friend</span>
          </button>
          <button class="btn btn-primary" v-if="profile.status == 'Request Received'" @click="acceptRequest(profile.id)">
            Accept
          </button>
          <button class="btn btn-danger ms-2" v-if="profile.status == 'Request Received'" @click="rejectRequest(profile.id)">
            Reject
          </button>
        </div>
      </div>
      <hr />
      <ul class="nav" id="myTab" role="tablist">
        <!-- Navigation tabs for Posts, About, and Friends -->
        <li class="nav-item">
          <a class="nav-link active" data-bs-toggle="tab" href="#posts" role="tab" aria-controls="posts" aria-selected="true">Posts</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="tab" href="#about" role="tab" aria-controls="about" aria-selected="false">About</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" data-bs-toggle="tab" href="#friends" role="tab" aria-controls="friends" aria-selected="false">Friends</a>
        </li>
      </ul>
      <div class="tab-content bg-light mt-3" id="myTabContent">
        <div class="tab-pane fade show active p-3" id="posts" role="tabpanel" aria-labelledby="Posts-tab">
          <postTabView />
        </div>
        <div class="tab-pane fade p-3" id="about" role="tabpanel" aria-labelledby="About-tab">
          <aboutTabView />
        </div>
        <div class="tab-pane fade p-3" id="friends" role="tabpanel" aria-labelledby="Friends-tab">
          <friendsTabView />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import navbarVue from './partials/navbar.vue';
import axiosInstance from '@/axios';
import postTabView from './partials/postTabView.vue';
import friendsTabView from './partials/friendsTabView.vue';
import aboutTabView from './partials/aboutTabView.vue';

export default {
  name: "profile_page", 
  components: { navbarVue, postTabView, friendsTabView, aboutTabView },
  setup() {
    const store = useStore(); 
    const profile = computed(() => store.state.userProfile); // Get user profile from Vuex

    // Function to send a friend request
    const addFriend = async (id) => {
      await axiosInstance.get(`friend-request/send/${id}/`).then(() => {
        const status = 'Request Sent'; // Update status after sending request
        store.commit('UPDATE_USER_PROFILE_STATUS', status); // Commit the status change to the store
      });
    };

    // Function to delete a sent friend request
    const deleteRequest = async (id) => {
      await axiosInstance.get(`friend-request/delete/${id}/`).then(() => {
        const status = 'Not Friends'; // Update status after deleting request
        store.commit('UPDATE_USER_PROFILE_STATUS', status); // Commit the status change to the store
      });
    };

    // Function to reject a received friend request
    const rejectRequest = async (id) => {
      await axiosInstance.get(`friend-request/reject/${id}/`).then(() => {
        const status = 'Not Friends'; // Update status after rejecting request
        store.commit('UPDATE_USER_PROFILE_STATUS', status); // Commit the status change to the store
      });
    };

    // Function to accept a received friend request
    const acceptRequest = async (id) => {
      await axiosInstance.get(`friend-request/accept/${id}/`).then(() => {
        const status = 'Friend'; // Update status after accepting request
        store.commit('UPDATE_USER_PROFILE_STATUS', status); // Commit the status change to the store
      });
    };

    return { profile, addFriend, rejectRequest, acceptRequest, deleteRequest }; // Return properties and methods to the template
  },
};
</script>

<style scoped>
.cover-image {
  height: 60vh; /* Set height for cover image section */
  position: relative;
}
.cover-image img {
  width: 100%; /* Full width for cover image */
  height: 100%; /* Full height for cover image */
  object-fit: cover; /* Maintain aspect ratio */
}
.cover-image button {
  position: absolute; /* Position buttons on cover image */
  right: 2rem;
  bottom: 2rem;
  padding: 0.5rem 1rem;
  border: none;
  background: white;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
.cover-image button:hover {
  background: #f2f2f2; /* Hover effect for buttons */
}
.cover-image button svg {
  font-size: 1.1rem;
}
.image-container {
  width: 10rem; /* Profile image size */
  height: 10rem;
  border-radius: 50%; /* Circular profile image */
  border: 4px solid #636c72; /* Border for profile image */
  position: relative;
  top: -15%; /* Adjust position */
  background: white;
}
.image-container img {
  width: 100%; /* Full size for profile image */
  height: 100%;
  object-fit: cover; /* Maintain aspect ratio */
  border-radius: 50%; /* Circular profile image */
}
.image-container button {
  border: none; /* Button styles */
  width: 40px;
  height: 40px;
  border-radius: 50%; /* Circular button */
  position: absolute;
  bottom: 0;
  right: 0.4rem;
}

.nav-link {
  border: none !important; /* Override Bootstrap styles */
  color: #636c72;
}
.nav-link.active {
  border-bottom: 2px solid #24a0ed !important; /* Active tab style */
  color: #24a0ed;
}
.edit-btn {
  background: #e7e4e4; /* Edit button background */
}
.edit-btn:hover {
  background: #d4d3d3; /* Hover effect for edit button */
}
.choosePhoto {
  cursor: pointer; /* Pointer cursor for choose photo */
}
.choosePhoto:hover {
  opacity: 0.9; /* Hover effect for choose photo */
}
</style>
