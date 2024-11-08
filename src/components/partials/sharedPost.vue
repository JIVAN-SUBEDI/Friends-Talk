<template>
  <div class="card mt-3">
    <div class="card-body">
      <div class="post-header d-flex align-items-center">
        <div class="d-flex align-items-center">
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
                >&ThickSpace;Is
                {{ post.feeling_details.name }}
                {{ post.feeling_details.emoji }}
              </span>
              <span v-if="post.activity && post.sub_activity"
                >&ThickSpace;Is
                {{ post.activity_details.name }}
                {{ post.activity_details.subActivity[0].name }}
                {{ post.activity_details.subActivity[0].emoji }}</span
              >
              <span v-if="post.shared_post"> shared a post</span>
            </span>
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
        <div
          class="image-gallery"
          :class="{
            'multiple-image': imageContainerClass,
          }"
        >
          <a
          data-bs-toggle="modal"
          data-bs-target="#imageModal"
          v-for="(image, index) in post.images"
          :key="image.id"
          :style="{
              height: getImageHeight + 'rem',
              width: getImageWidth(index),
            }"
            @click="passImage(index)"
          >
            <img :src="image.image" class="image" />
          </a>
        </div>
        <div class="mt-3" v-if="post.shared_post">
          <sharedPost :post="post.shared_post_details" :depth="depth + 1" />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { ref, computed, onMounted } from "vue";
import { useStore } from "vuex";


export default {
  name: "shared_post",
  props: { post: {
    type: Object,
    default: () => ({}), 
    depth: {
      type: Number,
      default: 0
    },
    maxDepth: {
      type: Number,
      default: 5 // Customize the maximum depth to prevent infinite nesting
    }
  },
   },
  setup(props) {
    const store = useStore();
    const expanded = ref(false);
    const textContainer = ref(null);
    const isOverflowing = ref(false);
    const getImageHeight = computed(() => {
      const imageCount = props.post.images.length;
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
      const imageCount = props.post.images.length;
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
    const toggleText = () => {
      expanded.value = !expanded.value;
    };
    const imageContainerClass = computed(() => {
      const imageCount = props.post.images.length;
      return imageCount > 1;
    });
    const checkOverflow = () => {
      const el = textContainer.value;
      const lineHeight = parseFloat(window.getComputedStyle(el).lineHeight);
      const maxHeight = lineHeight * 8;
      isOverflowing.value = el.scrollHeight > maxHeight;
    };

    onMounted(async () => {
      checkOverflow();
    });
    const passImage = (index) => {

      const images = props.post.images
      store.commit('SET_IMAGES',{images,index})
    };
    return {
      expanded,
      isOverflowing,
      textContainer,
      getImageHeight,
      getImageWidth,
      toggleText,
      imageContainerClass,
      passImage
      
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
