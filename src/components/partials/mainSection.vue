<template>
    <div class="col-md-6 border">
       <createPostVue/>
       <postVue/>
    </div>
</template>
<script>
import createPostVue from './createPost.vue'
import postVue from './post.vue'

export default {
    name:"main_section",
    components:{createPostVue,postVue}
}
</script>
<style scoped>
.card{
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

</style>