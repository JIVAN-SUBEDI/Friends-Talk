<template>
  <div>
    <div class="card border-0 mt-3">
      <div class="card-body">
        <div class="row">
          <div class="col d-flex justify-content-end">
            <img
              :src="
                user.profile_image
                  ? user.profile_image
                  : require('@/assets/img/default-profile.jpg')
              "
              class="rounded-circle border"
              width="60px"
              height="60px"
            />
          </div>
          <div class="col-10">
            <button
              class="create-post-btn"
              data-bs-toggle="modal"
              data-bs-target="#addPost"
            >
              What's on you mind, {{ user.first_name }}?
            </button>
          </div>
        </div>
        <hr />
        <div class="d-flex justify-content-between">
          <button class="btn btn-custom" @click="photoBtnClick">
            <font-awesome-icon
              :icon="['fas', 'image']"
              class="text-success me-2"
            /><span> Photo</span>
          </button>
          <button
            class="btn btn-custom"
            data-bs-toggle="modal"
            data-bs-target="#feeling"
          >
            <font-awesome-icon
              :icon="['fas', 'face-smile']"
              class="text-warning me-2"
            /><span> Feeling</span>
          </button>
          <button
            class="btn btn-custom"
            data-bs-toggle="modal"
            data-bs-target="#activity"
          >
            <font-awesome-icon
              :icon="['fas', 'person-running']"
              class="text-secondary me-2"
            /><span> Activity</span>
          </button>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="addPost"
      tabindex="-1"
      role="dialog"
      aria-labelledby="add post"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header d-flex justify-content-between">
            <h5 class="modal-title">Create Post</h5>
            <button
              type="button"
              class="close btn"
              data-bs-dismiss="modal"
              aria-label="Close"
            >
              <font-awesome-icon :icon="['fas', 'xmark']" />
            </button>
          </div>
          <div class="modal-body">
            <div class="post-header d-flex align-items-center">
              <div class="d-flex align-items-center">
                <img
                  :src="
                    user.profile_image
                      ? user.profile_image
                      : require('@/assets/img/default-profile.jpg')
                  "
                  alt=""
                  class="rounded-circle border me-2"
                  width="50px"
                  height="50px"
                />
                {{ user.first_name + " " + user.last_name }}
              </div>
              <span v-if="actions.activity && actions.subActivity"
                >&ThickSpace;is {{ actions.activity }}
                {{ actions.subActivity }}.
              </span>
              <span v-if="actions.feeling"
                >&ThickSpace;is feeling {{ actions.feeling }}.
              </span>
            </div>
            <div class="mt-3">
              <textarea
                style="resize: none"
                class="custom-texarea"
                cols="30"
                rows="10"
                placeholder="What's on your mind, Jivan?"
                v-model="post.content"
              ></textarea>
              <div
                class="card rounded mb-2 mt-2"
                v-if="images.length <= 0 && showAddPhotoField"
              >
                <div class="card-body">
                  <div class="d-flex justify-content-end">
                    <button class="btn" @click="showAddPhotoField = false">
                      <font-awesome-icon :icon="['fas', 'xmark']" />
                    </button>
                  </div>
                  <a
                    class="bg-light btn d-flex justify-content-center align-items-center addBtn text-decoration-none text-black"
                    @click="uploadPhoto"
                  >
                    <font-awesome-icon
                      :icon="['fas', 'image']"
                      class="me-2"
                      style="font-size: 1.2rem"
                    />
                    <span>Add photos</span>
                  </a>
                </div>
              </div>
              <input
                type="file"
                id="uploadFileInput"
                style="display: none"
                @change="handleFileChange($event)"
                accept="image/*"
                multiple
              />
              <div
                v-if="images.length"
                class="image-gallery mb-2 mt-2"
                :class="{ 'multiple-image': imageContainerClass }"
              >
                <button @click="uploadPhoto" class="btn bg-white shadow">
                  <font-awesome-icon
                    :icon="['fas', 'image']"
                    class="me-2"
                    style="font-size: 1.2rem"
                  />
                  <span>Add photos</span>
                </button>
                <a
                  @click="passImage"
                  v-for="(image, index) in images"
                  :key="image"
                  :style="{
                    height: getImageHeight + 'rem',
                    width: getImageWidth(index),
                  }"
                  class="image-container"
                >
                  <button class="text-black shadow" @click="removeImage(index)">
                    <font-awesome-icon :icon="['fas', 'xmark']" />
                  </button>
                  <img :src="image.previewUrl" class="image" />
                </a>
              </div>
            </div>
            <div
              class="border d-flex justify-content-between align-items-center ps-2 pe-2 rounded"
            >
              <div>Add to your post</div>
              <div>
                <button
                  class="btn btn-custom"
                  @click="showAddPhotoField = true"
                >
                  <font-awesome-icon
                    :icon="['fas', 'image']"
                    class="text-success me-2"
                  />
                </button>

                <button
                  class="btn btn-custom"
                  data-bs-toggle="modal"
                  data-bs-target="#feeling"
                >
                  <font-awesome-icon
                    :icon="['fas', 'face-smile']"
                    class="text-warning me-2"
                  />
                </button>

                <button
                  class="btn btn-custom"
                  data-bs-toggle="modal"
                  data-bs-target="#activity"
                >
                  <font-awesome-icon
                    :icon="['fas', 'person-running']"
                    class="text-secondary me-2"
                  />
                </button>
              </div>
            </div>
          </div>
          <div class="modal-footer d-flex">
            <button type="button" class="btn btn-primary post-btn" @click="submitPost">Post</button>
          </div>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="feeling"
      tabindex="-1"
      role="dialog"
      aria-labelledby="feelingmodal"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header d-flex justify-content-between">
            <h5 class="modal-title">How are you feeling?</h5>
            <button
              type="button"
              class="close btn"
              data-bs-dismiss="modal"
              aria-label="Close"
            >
              <font-awesome-icon :icon="['fas', 'xmark']" />
            </button>
          </div>
          <div class="modal-body">
            <div class="search">
              <span class="search-icon"
                ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
              /></span>
              <input
                type="text"
                placeholder="Search..."
                v-model="searchFeeling"
              />
            </div>
            <div class="mt-3">
              <div class="row">
                <button
                  class="btn btn-custom col-md-6 d-flex align-items-center"
                  v-for="feeling in feeling"
                  :key="feeling.id"
                  @click="feelingClick(feeling)"
                >
                  <div class="emoji me-2">
                    <span>{{ feeling.emoji }}</span>
                  </div>
                  <div>{{ feeling.name }}</div>
                </button>
                <div
                  v-if="feeling.length === 0 && searchFeeling != ''"
                  class="col-12"
                >
                  <div class="alert alert-info">
                    No feeling found matching your search.
                  </div>
                </div>
                <div
                  v-if="feeling.length === 0 && searchFeeling == ''"
                  class="col-12"
                >
                  <div class="alert alert-info">No feeling available.</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div
      class="modal fade"
      id="activity"
      tabindex="-1"
      role="dialog"
      aria-labelledby="activitymodal"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header d-flex justify-content-between">
            <button
              class="btn btn-custom"
              v-if="subActivity != ''"
              @click="backPress"
            >
              <font-awesome-icon :icon="['fas', 'arrow-left']" />
            </button>
            <h5 class="modal-title">What are you doing?</h5>
            <button
              type="button"
              class="close btn"
              data-bs-dismiss="modal"
              aria-label="Close"
            >
              <font-awesome-icon :icon="['fas', 'xmark']" />
            </button>
          </div>
          <div class="modal-body">
            <div class="search" v-if="subActivity == ''">
              <span class="search-icon"
                ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
              /></span>
              <input
                type="text"
                placeholder="Search..."
                v-model="searchActivity"
              />
            </div>
            <div v-else>
              <button class="btn btn-custom"></button>
            </div>
            <div class="mt-3">
              <div class="row" v-if="subActivity == ''">
                <button
                  class="btn btn-custom col d-flex align-items-center"
                  v-for="activity in activity"
                  :key="activity.id"
                  @click="activityClick(activity)"
                >
                  <div class="emoji me-2">
                    <span>{{ activity.emoji }}</span>
                  </div>
                  <div>{{ activity.name }}</div>
                </button>
                <div
                  v-if="activity.length === 0 && searchActivity != ''"
                  class="col-12"
                >
                  <div class="alert alert-info">
                    No activity found matching your search.
                  </div>
                </div>
                <div
                  v-if="activity.length === 0 && searchActivity == ''"
                  class="col-12"
                >
                  <div class="alert alert-info">No activity available.</div>
                </div>
              </div>
              <div class="row" v-else>
                <button
                  class="btn btn-custom col d-flex align-items-center"
                  v-for="activity in subActivity"
                  :key="activity.id"
                  @click="subActivityClick(activity)"
                >
                  <div class="emoji me-2">
                    <span>{{ activity.emoji }}</span>
                  </div>
                  <div>{{ activity.name }}</div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-if="isLoading" class="loading-circle">
      <div class="spinner"></div>
      <p>Posting...</p>
    </div>
  </div>
