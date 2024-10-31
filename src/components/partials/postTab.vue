<template>
  <div>
    <div class="row">
      <div class="col-md-4">
        <div class="card border-0">
          <div class="card-body">
            <h5>Intro</h5>
            <div class="d-flex flex-column">
              <span v-if="!bioFieldVisible">{{ localBio.bio }}</span>
              <div class="form-group" v-if="bioFieldVisible">
                <span class="text-secondary mt-2">{{bioLength}}/255</span>
                <textarea class="form-control" style="resize: none;"  v-model="localBio.bio" maxlength="255"></textarea>
                <span class="text-danger">{{ localBioError.bio }}</span>
                <div class="d-flex justify-content-end mt-2">
                    <button class="btn btn-secondary btn-sm" @click="bioFieldVisibleChange">Cancel</button>
                    <button class="btn btn-primary btn-sm ms-2" @click="updateBio" :disabled="isLoading">
                      <span v-if="!isLoading">Save</span>
                      <span v-else>Saving...</span>
                    </button>
                </div>
              </div>
              <button class="btn edit-btn mt-2" v-if="!bioFieldVisible"  @click="bioFieldVisibleChange">Edit bio</button>
            </div>
            <div class="d-flex flex-column mt-3">
              <div class="d-flex mt-2">
                <font-awesome-icon :icon="['fas', 'suitcase']" class="text-secondary" />
                <span class="ms-2" v-if="workplace">{{ workplace.position }} at {{ workplace.name }}</span>
                <span class="ms-2" v-else>Not yet Working</span>
              </div>
              <div class="d-flex mt-2" v-if="college">
                <font-awesome-icon :icon="['fas', 'graduation-cap']" class="text-secondary" />
                <span class="ms-2">{{ college.message }}</span>
              </div>
              <div class="d-flex mt-2" v-if="currentCity">
                <font-awesome-icon :icon="['fas', 'house']" class="text-secondary" />
                <span class="ms-2">Lives in {{ currentCity.city }}</span>
              </div>
              <div class="d-flex mt-2" v-if="Hometown">
                <font-awesome-icon :icon="['fas', 'location-dot']" class="text-secondary" />
                <span class="ms-2">From {{ Hometown.city }}</span>
              </div>
              <div class="d-flex mt-2" v-if="profile.relationship">
                <font-awesome-icon :icon="['fas', 'heart']" class="text-secondary" />
                <span class="ms-2">{{ profile.relationship}}</span>
              </div>
              <div class="d-flex mt-2" v-if="profile.primary_phone_number">
                <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary" />
                <span class="ms-2">{{ profile.primary_phone_number}}</span>
              </div>
              <div class="d-flex mt-2" v-if="profile.secondary_phone_number">
                <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary" />
                <span class="ms-2">{{ profile.secondary_phone_number}}</span>
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
import { computed, watch,ref,reactive } from 'vue';
import mainSection from './mainSection.vue';
import { useStore } from 'vuex';
import axiosInstance from '@/axios';


export default {
  name: 'postTab',
  components: { mainSection },
  setup() {
    const store = useStore();
    const profile = computed(() => store.state.profile);
    const Hometown = computed(() => store.getters.getHometown);
    const currentCity = computed(() => store.getters.getCurrentCity);
    const college = computed(() => store.getters.getLatestCollege);
    const workplace = computed(() => store.getters.getCurrentOrLatestWorkplace);
    const localBio = reactive({bio:""});
    const localBioError = reactive({bio:""});
    const bioFieldVisible = ref(false);
    const bioLength = computed(()=>localBio.bio.length)
    // Watch the profile and update localBio when it changes
    watch(profile, (newProfile) => {
      if (newProfile && newProfile.bio) {
        localBio.bio = newProfile.bio;
      }
    }, { immediate: true })
    const bioFieldVisibleChange = ()=>{
      bioFieldVisible.value = !bioFieldVisible.value
      localBio.bio = profile.value.bio
    }
    const isLoading = ref(false);

const updateBio = async () => {
  isLoading.value = true;
  localBioError.bio = ""
  try {
    await axiosInstance.post('bio/update/', localBio);
    store.commit('UPDATE_BIO', localBio.bio);
    bioFieldVisible.value = false;
  } catch (error) {
    if(error.response.data.bio){
      localBioError.bio = error.response.data.bio[0]
    }
  } finally {
    isLoading.value = false;
  }
};


    return { profile,Hometown,currentCity,college,workplace,localBio,updateBio,bioFieldVisible,bioFieldVisibleChange,bioLength,isLoading,localBioError};
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
</style>
