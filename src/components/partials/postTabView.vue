<template>
  <div>
    <div class="row">
      <div class="col-md-4">
        <div class="card border-0">
          <div class="card-body">
            <h5>Intro</h5>
            <div class="d-flex flex-column">
              <span >{{ profile.basicInfo?.bio || "No bio available" }}</span>
             
            </div>
            <div class="d-flex flex-column mt-3">
              <div class="d-flex align-items-center mt-2">
                <font-awesome-icon :icon="['fas', 'suitcase']" class="text-secondary text-big" />
                <span class="ms-3" v-if="profile.latestWorkplace">{{ profile.latestWorkplace.position }} at {{ profile.latestWorkplace.name }}</span>
                <span class="ms-3" v-else>Not yet Working</span>
              </div>
              <div class="d-flex align-items-center mt-2" v-if="profile.latestCollage && profile.latestCollage.message">
                <font-awesome-icon :icon="['fas', 'graduation-cap']" class="text-secondary text-big" />
                <span class="ms-3">{{ profile.latestCollage?.message || "" }}</span>
              </div>
              <div v-for="lived in profile.lived" :key="lived.id">

              <div class="d-flex align-items-center mt-2" v-if="lived.type==1">
                <font-awesome-icon :icon="['fas', 'location-dot']" class="text-secondary text-big" />
                <span class="ms-3">Lives in {{ lived.city }}</span>
              </div>
              </div>
              <div v-for="lived in profile.lived" :key="lived.id">

                <div class="d-flex align-items-center mt-2" v-if="lived.type==0">
                  <font-awesome-icon :icon="['fas', 'location-dot']" class="text-secondary text-big" />
                  <span class="ms-3">From {{ lived.city }}</span>
                </div>
              </div>
              <div class="d-flex align-items-center mt-2" v-if="profile.basicInfo && profile.basicInfo.relationship ">
                <font-awesome-icon :icon="['fas', 'heart']" class="text-secondary text-big" />
                <span class="ms-3">{{ profile.basicInfo.relationship || "No relationship info"}}</span>
              </div>
              <div class="d-flex align-items-center mt-2" v-if="profile.basicInfo && profile.basicInfo.primary_phone_number">
                <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big" />
                <span class="ms-3">{{ profile.basicInfo.primary_phone_number || "No phone number available" }}</span>
              </div>

              <!-- Secondary Phone Number -->
              <div class="d-flex align-items-center mt-2" v-if="profile.basicInfo && profile.basicInfo.secondary_phone_number">
                <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big" />
                <span class="ms-3">{{ profile.basicInfo.secondary_phone_number || "No secondary phone number available" }}</span>
              </div>

      
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-8">
        <mainSection :user="user" />
      </div>
    </div>
  
  </div>
</template>

<script>

import { useStore } from 'vuex';
import mainSection from './mainSection.vue';
import { computed } from 'vue';


export default {
  name: 'postTab',
  components: { mainSection },
  setup(){
    const store = useStore();
    const profile = computed(()=>store.state.userProfile);
    return {profile}
  }

};
</script>

<style scoped>
.edit-btn {
  background: #e7e4e4;
}
.edit-btn:hover {
  background: #d4d3d3;
}
svg{
  width: 25px;
  height: 25px;
}

</style>
