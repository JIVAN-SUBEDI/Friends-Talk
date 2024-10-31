<template>
  <div>
    <navbar />
    <div class="bg-light" style="min-height:calc(100vh - 80px);">
      <div class="container bg-light p-3">
        <h4 class="p-3">Friend Requests</h4>
        <div class="row g-3">
          <div class="col-md-3" v-for="user in requests" :key="user.id">
            <div class="card border-0">
              <div class="card-body">
                <img
                  :src="
                    user.sender.profile_image
                      ? user.sender.profile_image
                      : require('@/assets/img/default-profile.jpg')
                  "
                  alt=""
                  class="image-request rounded"
                />
                <div class="d-flex flex-column mt-2">
                  <h6>
                    {{ user.sender.first_name }} {{ user.sender.last_name }}
                  </h6>
                  <span
                    class="text-small text-secondary"
                    v-if="user.mutual_friend_count > 0"
                    >{{ user.mutual_friend_count }} Mutual Friends</span
                  >
                </div>
                <div class="d-flex flex-column mt-2">
                  <button
                    class="btn btn-primary"
                    @click="acceptRequest(user.sender.id)"
                  >
                    Accept
                  </button>
                  <button
                    class="btn btn-danger mt-2"
                    @click="rejectRequest(user.sender.id)"
                  >
                    Reject
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div v-if="requests && requests.length === 0" class="col-12">
            <div class="alert alert-info text-center">
              No friend requests available.
            </div>
          </div>
        </div>
        <h4 class="p-3">People you may Know</h4>
        <div class="row g-3">
          <div class="col-md-3" v-for="people in people" :key="people.id">
            <div class="card border-0">
              <div class="card-body">
                <img
                :src="
                    people.profile_image
                      ? people.profile_image
                      : require('@/assets/img/default-profile.jpg')
                  "
                  alt=""
                  class="image-request rounded"
                />
                <div class="d-flex flex-column mt-2">
                  <h6>{{ people.first_name }} {{ people.last_name }}</h6>
                  <span class="text-small text-secondary" v-if="people.mutual_friend_count > 0"
                    >{{ people.mutual_friend_count }} Mutual Friends</span
                  >
                </div>
                <div class="d-flex flex-column mt-2">
                  <button class="btn btn-primary" v-if="people.status == 'Not Friends'" @click="addFriend(people.id)"><font-awesome-icon :icon="['fas', 'user-plus']" /> <span class="ms-1">Add Friend</span></button>
                  <button class="btn btn-danger mt-2" v-else-if="people.status == 'Request Sent'" @click="deleteRequest(people.id)"><font-awesome-icon :icon="['fas', 'trash']" /> <span class="ms-1">Delete Request</span></button>
                  
                </div>
              </div>
            </div>
          </div>
          <div v-if="people && people.length === 0" class="col-12">
            <div class="alert alert-info text-center">
              No people you may know available.
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { onMounted, ref } from "vue";
import navbar from "./partials/navbar.vue";
import axiosInstance from "@/axios";
export default {
  name: "friend_request",
  components: { navbar },
  setup() {
    const requests = ref();
    const people = ref();
    onMounted(async () => {
      await axiosInstance
        .get("friend-request/")
        .then((resp) => {
          requests.value = resp.data;
        })
        .catch(() => {
          console.error("some error occured while fetching friend requests!");
        });
      await axiosInstance
        .get("people-you-may-know/")
        .then((resp) => {
          people.value = resp.data

        })
        .catch(() => {
          console.error("some error occured while fetching people you may know!");
        });
        
    });
    // Function to reject a received friend request
    const rejectRequest = async (id) => {
      await axiosInstance.get(`friend-request/reject/${id}/`).then(() => {
        requests.value = requests.value.filter((user) => user.sender.id != id);
      }).catch(()=>{
        console.error("some error occured while rejecting request!");
      });
    };

    // Function to accept a received friend request
    const acceptRequest = async (id) => {
      await axiosInstance.get(`friend-request/accept/${id}/`).then(() => {
        requests.value = requests.value.filter((user) => user.sender.id != id);
      }).catch(()=>{
        console.error("some error occured while accepting request!");
      });
    };
    const addFriend = async (id) => {
      await axiosInstance.get(`friend-request/send/${id}/`).then(() => {
      
        const status = 'Request Sent';
        const changeStatus = people.value.find(user=>user.id === id);
        if(changeStatus){
          changeStatus.status = status;
        }

      }).catch(()=>{
        console.error("some error occured while addubg friend!");
      });
    };
    const deleteRequest = async (id) => {
      await axiosInstance.get(`friend-request/delete/${id}/`).then(() => {
        const status = 'Not Friends';
        const changeStatus = people.value.find(user=>user.id === id);
        if(changeStatus){
          changeStatus.status = status;
        }

        
      }).catch(()=>{
        console.error("some error occured while deleting request!");
      });
    };
    return { requests, acceptRequest, rejectRequest,people,addFriend,deleteRequest };
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
