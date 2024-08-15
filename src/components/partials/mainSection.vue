<template>
    <div class="pb-4">
       <createPostVue/>
       <postVue  v-for="post in posts" :key="post.id" :post="post" @passImage="passImage"/>
      </div>
      <modalSectionVue :images="imageShow"/>
</template>
<script>
import createPostVue from './createPost.vue'
import postVue from './post.vue'
import {ref} from 'vue'
import modalSectionVue from './modalSection.vue'
export default {
    name:"main_section",
    components:{createPostVue,postVue,modalSectionVue},
    setup(){
        const imageShow = ref();
        const posts = ref([
      {
        id: 1,
        desc: "Had a great time at the beach!",
        userDetails: {
          firstName: "John",
          middleName: "A.",
          lastName: "Doe",
          user_id: "user123",
        },
        images: ["https://i0.wp.com/picjumbo.com/wp-content/uploads/beautiful-nature-mountain-scenery-with-flowers-free-photo.jpg?w=600&quality=80", "https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg", "https://images.pexels.com/photos/1266810/pexels-photo-1266810.jpeg?cs=srgb&dl=pexels-8moments-1266810.jpg&fm=jpg"],
        like: 120,
        activity: "feeling happy",
      },
      {
        id: 2,
        desc: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum. Donec vitae felis eu turpis tincidunt dignissim. Sed feugiat, mi eu vehicula bibendum, libero erat varius urna, id vulputate sapien arcu ut turpis. Integer accumsan justo non risus fermentum, ac facilisis purus gravida. Sed euismod ex et lectus fringilla, eu venenatis urna tempor. Aenean a bibendum risus, in vehicula sapien. Curabitur id eros a odio lacinia auctor. Integer sollicitudin ligula vel odio interdum auctor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Mauris lacinia, erat at facilisis.",
        userDetails: {
          firstName: "Jane",
          middleName: "B.",
          lastName: "Smith",
          user_id: "user456",
        },
        images: ["https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg", 
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
        "https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=",
      ],
        like: 85,
        activity: "feeling exhahusted",
      },
      {
        id: 3,
        desc: "Morning workout",
        userDetails: {
          firstName: "Alice",
          middleName: "C.",
          lastName: "Johnson",
          user_id: "user789",
        },
        images: ["https://t4.ftcdn.net/jpg/06/44/26/41/360_F_644264157_ksBPMdndPvT5as7W9PWWNAnjdC2aEMQA.jpg"],
        like: 65,
        activity: "celebreting sister birthday",
      },
    ]);
    const passImage = (image)=>{

      imageShow.value = image;
    }
    return{posts,passImage,imageShow}
    }
}
</script>
<style scoped>
.card{
    box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

</style>