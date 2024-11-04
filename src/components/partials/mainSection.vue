<template>
    <div class="pb-4">
       <createPostVue />
        <div @scroll="checkScroll" ref="scrollContainer" class="scrollContainer">
     
          <div v-if="posts.length">
            <postVue  v-for="post in posts" :key="post.id" :post="post" @passImage="passImage"/>
          </div>
          <div v-else>
            <p>No posts to display.</p>
          </div>
          <div v-if="isLoading">Loading  posts...</div>
        </div>
       <modalSectionVue :images="imageShow"/>
      </div>
</template>
<script>
import createPostVue from './createPost.vue'
import postVue from './post.vue'
import {ref,onMounted,onBeforeUnmount,computed} from 'vue'
import modalSectionVue from './modalSection.vue'
import { useStore } from 'vuex'
export default {
    name:"main_section",
    components:{createPostVue,postVue,modalSectionVue},
   
    setup(){
        const imageShow = ref();
        const passImage = (image)=>{

            imageShow.value = image;
          }
          const store = useStore();
          const scrollContainer = ref(null);
          const posts = computed(() => store.state.posts);
          const isLoading = computed(() => store.state.loading);

          // Fetch initial posts on mount
          onMounted(() => {
            store.dispatch('fetchPosts');
          });

          // Clean up on unmount
          onBeforeUnmount(() => {
            store.dispatch('resetPosts');
          });

          // Check scroll position to load more posts
          const checkScroll = () => {
            const container = scrollContainer.value;
            if (container.scrollTop + container.clientHeight >= container.scrollHeight - 10) {
              store.dispatch('fetchPosts'); // Load more posts if scrolled to the bottom
            }
          };

    return{posts,passImage,imageShow,checkScroll,scrollContainer,isLoading}
    }
}
</script>
<style scoped>
.card{
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}
.scrollContainer {
  height: 400px; /* Set a fixed height for the scroll area */
  overflow-y: auto; /* Enable vertical scrolling */
}

</style>