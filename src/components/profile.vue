<template>
  <div>
    <navbarVue />
    <div class="container mt-3">
      <div class="cover-image bg-light rounded">
        <!-- Preview Image or Default Image -->
        <img v-if="previewImage" :src="previewImage" alt="Cover Photo Preview" class="rounded">
        <img v-else
        :src="selectedCoverImage ? selectedCoverImage : require('@/assets/img/default-cover.png')"
  
        alt="Default Cover Photo" class="rounded" />

        <div class="dropdown">
          <button
            class="rounded dropdown-toggle"
            type="button"
            data-bs-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <font-awesome-icon :icon="['fas', 'camera']" />
            <span>Add cover photo</span>
          </button>
          <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
            <a class="dropdown-item" data-bs-toggle="modal" data-bs-target="#images" @click="showPhoto">Choose Cover Photo</a>
            <a class="dropdown-item" @click="uploadPhoto">Upload Photo</a>
          </div>
          <input
            type="file"
            id="uploadFileInput"
            @change="handleFileChange($event)"
            accept="image/*"
            style="display: none"
          />
        </div>
      </div>
      <div class="d-flex justify-content-between ps-2 pe-2">
        <div class="d-flex align-items-center">
          <div class="image-container">
            <img v-if="previewProfile"
              :src="previewProfile"
              alt=""
            />
            <img v-else
              :src="selectedProfileImage ? selectedProfileImage : require('@/assets/img/default-profile.jpg')"
              alt=""
            />
            
            <button class="edit-btn" data-bs-toggle="modal" data-bs-target="#imagesProfile" @click="showPhoto">
              <font-awesome-icon :icon="['fas', 'camera']" />
            </button>
          </div>
          <div class="d-flex flex-column ms-3">
            <h5>
              {{ user_details.first_name + " " + user_details.last_name }}
            </h5>
            <span class="text-secondary">{{ friends }} Friends</span>
          </div>
        </div>

      </div>
      <hr />
      <ul class="nav" id="myTab" role="tablist">
        <li class="nav-item">
          <a
            class="nav-link active"
            data-bs-toggle="tab"
            href="#posts"
            role="tab"
            aria-controls="posts"
            aria-selected="true"
            >Posts</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            data-bs-toggle="tab"
            href="#about"
            role="tab"
            aria-controls="about"
            aria-selected="false"
            >About</a
          >
        </li>
        <li class="nav-item">
          <a
            class="nav-link"
            data-bs-toggle="tab"
            href="#friends"
            role="tab"
            aria-controls="friends"
            aria-selected="false"
            >Friends</a
          >
        </li>
      </ul>
      <div class="tab-content bg-light mt-3" id="myTabContent">
        <div
          class="tab-pane fade show active p-3"
          id="posts"
          role="tabpanel"
          aria-labelledby="Posts-tab"
        >
          <postTabVue />
        </div>
        <div
          class="tab-pane fade p-3"
          id="about"
          role="tabpanel"
          aria-labelledby="About-tab"
        >
          <aboutTab />
        </div>
        <div
          class="tab-pane fade p-3"
          id="friends"
          role="tabpanel"
          aria-labelledby="Friends-tab"
        >
          <friendsTabVue />
        </div>
      </div>
    </div>
    
    <!-- Modal for preview and confirmation -->
    <div class="modal fade" id="coverChange" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <p>Do you really want to change cover photo?</p>
          
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
              @click="removeCoverPhoto"
            >
              Close
            </button>
            <button
              type="button"
              class="btn btn-primary"
              @click="changeCover"
            >
              Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="profileChange" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <p>Do you really want to change profile photo?</p>
          
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
              @click="removeCoverPhoto"
            >
              Close
            </button>
            <button
              type="button"
              class="btn btn-primary"
              @click="changeProfileFromPhoto"
            >
              Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="coverChangeFromPhoto" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <p>Do you really want to change cover photo?</p>
          
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
              @click="removeCoverPhoto"
            >
              Close
            </button>
            <button
              type="button"
              class="btn btn-primary"
              @click="changeCoverFromPhoto"
            >
              Save changes
            </button>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="images" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            photos
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
          
            <div class="row g-2">
              <a class="col-md-3 choosePhoto" data-bs-toggle="modal" data-bs-target="#coverChangeFromPhoto" v-for="photo in photos" :key="photo" @click="chooseCoverFromPhoto(photo)"  >
                <img :src="photo.image" width="100%" height="100%" style="object-fit: cover;">
              </a>
            </div>
          
          </div>
  
        </div>
      </div>
    </div>
    <div class="modal fade" id="imagesProfile" tabindex="-1">
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-header">
            photos
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <div class="row g-2">
              <a class="col-md-2 choosePhoto" style="aspect-ratio: 1 / 1;" data-bs-toggle="modal" data-bs-target="#profileChange" v-for="photo in photos" :key="photo" @click="chooseProfileFromPhoto(photo)" >
                <img :src="photo.image" width="100%" height="100%" style="object-fit: cover;  ">
              </a>
            </div>
          
          </div>
          <div class="progress" v-if="loading">
            <div class="progress-bar bg-success" role="progressbar" :style="'width: '+loading+'%'" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
          <div class="modal-footer">
            <input type="file" id="uploadPhoto" style="display:none;" @change="uploadPhotoProfile($event)">
            <button class="btn btn-primary" @click="uploadPhotoClick">Upload Photo</button>
          </div>
        </div>
      </div>
    </div>
  
  </div>
