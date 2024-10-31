<template>
  <div>
    <h5 class="mb-2">Places Lived</h5>
    <!-- hometown section -->
    <a class="text-primary cursor-pointer plus-button mt-3" v-if="hometownBtnVisible" @click="hometownVisibleChange">
      <font-awesome-icon :icon="['fas', 'circle-plus']" />
      <span class="ms-2">Add hometown</span>
    </a>
    <!-- hometown add fields -->
    <div class="form-group mt-3" v-if="hometownFieldVisible">
      <input type="text" placeholder="Hometown" v-model="hometown.city" class="form-control">
      <span class="text-danger">{{ hometownError.city }}</span>
      <h6 class="mt-3">Audience</h6>
      <select  class="mt-2 form-control" v-model="hometown.audience">
          <option value="0">Public</option>
          <option value="1">Friends</option>
          <option value="2">Only Me</option>
      </select>
      <div class="d-flex justify-content-end mt-2">
        <button class="btn btn-secondary" @click="hometownVisibleChange">
          Cancel
        </button>
        <button class="btn btn-primary ms-2" @click="addHometown">
          Save
        </button>
      </div>
    </div>
    <!-- current city fields -->
    <a class="text-primary cursor-pointer plus-button mt-3" v-if="currentCityBtnVisible" @click="currentCityVisibleChange">
      <font-awesome-icon :icon="['fas', 'circle-plus']" />
      <span class="ms-2">Add Current City</span>
    </a>
    <!-- current city add fields -->
    <div class="form-group mt-3" v-if="currentCityFieldVisible">
      <input type="text" placeholder="Current City" v-model="currentCity.city" class="form-control">
      <span class="text-danger">{{ currentCityError.city }}</span>
      <h6 class="mt-3">Audience</h6>
      <select  class="mt-2 form-control" v-model="currentCity.audience">
          <option value="0">Public</option>
          <option value="1">Friends</option>
          <option value="2">Only Me</option>
      </select>
      <div class="d-flex justify-content-end mt-2">
        <button class="btn btn-secondary" @click="currentCityVisibleChange">
          Cancel
        </button>
        <button class="btn btn-primary ms-2" @click="addCurrentCity">
          Save
        </button>
      </div>
    </div>
    <!-- city section -->
    <a class="text-primary cursor-pointer plus-button mt-3" @click="cityAddVisibleChange">
      <font-awesome-icon :icon="['fas', 'circle-plus']" />
      <span class="ms-2">Add City</span>
    </a>
    <!-- city add fields -->
    <div class="form-group mt-3" v-if="cityAddFieldVisible">
      <input type="text" placeholder="City" v-model="city.city" class="form-control">
      <span class="text-danger">{{ cityError.city }}</span>
      <h6 class="mt-3">Moved on</h6>
        <input type="date" class="form-control" v-model="city.moved">
      <h6 class="mt-3">Audience</h6>
      <select  class="mt-2 form-control" v-model="city.audience">
          <option value="0">Public</option>
          <option value="1">Friends</option>
          <option value="2">Only Me</option>
      </select>
      <div class="d-flex justify-content-end mt-2">
        <button class="btn btn-secondary" @click="cityAddVisibleChange">
          Cancel
        </button>
        <button class="btn btn-primary ms-2" @click="addCity">
          Save
        </button>
      </div>
    </div>
    <!-- city Edit fields -->
    <div class="form-group mt-3" v-if="cityEditFieldVisible">
      <input type="text" placeholder="City" v-model="cityEdit.city" class="form-control">
      <span class="text-danger">{{ cityEditError.city }}</span>
      <h6 class="mt-3">Moved on</h6>
        <input type="date" class="form-control" v-model="cityEdit.moved">
      <h6 class="mt-3">Audience</h6>
      <select  class="mt-2 form-control" v-model="cityEdit.audience">
          <option value="0">Public</option>
          <option value="1">Friends</option>
          <option value="2">Only Me</option>
      </select>
      <div class="d-flex justify-content-end mt-2">
        <button class="btn btn-secondary" @click="cityEditClose">
          Cancel
        </button>
        <button class="btn btn-primary ms-2" @click="updateCity">
          Save
        </button>
      </div>
    </div>
    <!-- citites list section -->
    <ul>
      <li class=" mt-2" v-for="(place,index) in places" :key="place.id" style="list-style: none">
        <div class="d-flex justify-content-between">
          <div class="d-flex align-items-center">
              <div class="d-flex flex-column ">
                  <span>{{ place.city}}</span>
                  <span class="text-small text-secondary"><span v-if="place.type === 0">Hometown</span><span v-else-if="place.type === 1">Current City</span> <span v-else> Moved on {{ place.moved }}</span> </span>
              </div>
          </div>
          <div class="d-flex justify-content-end align-items-center">
            <a class="me-2 text-dark cursor-pointer" @click="loadAudience(place.id,index)">
              <font-awesome-icon v-if="place.audience =='0'" :icon="['fas', 'earth-americas']" />
              <font-awesome-icon v-if="place.audience =='1'" :icon="['fas', 'users']" />
              <font-awesome-icon v-if="place.audience =='2'" :icon="['fas', 'lock']" />
            </a>
            <div class="dropdown">
              <a  class="ms-4 text-dark cursor-pointer  rounded-circle bg-light edit-btn" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                <font-awesome-icon :icon="['fas', 'ellipsis']" />
              </a>
              <div class="dropdown-menu">
                <a v-if="place.type == '2'" class="dropdown-item" @click="loadPlace(place.id)">Edit city</a>
                <a v-if="place.type == '0'" class="dropdown-item"  @click="deleteCity(place.id)">Delete Hometown</a>
                <a v-if="place.type == '1'" class="dropdown-item"  @click="deleteCity(place.id)">Delete Current City</a>
                <a v-if="place.type == '2'" class="dropdown-item"  @click="deleteCity(place.id)">Delete City</a>
              </div>
            </div>
          </div>
          </div>
          <div class="mt-2 form-group" v-if="placesAudience[index] && placesAudience[index].isEditing">
            <h6 class="mt-3">Select Audience</h6>
      <select  class="mt-2 form-control" v-model="cityEdit.audience">
          <option value="0">Public</option>
          <option value="1">Friends</option>
          <option value="2">Only Me</option>
      </select>
      <div class="d-flex justify-content-end mt-2">
        <button class="btn btn-secondary" @click="placesAudience[index].isEditing = false">
          Cancel
        </button>
        <button class="btn btn-primary ms-2" @click="updateCity">
          Save
        </button>
        </div>
          </div>
      </li>
    </ul>
  </div>
