<template>
  <div>
  <div class="modal fade" id="imageModal" tabindex="-1" role="dialog">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-body">
          <div
            class="d-flex justify-content-between align-items-center ps-2 pe-2 header-modal"
          >
            <a data-bs-dismiss="modal">
              <font-awesome-icon :icon="['fas', 'xmark']" />
            </a>
            <div class="row gx-10">
              <a class="col" @click="zoomIn">
                <font-awesome-icon :icon="['fas', 'magnifying-glass-plus']" />
              </a>
              <a class="col" @click="zoomOut">
                <font-awesome-icon :icon="['fas', 'magnifying-glass-minus']" />
              </a>
            </div>
          </div>
          <div class="row main-modal">
            <div class="col d-flex align-items-center justify-content-center">
              <a
                class="btn-custom"
                @click="imageChangeLeft"
                :class="{ hide: currentIndex === 0 }"
              >
                <font-awesome-icon :icon="['fas', 'chevron-left']" />
              </a>
            </div>
            <div class="col-8 d-flex align-items-center justify-content-center">
              <div
                class="image-container"
                @mousedown="startDrag"
                @mouseup="endDrag"
                @mousemove="drag"
                @mouseleave="endDrag"
              >
                <img
                  :src="imageShow"
                  :style="{
                    transform: `scale(${scale})`,
                    left: `${position.x}px`,
                    top: `${position.y}px`,
                  }"
                  alt=""
                />
              </div>
            </div>
            <div class="col d-flex align-items-center justify-content-center">
              <a
                class="btn-custom"
                @click="imageChangeRight"
                :class="{ hide: currentIndex === images.length - 1 }"
              >
                <font-awesome-icon :icon="['fas', 'chevron-right']" />
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="comment"
    tabindex="-1"
    role="dialog"
    aria-labelledby="add post"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered modal-lg" role="document">
      <div class="modal-content">
        <div class="modal-header d-flex justify-content-between">
          <h5 class="modal-title">Comments</h5>
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
          <div class="comment-container">
          <div class="row me-3 mt-3" v-for="comments in post.comments" :key='comments.id' >
            <a class="col-1 text-decoration-none ">
              <img
              :src="comments.user_details.profile_image ? comments.user_details.profile_image : require('@/assets/img/default-profile.jpg')"                  alt=""
             
                class="rounded-circle border me-2"
                width="40px"
                height="40px"
              />
            </a>
            <div class="col bg-light rounded">
                <div class="d-flex justify-content-between"><b> {{comments.user_details.first_name}} {{comments.user_details.last_name}}</b>
                  <div class="dropdown" v-if="comments.user_details.id === user.id">
                    <a class=" btn" data-bs-toggle="dropdown"><font-awesome-icon :icon="['fas', 'ellipsis-vertical']" /></a>
                    <ul class="dropdown-menu" >
                   
                      <li><a class="dropdown-item" @click="deleteComment(comments.id)">Delete</a></li>
                    </ul>
                  </div>
                </div>
                <p> {{ comments.content }}</p>
            </div>
          </div>
          </div>
          <div class=" mt-3 row">
              <div class="col-1">
                  <img
                  :src="user.profile_image ? user.profile_image : require('@/assets/img/default-profile.jpg')"                  alt=""
                  class="rounded-circle border me-2"
                  width="40px"
                  height="40px"
                  />
                </div>
                <div class="col">
                    <div class="form-group">
                        <input
                        type="text"
                        class="form-control"
                        :placeholder="`Comment as ${user.first_name} ${user.last_name}` "
                        v-model="comment.content"
                        @keyup.enter="postComment"

                        />
                    </div>
                </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="share"
    tabindex="-1"
    role="dialog"
    aria-labelledby="add post"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header d-flex justify-content-between">
          <h5 class="modal-title">Share Post</h5>
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
              :src="user.profile_image ? user.profile_image : require('@/assets/img/default-profile.jpg')"                  
              alt=""
                class="rounded-circle border me-2"
                width="50px"
                height="50px"
              />
              <span>

                {{user.first_name}} {{user.last_name}} shared a post
              </span>
              
            </div>
            
          </div>
          <div class="mt-3">
       
            <textarea
              style="resize: none"
              class="custom-texarea"
              cols="30"
              rows="10"
              placeholder="Say something about this...."
              v-model="sharePost.content"
            ></textarea>
          </div>
          <div
            class="border d-flex justify-content-between align-items-center ps-2 pe-2 rounded"
          >
            <button class="btn btn-custom1">
              <font-awesome-icon
                :icon="['fas', 'message']"
                class="text-secondary me-2"
              /><span> Message</span>
            </button>
            <button class="btn btn-custom1">
              <font-awesome-icon
                :icon="['fas', 'users']"
                class="text-secondary me-2"
              /><span> Groups</span>
            </button>
            <button class="btn btn-custom1" @click="copyLink">
              <font-awesome-icon
                :icon="['fas', 'copy']"
                class="text-secondary me-2"
              /><span> Copy Link</span>
            </button>
          </div>
        </div>
        <div class="modal-footer d-flex">
          <button type="button" class="btn btn-primary post-btn" @click="share">Share</button>
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
import axiosInstance from "@/axios";
import { ref, onMounted, watch, reactive, computed } from "vue";
import { useStore } from "vuex";
import { useToast } from "vue-toastification";
import { Modal } from "bootstrap";

