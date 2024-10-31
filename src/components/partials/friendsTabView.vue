<template>
  <div class="card border-0">
    <div class="card-body">
      <h5>Friends</h5>
      <div class="d-flex justify-content-between mt-3">
        <div class="search">
          <span class="search-icon">
            <font-awesome-icon :icon="['fas', 'magnifying-glass']" />
          </span>
          <input 
            type="text" 
            placeholder="Search Friends"
            v-model="searchQuery" 
          />
        </div>
      </div>
      <div class="row g-3 mt-3">
        <div class="col-md-6" v-for="friend in filteredFriends" :key="friend.id">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between align-items-center">
                <div class="d-flex align-items-center">
                  <img
                    :src="friend.details?.profile_image || require('@/assets/img/default-profile.jpg')"
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>{{ friend.details?.first_name }} {{ friend.details?.last_name }}</h5>
                    <span class="text-secondary text-small" v-if="friend.status === 'Friend'">
                      Friend
                    </span>
                    <span class="text-secondary text-small" v-else-if="friend.mutual_friends_count > 0">
                      {{ friend.mutual_friends_count }} Mutual Friends
                    </span>
                  </div>
                </div>
                <button 
                  class="btn btn-primary" 
                  @click="addFriend(friend.details?.id)" 
                  v-if="friend.status === 'Not Friends'"
                >
                  <font-awesome-icon :icon="['fas', 'user-plus']" />
                  <span class="ms-2">Add Friend</span>
                </button>
                <button 
                  class="btn btn-danger" 
                  @click="deleteRequest(friend.details?.id)" 
                  v-if="friend.status === 'Request Sent'"
                >
                  <font-awesome-icon :icon="['fas', 'trash']" />
                  <span class="ms-2">Delete Request</span>
                </button>
                <div v-if="friend.status === 'Request Received'" class="d-flex gap-3">
                  <button class="btn btn-primary" @click="acceptRequest(friend.details?.id)">Accept</button>
                  <button class="btn btn-danger" @click="rejectRequest(friend.details?.id)">Reject</button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <!-- Message if no friends found -->
        <div v-if="filteredFriends.length === 0 && searchQuery != ''" class="col-12">
            <div class="alert alert-info">No friends found matching your search.</div>
          </div>
          <div v-if="filteredFriends.length === 0 && searchQuery == ''" class="col-12">
            <div class="alert alert-info">No friends available.</div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from '@/axios'; 
import { computed, ref } from 'vue'; 
import { useStore } from 'vuex'; 

export default {
  name: "friends_tab", 
  
  setup() {
    const store = useStore(); 
    const searchQuery = ref(''); 
   
    // Computed property to filter friends based on search query
    const filteredFriends = computed(() => {
      // Safeguard against undefined or null friends array
      const friendsList = Array.isArray(store.state.userProfile.friends) ? store.state.userProfile.friends : [];
      return friendsList.filter(friend => {
        // Create a full name string for comparison
        const fullName = `${friend.details?.first_name || ''} ${friend.details?.last_name || ''}`.toLowerCase();
        // Return friends whose names include the search query
        return fullName.includes(searchQuery.value.toLowerCase());
      });
    });

    // Function to send a friend request
    const addFriend = async (id) => {
      await axiosInstance.get(`friend-request/send/${id}/`).then(() => {
        const status = 'Request Sent'; // Update status after sending request
        store.commit('UPDATE_FRIEND_USER_STATUS', { id, status }); // Commit the status change to the store
      });
    };

    // Function to delete a sent friend request
    const deleteRequest = async (id) => {
      await axiosInstance.get(`friend-request/delete/${id}/`).then(() => {
        const status = 'Not Friends'; // Update status after deleting request
        store.commit('UPDATE_FRIEND_USER_STATUS', { id, status }); // Commit the status change to the store
      });
    };

    // Function to reject a received friend request
    const rejectRequest = async (id) => {
      await axiosInstance.get(`friend-request/reject/${id}/`).then(() => {
        const status = 'Not Friends'; // Update status after rejecting request
        store.commit('UPDATE_FRIEND_USER_STATUS', { id, status }); // Commit the status change to the store
      });
    };

    // Function to accept a received friend request
    const acceptRequest = async (id) => {
      await axiosInstance.get(`friend-request/accept/${id}/`).then(() => {
        const status = 'Friend'; // Update status after accepting request
        store.commit('UPDATE_FRIEND_USER_STATUS', { id, status }); // Commit the status change to the store
      });
    };

    // Return reactive properties and methods to the template
    return {
      searchQuery,
      filteredFriends,
      addFriend,
      acceptRequest,
      rejectRequest,
      deleteRequest
    };
  }
};
</script>

<style scoped>
.search {
  position: relative;
  height: 100%;
}
.search input {
  height: 45px;
  width: 25rem;
  border-radius: 45px;
  outline: none;
  border: none;
  background: #f2f2f2;
  padding-left: 3rem;
}
.search-icon {
  position: absolute;
  top: calc(22.5px - 0.6rem);
  left: 0.8rem;
  color: #636c72;
}
.text-small {
  font-size: 0.9rem;
}
</style>
