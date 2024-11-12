<template>
    <div>
        <navbar/>
        <div class="container-fluid bg-light custom-container min-100">
            <div class="row">
                <div class="col-md-3">
                    <!-- Side content can go here -->
                </div>
                <div class="col-md-6">
                    <post :post="postData"/>
                </div>
                <div class="col-md-3">
                    <!-- Side content can go here -->
                </div>
            </div>
        </div>
        <modalSection/>
    </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import navbar from './partials/navbar.vue';
import post from './partials/post.vue';
import modalSection from './partials/modalSection.vue';
import axiosInstance from '@/axios';
import { useRoute, useRouter } from 'vue-router';
import { useStore } from 'vuex';


export default {
    name: "page_view",
    components: { navbar, post, modalSection },
    setup() {
        const store = useStore();
        const route = useRoute();
        const postData = computed(() =>{
            const post = store.state.posts.results.find(obj => obj.id === route.params.id);
            if (post){

                return post;
            }
            return {}

        } ); 
        const router = useRouter();
        
        onMounted(async () => {
            try {
                const response = await axiosInstance.get(`post/${route.params.id}`);
                store.commit('SET_POSTS',response.data)
            } catch (error) {
                router.push('/');
            }
        });
        
        return { postData }; // Use `postData` to bind to the template
    }
}
</script>

<style scoped>
.min-100 {
    min-height: calc(100vh - 80px);
}
</style>