</template>

<script>
import navbarVue from "./partials/navbar.vue";
import postTabVue from "./partials/postTab.vue";
import aboutTab from "./partials/aboutTab.vue";
import friendsTabVue from "./partials/friendsTab.vue";
import { computed, onMounted, ref } from "vue";
import { useStore } from "vuex";
import { Modal } from "bootstrap";
import axiosInstance from "@/axios";

export default {
  name: "profile_page",
  components: { navbarVue, postTabVue, aboutTab, friendsTabVue },
  setup() {
    const store = useStore();
    const fileInput = ref(null);
    const photoInput = ref(null);
    const coverModal = ref(null);
    const profileModal = ref(null);
    const coverModalPhoto = ref(null);
    const coverFile = ref(null);
    const profileFile = ref(null);
    const user_details = computed(() => store.state.user);
    const friends = computed(() => store.state?.friends.length || 0);
    const selectedCoverImage = computed(()=>store.state.user.cover_image);
    const selectedProfileImage = computed(()=>store.state.user.profile_image);
    const previewImage = ref(null);
    const previewProfile = ref(null);
    const photos = ref([]);
    const loading = ref(null);
    onMounted(() => {
      fileInput.value = document.querySelector("#uploadFileInput");
      photoInput.value = document.querySelector("#uploadPhoto");
      coverModal.value = new Modal(document.querySelector("#coverChange"));
      coverModalPhoto.value = new Modal(document.querySelector("#coverChangeFromPhoto"));
      profileModal.value = new Modal(document.querySelector("#profileChange"));
      store.dispatch("loadProfile");
    });
    const uploadPhoto = () => {
      fileInput.value.click();
    };
    const handleFileChange = (e) => {
      coverFile.value = e.target.files[0];
      if (coverFile.value) {
        const reader = new FileReader();
        reader.onload = (e) => {
          previewImage.value = e.target.result;
        };
        reader.readAsDataURL(coverFile.value);
        coverModal.value.show();
      }
    };
    const changeCover = async () => {
      const form = new FormData();
      form.append("cover_image", coverFile.value); // Ensure coverFile is correctly defined and assigned

      try {
        await axiosInstance.post("cover/update/", form, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });
     
        store.dispatch("loadProfileforce"); 
        
      } catch (error) {
        console.error("Error uploading cover photo:", error);
      }
     
      coverModal.value.hide();
    };
    const showPhoto =async()=>{
      await axiosInstance.get('images').then(resp=>{
        photos.value = resp.data
      }).catch(()=>{
        console.error("photo loading failed.");
      })
    }
    const removeCoverPhoto = ()=>{
      previewImage.value = "";
    }
    const chooseCoverFromPhoto = (photo)=>{
      previewImage.value = photo.image;
      coverFile.value = photo

    }
    const chooseProfileFromPhoto = (photo)=>{
      previewProfile.value = photo.image;
      profileFile.value = photo

    }
    const changeCoverFromPhoto = ()=>{
      axiosInstance.get('cover/update/'+coverFile.value.id).then(()=>{
        store.dispatch("loadProfileforce"); 
      })
      coverModalPhoto.value.hide();
   
    }
    const changeProfileFromPhoto = ()=>{
      axiosInstance.get('profile/update/'+profileFile.value.id).then(()=>{
        store.dispatch("loadProfileforce"); 
      })
      profileModal.value.hide();
   
    }
    const uploadPhotoClick = ()=>{
      photoInput.value.click();
    }
    const uploadPhotoProfile = (e)=>{
      const file = e.target.files[0]
      if (file){
        const form = new FormData();
        form.append('image',file)
        axiosInstance.post('photo/upload/',form,{
          onUploadProgress:({loaded,total})=>{
        
            loading.value = Math.floor((loaded/total)*100)
          }
        }).then(resp=>{
          photos.value.push(resp.data)
          loading.value = null;
        }).catch(()=>{
          loading.value = null;

        })
      }

    }

    return {
      user_details,
      uploadPhoto,
      handleFileChange,
      selectedCoverImage,
      changeCover,
      previewImage,
      showPhoto,
      photos,
      removeCoverPhoto,
      chooseCoverFromPhoto,
      changeCoverFromPhoto,
      selectedProfileImage,
      previewProfile,
      changeProfileFromPhoto,
      chooseProfileFromPhoto,
      uploadPhotoProfile,
      uploadPhotoClick,
      loading,
      friends
    };
  },
};
</script>
<style scoped>
.cover-image {
  height: 60vh;
  position: relative;
}
.cover-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.cover-image button {
  position: absolute;
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
  background: #f2f2f2;
}
.cover-image button svg {
  font-size: 1.1rem;
}
.image-container {
  width: 10rem;
  height: 10rem;
  border-radius: 50%;
  border: 4px solid #636c72;
  position: relative;
  top: -15%;
  background:white;
}
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}
.image-container button {
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  position: absolute;
  bottom: 0;
  right: 0.4rem;
}

.nav-link {
  border: none !important;
  color: #636c72;
}
.nav-link.active {
  border-bottom: 2px solid #24a0ed !important;
  color: #24a0ed;
}
.edit-btn {
  background: #e7e4e4;
}
.edit-btn:hover {
  background: #d4d3d3;
}
.choosePhoto{
  cursor: pointer;

}
.choosePhoto:hover{
  opacity: 0.9;
}
</style>
