<template>
  <div class="pb-4">
    <createPostVue />
    
    <!-- Display posts if available, otherwise show message -->
    <div v-if="posts?.results?.length">
      <postVue 
        v-for="post in posts.results" 
        :key="post.id" 
        :post="post" 
      />
    </div>
    <div v-else>
      <p>No posts to display.</p>
    </div>
<div class="d-flex align-items-center flex-column">

  <!-- Show More button -->
  <a v-if="posts?.next && !isLoading" class="text-primary mt-2 cursor-pointer text-decoration-none " @click="showMore">
    Show More
  </a>
  
  <!-- Loading message -->
  <div v-if="isLoading">Loading posts...</div>
</div>

    <!-- Modal Section for image -->
    <modalSectionVue  />
  </div>
</template>

<script>
import createPostVue from './createPost.vue'
import postVue from './post.vue'
import modalSectionVue from './modalSection.vue'
import { onMounted, onBeforeUnmount, computed } from 'vue'
import { useStore } from 'vuex'

export default {
  name: "main_section",
  components: { createPostVue, postVue, modalSectionVue },
  
  setup() {
    const store = useStore();
    
 

    // Posts data and loading state from Vuex
    const posts = computed(() => store.state.posts ?? { results: [], next: null });
    const isLoading = computed(() => store.state.loading);
    
    // Fetch initial posts on mount
    onMounted(() => {
      store.dispatch('fetchPosts');
    });

    // Clean up on unmount
    onBeforeUnmount(() => {
      store.dispatch('resetPosts');
    });

    // Show more posts
    const showMore = async () => {
      if (posts.value.next && !isLoading.value) {
        await store.dispatch('fetchMorePosts', posts.value.next);
      }
    };

    return { posts, isLoading, showMore};
  }
}
</script>

<style scoped>
.card {
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}
</style>