export default {
  name: "modal_section",

  setup() {
    const toast = useToast();
    const store = useStore();
    const isLoading = ref(false);
    const user = computed(()=>store.state.user)
    const sharedPost = computed(()=>store.state.share)
    const images = computed(()=>store.state.images)
    const imageIndex = computed(()=>store.state.imageIndex);
    const post = computed(()=>store.state.post);
    const sharePost = reactive({
      content:"",
      shared_post: null,
    })
    const shareModal = ref(null);
    const currentIndex = ref(0);

    const imageShow = ref(null);
    const scale = ref(1); // Initial scale is 1 (normal size)
    const position = ref({ x: 0, y: 0 });
    const isDragging = ref(false);
    const comment = reactive({
      content:"",
      shared_post:null
    });
    // Initialize the first image when component is mounted
    onMounted(() => {
      sharePost.shared_post = sharedPost.value
      shareModal.value = new Modal(document.querySelector('#share'))
      if (images.value.length > 0) {
        imageShow.value = images.value[imageIndex.value].image;
      }
      
    });

    // Watch for changes in images prop and update the displayed image accordingly
    watch(
  () => images.value  ,
  (newImages) => {
    // Ensure `newImages` is an array and contains images
    if (Array.isArray(newImages) && newImages.length > 0 && imageIndex.value < newImages.length) {
      currentIndex.value = imageIndex.value;
      imageShow.value = newImages[imageIndex.value].image;
    } else {
      // Reset `imageShow` in case of invalid `newImages` or `imageIndex`
      imageShow.value = null;
    }
    
    // Reset scale and position regardless of changes
    scale.value = 1;
    position.value = { x: 0, y: 0 };
  }
);
watch(
  imageIndex,
  (newIndex) => {

    // Check if `images` has valid entries and `newIndex` is within range
    if (Array.isArray(images.value) && images.value.length > newIndex && newIndex >= 0) {
      // Update the current index and displayed image
      currentIndex.value = newIndex;
     
      imageShow.value = images.value[newIndex].image;
    } else {
      // Handle out-of-bounds or empty array gracefully
      imageShow.value = null;
    }
    
    // Reset scale and position for the new image
    scale.value = 1;
    position.value = { x: 0, y: 0 };
  }
);

    watch(()=>sharedPost.value,(newPost)=>{
      sharePost.shared_post = newPost
    })

    const imageChangeRight = () => {
      if (currentIndex.value < images.value.length - 1) {
        currentIndex.value += 1;
        imageShow.value = images.value[currentIndex.value].image;
        scale.value = 1; // Reset scale when changing the image
        position.value = { x: 0, y: 0 }; // Reset position
      }
    };
    const imageChangeLeft = () => {
      if (currentIndex.value > 0) {
        currentIndex.value -= 1;
        imageShow.value = images.value[currentIndex.value].image;
        scale.value = 1; // Reset scale when changing the image
        position.value = { x: 0, y: 0 }; // Reset position
      }
    };

    const zoomIn = () => {
      scale.value += 0.1; // Increase scale by 0.1 on zoom in
    };

    const zoomOut = () => {
      if (scale.value > 1) {
        scale.value -= 0.1; // Decrease scale by 0.1 on zoom out
      }
    };
    const startDrag = (event) => {
      isDragging.value = true;
      event.preventDefault();
    };

    const endDrag = () => {
      isDragging.value = false;
    };

    const drag = (event) => {
      if (isDragging.value) {
        const container = event.currentTarget;
        const img = container.querySelector("img");
        const rect = img.getBoundingClientRect();
        position.value.x += event.movementX;
        position.value.y += event.movementY;

        // Prevent the image from going outside the container
        position.value.x = Math.min(
          Math.max(
            position.value.x,
            container.clientWidth - rect.width * scale.value
          ),
          0
        );
        position.value.y = Math.min(
          Math.max(
            position.value.y,
            container.clientHeight - rect.height * scale.value
          ),
          0
        );
      }
    };
    const postComment = async()=>{
   
      const id = post.value.id
      await axiosInstance.post(`posts/${id}/comment/`,comment).then(resp=>{
        const data = resp.data
       comment.content = ""
        store.commit('UPDATE_COMMENTS',{id,data})
        
      })
    }
    const deleteComment = async(cmtId)=>{
      const id = post.value.id
      await axiosInstance.delete(`comments/${cmtId}/`).then(()=>{
        store.commit('DELETE_COMMENT',{id,cmtId})

      })
    }
    const share = async()=>{
      isLoading.value = true
   
      await axiosInstance.post('posts/', sharePost).then(resp=>{
        store.commit('ADD_POST_SELF',resp.data)
        isLoading.value = false
        sharePost.content = ''
        shareModal.value.hide();
        
      }).catch(()=>{
        toast.error('An error occurred while sharing your post. Please try again shortly.', { timeout: 5000 });
      });
     
    }
    const copyLink = () =>{
      const link =  window.location.origin +'/post/'+ sharedPost.value
      navigator.clipboard.writeText(link)
        .then(() => {
          toast.success('Link copied to clipboard.',{timeout:5000})
        })
        .catch(() => {
          toast.error('Failed to copy text.',{timeout:5000})
       
        });
    }

    return {
      imageShow,
      imageChangeRight,
      imageChangeLeft,
      currentIndex,
      scale,
      zoomIn,
      zoomOut,
      startDrag,
      endDrag,
      drag,
      position,
      postComment,
      comment,
      user,
      deleteComment,
      sharePost,
      share,
      images,
      post,
      sharedPost,
      copyLink
    };
  },
};
</script>
<style scoped>
#imageModal .modal-dialog {
  margin: 0;
  padding: 0;
  height: 100vh;
  width: 100vw;

  position: absolute;
  top: 0;
  left: 0;
}
#imageModal .modal-dialog .modal-content {
  background: transparent;
  border: none;
  width: 100vw;
}
#imageModal svg {
  font-size: 1.2rem;
  color: white;
  cursor: pointer;
}
.header-modal {
  height: 2rem;
}
.main-modal {
  height: calc(100vh - 5rem);
}
.col,
.col-8 {
  height: 100%;
}
.btn-custom {
  background: #c2c6c9;
  display: flex;
  justify-content: center;
  align-items: center;
  border: none;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  cursor: pointer;
}

.btn-custom svg {
  color: rgb(39, 38, 38) !important;
}
.btn-custom:hover {
  background: #f2f2f2;
}
.main-modal img {
  height: 100%;
  width: 100%;
  object-fit: contain;
}
.hide {
  display: none;
}
.image-container {
  width: 100%;
  height: 100%;
  overflow: hidden;
  position: relative;
  cursor: grab;
}
.image-container img {
  position: absolute;
  transition: transform 0.3s ease; /* Smooth zoom transition */
}
.create-post-btn {
  width: 100%;
  height: 50px;
  border: none;
  border-radius: 25px;
  text-align: left;
  padding-left: 2rem;
}
.btn-custom1 {
  outline: none;
  display: flex;
  align-items: center;
  /* color: #b4b4b4; */
}
.btn-custom1 svg {
  font-size: 1.3rem;
}
.btn-custom1:hover {
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
.comment-container{
  max-height: 400px;
  overflow-y: auto;

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
