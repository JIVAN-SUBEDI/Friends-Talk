<template>
    <div>
      <navbar />
      <div class="bg-light" style="min-height:calc(100vh - 80px);">
        <div class="container bg-light p-3">
          <h4 class="p-3">Friends</h4>
          <div class="row g-3">
            <div class="col-md-3" v-for="user in friends" :key="user.id">
              <div class="card border-0">
                <div class="card-body">
                  <img
                    :src="
                      user.details.profile_image
                        ? user.details.profile_image
                        : require('@/assets/img/default-profile.jpg')
                    "
                    alt=""
                    class="image-request rounded"
                  />
                  <div class="d-flex flex-column mt-2">
                    <h6>
                      {{ user.details.first_name }} {{ user.details.last_name }}
                    </h6>
                    <span
                      class="text-small text-secondary"
                      v-if="user.mutual_friend_count > 0"
                      >{{ user.mutual_friend_count }} Mutual Friends</span
                    >
                  </div>
                  <div class="d-flex flex-column mt-2">
                    <button class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#unfriend" @click="unfriendClick(user)">
                    <font-awesome-icon :icon="['fas', 'user-xmark']" />
                    <span class="ms-1">Unfriend</span>
                  </button>
                  </div>
                </div>
              </div>
            </div>
            <div v-if="friends && friends.length === 0" class="col-12">
              <div class="alert alert-info text-center">
                No friends  available.
              </div>
            </div>
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
  import { computed, onMounted, ref } from "vue";
  import navbar from "./partials/navbar.vue";
  import axiosInstance from "@/axios";
  import { Modal } from "bootstrap";
  import { useStore } from "vuex";
  export default {
    name: "friends_page",
    components: { navbar },
    setup() {
    const store = useStore();
    const friends = computed(()=>store.state.friends);
    const unfriendModal = ref('');
    const statusModal = ref('');
    const friend = ref('');
    const message = ref('');
    const unfriendId = ref();
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
    return {unfriend,unfriendClick,fetchFriend,friends,friend}
    },
  };
  </script>
  <style scoped>
  .text-small {
    font-size: 0.9rem;
  }
  .image-request {
    width: 100%;
    height: 12rem;
    object-fit: cover;
  }
  </style>
  