</template>
<script>
import { computed, onMounted, reactive, ref,watch } from 'vue';
import { useStore } from 'vuex';
import axiosInstance from '@/axios';


export default {
  name: "about_places",
  setup() {
    const store = useStore();

    const hometown = reactive({
      city: "",
      type: "0",
      audience: "0",
    });

    const hometownError = reactive({ city: "" });
    const hometownFieldVisible = ref(false);

    const currentCity = reactive({
      city: "",
      type: "1",
      audience: "0",
    });

    const currentCityError = reactive({ city: "" });
    const currentCityFieldVisible = ref(false);

    const city = reactive({
      city: "",
      type: "2",
      moved: "",
      audience: "0",
    });

    const cityError = reactive({ city: "", moved: "" });
    const cityAddFieldVisible = ref(false);
    const cityEditFieldVisible = ref(false);
    const cityEdit = reactive({
      id:"",
      city:"",
      moved:"",
      type:"2",
      audience:"0"
    });
    const cityEditError = reactive({
      id:"",
      city:"",
      moved:"",

    });
    const places = computed(() => store.state.places);
    const placesAudience = ref([]);
    // Fetch places from the API and update Vuex state
    onMounted(async () => {
      const response = await axiosInstance.get('places/');
      store.commit('SET_PLACES', response.data);
   
    });
      watch(places, (newPlaces) => {
      placesAudience.value = newPlaces.map(() => ({ isEditing: false }));
      });

    // Add hometown using API call and then update Vuex state
    const addHometown = async () => {
      hometownError.city = "";
      try {
        const response = await axiosInstance.post('places/', hometown);
        store.commit('ADD_PLACE', response.data);
        hometownFieldVisible.value = false;
      } catch (err) {
        if (err.response?.data?.city) {
          hometownError.city = err.response.data.city;
        }
      }
    };

    // Add current city using API call and update Vuex state
    const addCurrentCity = async () => {
      currentCityError.city = "";
      try {
        const response = await axiosInstance.post('places/', currentCity);
        store.commit('ADD_PLACE', response.data);
        currentCityFieldVisible.value = false;
      } catch (err) {
        if (err.response?.data?.city) {
          currentCityError.city = err.response.data.city;
        }
      }
    };

    // Delete city using API call and update Vuex state
    const deleteCity = async (id) => {
      hometownFieldVisible.value = false;
      currentCityFieldVisible.value = false;
      cityAddFieldVisible.value = false;
      cityEditFieldVisible.value = false;
      placesAudience.value.map(item=>item.isEditing=false);
      try {
        await axiosInstance.delete(`places/${id}/`);
        store.commit('DELETE_PLACE', id);
      } catch {
        console.error("Some error occurred while deleting city.");
      }
    };

    // Add a new city using API call and then update Vuex state
    const addCity = async () => {
      cityError.city = "";
      cityError.moved = "";
      try {
        const response = await axiosInstance.post('places/', city);
        store.commit('ADD_PLACE', response.data);
        cityAddFieldVisible.value = false;
      } catch (err) {
        if (err.response?.data?.city) {
          cityError.city = err.response.data.city[0];
        }
        if (err.response?.data?.moved) {
          cityError.moved = err.response.data.moved[0];
        }
      }
    };

    // Update city using API call and then update Vuex state
    const updateCity = async () => {
      cityError.city = "";
      cityError.moved = "";
      try {
        const response = await axiosInstance.put(`places/${cityEdit.id}/`, cityEdit);
        store.commit('UPDATE_PLACE', response.data);
        cityEditFieldVisible.value = false;
        placesAudience.value.map(item=>item.isEditing=false);
      } catch (err) {
        if (err.response?.data?.city) {
          cityError.city = err.response.data.city[0];
        }
        if (err.response?.data?.moved) {
          cityError.moved = err.response.data.moved[0];
        }
      }
    };
    ////for opening and closing the  city
    const cityAddVisibleChange = ()=>{
      currentCityFieldVisible.value = false;
      hometownFieldVisible.value = false;
      cityEditFieldVisible.value = false;
      placesAudience.value.map(item=>item.isEditing=false);
      cityAddFieldVisible.value = !cityAddFieldVisible.value
    }
    //for opening and closing the current city
    const currentCityVisibleChange = ()=>{
      hometownFieldVisible.value = false;
      cityAddFieldVisible.value = false;
      cityEditFieldVisible.value = false;
      placesAudience.value.map(item=>item.isEditing=false);
      currentCityFieldVisible.value = !currentCityFieldVisible.value
    }
        //for opening and closing the hometown
        const hometownVisibleChange = ()=>{
      currentCityFieldVisible.value = false;
      cityAddFieldVisible.value = false;
      cityEditFieldVisible.value = false;
      placesAudience.value.map(item=>item.isEditing=false);
      hometownFieldVisible.value = !hometownFieldVisible.value
    }
        //to check that already hometown exists or not
        const hometownBtnVisible = computed(()=>{
      const hometownExists = places.value.find(item=>item.type === 0)
      if (hometownExists){
        return false;
      }
      return true;
    })
    //to check that already current city exists or not
    const currentCityBtnVisible = computed(()=>{
      const hometownExists = places.value.find(item=>item.type === 1)
      if (hometownExists){
        return false;
      }
      return true;
    });
        //to load data of city in city fields
        const loadPlace = async(id)=>{
      cityAddFieldVisible.value = false;
      hometownFieldVisible.value = false;
      currentCityFieldVisible.value = false;
      placesAudience.value.map(item=>item.isEditing=false);

      await axiosInstance.get('places/'+id).then(resp=>{
        cityEdit.city = resp.data.city
        cityEdit.moved = resp.data.moved
        cityEdit.audience = resp.data.audience
        cityEdit.id = resp.data.id
        cityEditFieldVisible.value = true;
   

      }).catch(()=>{
        console.error("Some error occured while fetching city.")
      })
    }
    const cityEditClose =()=>{
      cityEditFieldVisible.value = false;
    }
    const loadAudience = async(id,index)=>{
      cityAddFieldVisible.value = false;
      hometownFieldVisible.value = false;
      currentCityFieldVisible.value = false;
      const index_per = index
      placesAudience.value.map(item=>item.isEditing=false);
      await axiosInstance.get('places/'+id).then(resp=>{
        cityEdit.city = resp.data.city
        cityEdit.moved = resp.data.moved
        cityEdit.audience = resp.data.audience
        cityEdit.id = resp.data.id
        // cityEditFieldVisible.value = true;
        placesAudience.value[index_per].isEditing = true;
     

      }).catch(()=>{
        console.error("Some error occured while fetching city.")
      })
    }
    return {
      hometown,
      hometownError,
      hometownFieldVisible,
      addHometown,
      places,
      deleteCity,
      currentCity,
      currentCityError,
      currentCityFieldVisible,
      addCurrentCity,
      city,
      cityError,
      cityAddFieldVisible,
      addCity,
      updateCity,
      cityAddVisibleChange,
      hometownVisibleChange,
      currentCityBtnVisible,
      hometownBtnVisible,
      currentCityVisibleChange,
      loadPlace,
      cityEdit,
      cityEditFieldVisible,
      cityEditError,
      cityEditClose,
      placesAudience,
      loadAudience
    };
  },
};

</script>
<style scoped>
.edit-btn{
padding: 5px 10px ;
}
.edit-btn:hover{
  opacity: 0.8;
}
</style>