</template>
<script>
import { computed, onMounted, reactive, ref } from "vue";
import { useStore } from "vuex";
import { Modal } from "bootstrap";
import axiosInstance from "@/axios";
import { useToast } from "vue-toastification";

export default {
  name: "create_post",
  setup() {
    const store = useStore();
    const toast = useToast();
    const user = computed(() => store.state.user);
    const searchFeeling = ref("");
    const searchActivity = ref("");
    const subActivity = ref([]);
    const createPostModal = ref(null);
    const feelingModal = ref(null);
    const activityModal = ref(null);
    const friends = ref([]);
    const images = ref([]);
    const isLoading = ref(false);
    const showAddPhotoField = ref(false);
    const imageContainerClass = computed(() => {
      const imageCount = images.value.length;
      return imageCount > 1;
    });
    const post = reactive({
      activity: "",
      sub_activity: "",
      feeling: "",
      content: "",
      images: [],
    });
    const actions = reactive({
      feeling: "",
      activity: "",
      subActivity: "",
    });
    const fileInput = ref(null);
    onMounted(async () => {
      fileInput.value = document.querySelector("#uploadFileInput");
      createPostModal.value = new Modal(document.querySelector("#addPost"));
      feelingModal.value = new Modal(document.querySelector("#feeling"));
      activityModal.value = new Modal(document.querySelector("#activity"));
      await axiosInstance
        .get("friends/")
        .then((resp) => {
          friends.value = resp.data;
        })
        .catch(() => {
          console.error("some error occured while fetching friend!");
        });
    });
    const feeling = computed(() => {
      const feelingList = Array.isArray(store.state.feeling)
        ? store.state.feeling
        : [];

      return feelingList.filter((feeling) => {
        return feeling.name
          .toLowerCase()
          .includes(searchFeeling.value.toLowerCase());
      });
    });
    const activity = computed(() => {
      const activityList = Array.isArray(store.state.activity)
        ? store.state.activity
        : [];

      return activityList.filter((activity) => {
        return activity.name
          .toLowerCase()
          .includes(searchActivity.value.toLowerCase());
      });
    });
    const activityClick = (data) => {
      post.activity = data.id;
      subActivity.value = data.subActivity;
      actions.activity = data.name;
      actions.feeling = "";
      post.feeling = "";
    };
    const backPress = () => {
      subActivity.value = [];
      post.activity = "";
      actions.activity = "";
    };
    const feelingClick = (data) => {
      post.feeling = data.id;
      actions.feeling = data.name;
      actions.activity = "";
      post.activity = "";
      actions.subActivity = "";
      post.sub_activity = "";
      feelingModal.value.hide();
      createPostModal.value.show();
    };
    const subActivityClick = (data) => {
      post.sub_activity = data.id;
      post.feeling = "";
      actions.feeling = "";
      actions.subActivity = data.name;
      activityModal.value.hide();
      createPostModal.value.show();
    };

    const getImageHeight = computed(() => {
      const imageCount = images.value.length;
      if (imageCount > 1) {
        if (imageCount > 6) {
          const divider = Math.ceil(imageCount / 3);
          return 30 / Math.ceil(imageCount / divider);
        }
        return 30 / Math.ceil(imageCount / 2);
      } else {
        return 30;
      }
    });

    const getImageWidth = (index) => {
      const imageCount = images.value.length;
      if (imageCount > 6) {
        const divider = Math.ceil(imageCount / 3);
        const imagecalc =
          imageCount - Math.floor(imageCount / divider) * divider;
        if (index >= imageCount - imagecalc) {
          if (imageCount % divider) {
            return `calc(${100 / imagecalc}% - 10px)`;
          }
        }
        return `calc(${100 / divider}% - 10px)`;
      } else {
        if (index === imageCount - 1) {
          if (imageCount % 2 !== 0) {
            return "100%";
          }
        }
      }
    };
    const uploadPhoto = () => {
      fileInput.value.click();
    };
    const handleFileChange = (e) => {
      const files = e.target.files;
      for (const file of files) {
        // Check if the image is already in the images array by comparing name and size
        const isDuplicate = images.value.some(
          (image) =>
            image.file.name === file.name && image.file.size === file.size
        );

        if (!isDuplicate) {
          const reader = new FileReader();
          reader.onload = (e) => {
            images.value.push({ file, previewUrl: e.target.result });
          };
          reader.readAsDataURL(file); // Convert file to base64 URL for preview
        }
      }
    };

    const removeImage = (index) => {
      images.value.splice(index, 1); // Remove the selected image
    };
    const photoBtnClick = () => {
      showAddPhotoField.value = true;
      createPostModal.value.show();
    };
    const submitPost = async () => {
    // Create FormData instance
    const formData = new FormData();

    // Append other fields to FormData
    formData.append('content', post.content);
    formData.append('activity', post.activity);
    formData.append('sub_activity', post.sub_activity);
    formData.append('feeling', post.feeling);

    // Append images to FormData with the same key
    images.value.forEach((image) => {
      console.log(image)
        formData.append('images', image.file);  // 'images' should match the backend field name
    });

    isLoading.value = true;

    try {
        // Send FormData via axios with the appropriate headers
        const resp = await axiosInstance.post('posts/', formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
        });

        
        isLoading.value = false;
        createPostModal.value.hide();
        post.content = "";
        post.activity = "";
        post.sub_activity = "";
        post.feeling = "";
        actions.activity = "";
        actions.subActivity = "";
        actions.feeling = "";
        post.images = [];
        images.value = [];
        store.commit('ADD_POST_SELF',resp.data)

    } catch (error) {
        isLoading.value = false;
        toast.error('An error occurred while submitting your post. Please try again shortly.', { timeout: 5000 });

    }
};

    return {
      user,
      feeling,
      activity,
      searchFeeling,
      searchActivity,
      subActivity,
      activityClick,
      backPress,
      post,
      feelingClick,
      subActivityClick,
      actions,
      friends,
      getImageHeight,
      getImageWidth,
      images,
      imageContainerClass,
      uploadPhoto,
      handleFileChange,
      removeImage,
      showAddPhotoField,
      photoBtnClick,
      isLoading,
      submitPost
    };
  },
};
</script>
<style scoped>
img {
  object-fit: cover;
}
.create-post-btn {
  width: 100%;
  height: 50px;
  border: none;
  border-radius: 25px;
  text-align: left;
  padding-left: 2rem;
}
.addBtn {
  height: 100px;
}
.btn-custom {
  outline: none;
  /* color: #b4b4b4; */
}
.btn-custom svg {
  font-size: 1.3rem;
}
.btn-custom:hover {
  background: #f2f2f2;
}
.text-success {
  color: rgb(17, 206, 17) !important;
}
.custom-texarea {
  width: 100%;
  height: 10rem;
  border: none;
  outline: none;
  font-size: 1.2rem;
}
.post-btn {
  width: 100%;
}
.search {
  position: relative;
}
.search input {
  height: 45px;
  width: 100%;
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
.emoji {
  height: 40px;
  width: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 50%;
  background: #f2f2f2;
  font-size: 1.1rem;
}
.image-gallery {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  position: relative;
}
.image-gallery a {
  width: 100%;
}
.image-gallery.multiple-image a {
  width: calc(50% - 5px);
}
.image {
  width: 100%;
  object-fit: cover;
  height: 100%;
}
.image-container {
  position: relative;
  top: 0;
  left: 0;
}
.image-container button {
  position: absolute;
  top: 4%;
  right: 4%;
  cursor: pointer;
  border-radius: 50%;
  background: white;

  width: 20px;
  height: 20px;
  border: none;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 0.8rem;
}
.image-container button:hover {
  opacity: 0.8;
}
.image-gallery .btn {
  position: absolute;
  left: 4%;
  top: 20px;
  z-index: 100;
}
.loading-circle {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100vw;
  background: rgba(255, 255, 255, 0.8);
  z-index: 1060;
  flex-direction: column;
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-left-color: #4e9af1;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
