<template>
  <div class="card mt-3 border-0">
    <div class="card-body">
      <div class="post-header d-flex align-items-center">
        <div class="d-flex align-items-center">
          <img
          :src="post.user_details.profile_image ? post.user_details.profile_image : require('@/assets/img/default-profile.jpg')"            alt=""
            class="rounded-circle border me-2"
            width="50px"
            height="50px"
          />
          <div class="d-flex flex-column">
            <span>
              {{
                post.user_details.first_name +
                " " +
               
                post.user_details.last_name
              }}
              <!-- <span>&ThickSpace;is {{ post.activity }} </span> -->
            </span>
            <span class="text-secondary"> 24h ago </span>
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
          @click="passImage"
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
      <div class="d-flex justify-content-between mt-2">
        <div class="like-show ">
          <font-awesome-icon :icon="['fas', 'thumbs-up']" />
          <span class="ms-2">136</span>
        </div>
        <div class="comment-share-show ">
          <font-awesome-icon :icon="['fas', 'comment']" class="ms-3" />
          <span class="ms-2">136</span>
        </div>
      </div>
      <hr />
      <div class="d-flex justify-content-between ps-2 pe-2">
        <a class="d-flex align-items-center nav-link active">
          <font-awesome-icon :icon="['fas', 'thumbs-up']" />
          <span class="ms-2">Like</span>
        </a>
        <a class="d-flex align-items-center nav-link" data-bs-toggle="modal" data-bs-target="#comment">
          <font-awesome-icon :icon="['fas', 'comment']" />
          <span class="ms-2">Comment</span>
        </a>
        <a class="d-flex align-items-center nav-link" data-bs-toggle="modal" data-bs-target="#share">
          <font-awesome-icon :icon="['fas', 'share']" />
          <span class="ms-2">Share</span>
        </a>
      </div>
    </div>
  </div>
</template>

<script>

import { ref, onMounted, computed } from "vue";

export default {
  name: "post_card",
  props: ["post"],
  setup(props, { emit }) {
    const expanded = ref(false);
    const textContainer = ref(null);
    const isOverflowing = ref(false);

    const checkOverflow = () => {
      const el = textContainer.value;
      const lineHeight = parseFloat(window.getComputedStyle(el).lineHeight);
      const maxHeight = lineHeight * 8;
      isOverflowing.value = el.scrollHeight > maxHeight;
    };

    onMounted(async() => {
      checkOverflow();
     
    });

    const toggleText = () => {
      expanded.value = !expanded.value;
    };

    const imageContainerClass = computed(() => {
      const imageCount = props.post.images.length;
      return imageCount > 1;
    });

    const getImageHeight = computed(() => {
      const imageCount = props.post.images.length;
      if (imageCount > 1) {
        if (imageCount > 6) {
          const divider = Math.ceil(imageCount / 3);
          return 35 / Math.ceil(imageCount / divider);
        }
        return 35 / Math.ceil(imageCount / 2);
      } else {
        return 35;
      }
    });

    const getImageWidth = (index) => {
      const imageCount = props.post.images.length;
      if (imageCount > 6) {
        const divider = Math.ceil(imageCount / 3);
        const imagecalc = imageCount - Math.floor(imageCount / divider) * divider;
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

    const passImage = () => {
      emit('passImage', props.post.images);
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
.comment-share-show{
  color: #636c72;

}
.nav-link {
  cursor: pointer;
  color: #636c72;
}
.nav-link.active {
  color: #24a0ed;
}


</style>
