<template>
  <div class="card mt-3 border-0">
    <div class="card-body">
      <div class="post-header d-flex align-items-center">
        <div class="d-flex align-items-center" v-if="post && post.user_details">
          <router-link :to="'/profile/view/'+ post.user_details.id" class="text-black linkpost">
          <img
            :src="
              post.user_details.profile_image
                ? post.user_details.profile_image
                : require('@/assets/img/default-profile.jpg')
            "
            alt=""
            class="rounded-circle border me-2"
            width="50px"
            height="50px"
          />
          </router-link>
          <div class="d-flex flex-column">
            <span>
              <router-link :to="'/profile/view/'+ post.user_details.id" class="text-black linkpost">

                {{
                  post.user_details.first_name + " " + post.user_details.last_name
                }}
                </router-link>
              
              <span v-if="post.feeling"
                >&ThickSpace;Is {{ post.feeling_details.name }}
                {{ post.feeling_details.emoji }}
              </span>
              <span v-if="post.activity && post.sub_activity"
                >&ThickSpace;Is {{ post.activity_details.name }}
                {{ post.activity_details.subActivity[0].name }}
                {{ post.activity_details.subActivity[0].emoji }}</span
              >
              <span v-if="post.shared_post"> shared a post</span>
            </span>
            <span class="text-secondary"> {{ post.time_ago }} </span>
          </div>
        </div>
      </div>
      <div class="mt-4">
        <div
          :class="{ 'text-truncate-after-8': !expanded }"
          ref="textContainer"
        >
          {{ post.content }}
        </div>
        <!-- Conditionally render the button based on text overflow -->
        <a v-if="isOverflowing" href="#" @click.prevent="toggleText">
          {{ expanded ? "See Less" : "See More" }}
        </a>
       
      </div>

      <div
        class="image-gallery"
        :class="{ 'multiple-image': imageContainerClass }"
      >
        <a
          @click="passImage(index)"
          data-bs-toggle="modal"
          data-bs-target="#imageModal"
          v-for="(image, index) in post.images"
          :key="image.id"
          :style="{
            height: getImageHeight + 'rem',
            width: getImageWidth(index),
          }"
        >
          <img :src="image.image" class="image" />
        </a>
      </div>
      <div class="mt-3" v-if="post.shared_post">
          <sharedPost :post="post.shared_post_details" :depth="0" :maxDepth="5"/>
        </div>
      <div class="d-flex justify-content-between mt-2">
        <div class="like-show">
          <font-awesome-icon :icon="['fas', 'thumbs-up']" />
          <span class="ms-2">{{ post.likes_count }}</span>
        </div>
        <div class="comment-share-show" v-if="post.comments">
          <font-awesome-icon :icon="['fas', 'comment']" class="ms-3" />
          <span class="ms-2">{{ post.comments.length }}</span>
          <font-awesome-icon :icon="['fas', 'share']" class="ms-3" />
          <span class="ms-2">{{ post.share_count }}</span>
        </div>
      </div>
      <hr />
      <div class="d-flex justify-content-between ps-2 pe-2">
        <a
          class="d-flex align-items-center nav-link"
          :class="{ active: post.liked }"
          @click="likePost"
        >
          <font-awesome-icon :icon="['fas', 'thumbs-up']" />
          <span class="ms-2">Like</span>
        </a>
        <a
          class="d-flex align-items-center nav-link"
          data-bs-toggle="modal"
          data-bs-target="#comment"
          @click="passComments"
        >
          <font-awesome-icon :icon="['fas', 'comment']" />
          <span class="ms-2">Comment</span>
        </a>
        <a
          class="d-flex align-items-center nav-link"
          data-bs-toggle="modal"
          data-bs-target="#share"
          @click="sharePost"
        >
          <font-awesome-icon :icon="['fas', 'share']" />
          <span class="ms-2">Share</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import axiosInstance from "@/axios";
import sharedPost from "./sharedPost.vue";
import { ref, onMounted, computed } from "vue";
import { useStore } from "vuex";

export default {
  name: "post_card",
  props: ["post"],
  components:{sharedPost},
  setup(props) {
    const store = useStore();
    const expanded = ref(false);
    const textContainer = ref(null);
    const isOverflowing = ref(false);

    const checkOverflow = () => {
      const el = textContainer.value;
      const lineHeight = parseFloat(window.getComputedStyle(el).lineHeight);
      const maxHeight = lineHeight * 8;
      isOverflowing.value = el.scrollHeight > maxHeight;
    };

    onMounted(async () => {
      checkOverflow();
    });

    const toggleText = () => {
      expanded.value = !expanded.value;
    };
   

    const imageContainerClass = computed(() => {
      const imageCount = props.post.images && Array.isArray(props.post.images) ? props.post.images.length : 0;
      return imageCount > 1;
    });

    const getImageHeight = computed(() => {
      const imageCount = props.post.images && Array.isArray(props.post.images) ? props.post.images.length : 0;
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
//get image height
    const getImageWidth = (index) => {
      const imageCount = props.post.images && Array.isArray(props.post.images) ? props.post.images.length : 0;
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
    

    const passImage = (index) => {

      const images = props.post.images
      store.commit('SET_IMAGES',{images,index})
      };
    const passComments = () => {

      store.commit('SET_POST',props.post);
      
    };
    const likePost = async () => {
  const id = props.post.id;

  try {
    const response = await axiosInstance.post(`posts/${id}/like/`);
    const status = response.data.liked;

    // Commit the status update to the Vuex store
    store.commit('UPDATE_LIKE', { id, status });

  } catch (error) {
    console.error('Error liking post:', error);
    // Optionally, you can notify the user if there's an error
  }
};
    const sharePost = () => {
  
      store.commit('SET_SHARE',props.post.id);
    };
 

    return {
      expanded,
      textContainer,
      isOverflowing,
      toggleText,
      getImageHeight,
      imageContainerClass,
      getImageWidth,
      passImage,
      likePost,
      passComments,
      sharePost,
   
  
    };
  },
};
</script>

<style scoped>
.text-secondary {
  font-size: 0.9rem;
}
.text-truncate-after-8 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 8;
  overflow: hidden;
}
.image-gallery {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
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
.like-show svg,
.comment-share-show svg,
.nav-link svg {
  font-size: 1.1rem;
}
.like-show,
.comment-share-show {
  color: #636c72;
}
.nav-link {
  cursor: pointer;
  color: #636c72;
}
.nav-link.active {
  color: #24a0ed;
}
.linkpost{
  text-decoration: none;
}
.linkpost:hover{
  text-decoration: underline;
}
</style>
