<template>
  <div class="card border-0">
    <div class="card-body">
      <h5>Friends</h5>
      <div class="d-flex justify-content-between mt-3">
        <div class="search">
          <span class="search-icon"
            ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
          /></span>
          <input type="text" placeholder="Search Friends"  v-model="searchQuery" />
        </div>
        <router-link to="/friends/request" class="text-decoration-none">Friend Request</router-link>
      </div>
      <div class="row g-3 mt-3">
        <div class="col-md-6" v-for="friend in filteredFriends" :key="friend.id">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between">
                <div class="d-flex align-items-center">
                  <img
                  :src="friend.details?.profile_image || require('@/assets/img/default-profile.jpg')"
                  alt=""
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>{{ friend.details.first_name }} {{ friend.details.last_name }}</h5>
                    <span class="text-secondary text-small"
                      >{{ friend.mutual_friends_count }} Mutual Friends</span
                    >
                  </div>
                </div>
                <div class="d-flex align-items-center">
                  <button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#unfriend" @click="unfriendClick(friend)">
                    <font-awesome-icon :icon="['fas', 'user-xmark']" />
                  </button>
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
    <div class="modal fade" id="unfriend" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title">Unfriend {{friend  }}</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Are you sure you want to {{ friend }} as your friend?</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-primary" @click="unfriend">Yes</button>
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">No</button>
      </div>
    </div>
  </div>
    </div>
    <div class="modal fade" id="status" tabindex="-1" role="dialog">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>{{ message }}</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">close</button>
      </div>
    </div>
  </div>
    </div>
  </div>
  
</template>
<script>
import axiosInstance from '@/axios';
import { computed,onMounted,ref } from 'vue';
import { useStore } from 'vuex';
import { Modal } from 'bootstrap';

export default {
  name: "friends_tab",
  setup(){
    // const friends = ref();
    const store = useStore();
    const searchQuery = ref(''); 
    const unfriendModal = ref('');
    const statusModal = ref('');
    const friend = ref('');
    const message = ref('');
    const unfriendId = ref();
    // Computed property to filter friends based on search query
    const filteredFriends = computed(() => {
      // Safeguard against undefined or null friends array
      const friendsList = Array.isArray(store.state.friends) ? store.state.friends : [];

      return friendsList.filter(friend => {
        // Create a full name string for comparison
        const fullName = `${friend.details?.first_name || ''} ${friend.details?.last_name || ''}`.toLowerCase();
        // Return friends whose names include the search query
        return fullName.includes(searchQuery.value.toLowerCase());
      });
    });
    onMounted(async()=>{
      unfriendModal.value = new Modal(document.querySelector('#unfriend'))
      statusModal.value = new Modal(document.querySelector('#status'))
      await fetchFriend();

    })
    const fetchFriend = async()=>{
      await axiosInstance.get('friends/').then(resp=>{
        store.commit('SET_FRIENDS',resp.data)
      }).catch(()=>{
        console.error('some error occured while fetching friend!')
      })
    }
    const unfriendClick = (user)=>{
      friend.value = user.details.first_name +' '+user.details.last_name;
      unfriendId.value = user.id;

    }
    const unfriend = async()=>{
      await axiosInstance.delete(`friends/unfriend/${unfriendId.value}/`).then(()=>{
        message.value = `${friend.value} has been successfully removed from your friends list.`;
        unfriendModal.value.hide();
        statusModal.value.show();
        store.commit('REMOVE_FRIENDS',unfriendId.value)
        
      }).catch(()=>{
        message.value = `An error occurred while attempting to remove ${friend.value} from your friends list. Please try again later.`;
        unfriendModal.value.hide();
        statusModal.value.show();
        
      })
    }
    return {searchQuery,filteredFriends,friend,unfriendClick,unfriend,message}
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
