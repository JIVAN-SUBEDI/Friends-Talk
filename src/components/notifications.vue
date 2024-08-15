<template>
    <navbar/>
    <div class="bg-light p-3">
        <div class="container bg-white rounded p-3">
            <h4 class="mt2 mb-3">Notifications</h4>
                <div class="d-flex align-items-center gap-3 ">
                    <img src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=" alt="" width="70px" height="70px">
                    <div class="d-flex flex-column" style="width: calc(100% - (2rem + 70px));">
                        <p class="text-truncate-2" ><b>Jivan subedi</b> sent you a friend request. </p>
                        <span class="text-secondary text-small">5d</span>
                    </div>
                    <div class="dot"></div>
                </div>
                <div class="d-flex align-items-center gap-3 mt-4">
                    <img src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=" alt="" width="70px" height="70px">
                    <div class="d-flex flex-column" style="width: calc(100% - (2rem + 70px));">
                        <p class="text-truncate-2" ><b>Jivan subedi</b> sent you a friend request. </p>
                        <span class="text-secondary text-small">5d</span>
                    </div>
                    <div class="dot"></div>
                </div>
                <div class="d-flex align-items-center gap-3 mt-4">
                    <img src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=" alt="" width="70px" height="70px">
                    <div class="d-flex flex-column" style="width: calc(100% - (2rem + 70px));">
                        <p class="text-truncate-2" ><b>Jivan subedi</b> sent you a friend request. </p>
                        <span class="text-secondary text-small">5d</span>
                    </div>
                    <div class="dot"></div>
                </div>
                <div class="d-flex align-items-center gap-3 mt-4">
                    <img src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4=" alt="" width="70px" height="70px">
                    <div class="d-flex flex-column" style="width: calc(100% - (2rem + 70px));">
                        <p class="text-truncate-2" ><b>Jivan subedi</b> sent you a friend request. </p>
                        <span class="text-secondary text-small">5d</span>
                    </div>
                    <div class="dot"></div>
                </div>
        
                <div class="mt-3 d-flex border">

                    <button class="btn btn-outline-primary w-100 ">Show previous Notifications</button>
                </div>
        </div>
    </div>
</template>
<script>
import navbar from './partials/navbar.vue';
export default {
    name:"notification_page",
    components:{navbar}
}
</script>
<style scoped>
.text-small{
    font-size: 0.9rem;
}
.text-truncate-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;  
    overflow: hidden;
    text-overflow: ellipsis;
}
.dot{
    width: 15px;
    height: 15px;
    border-radius: 50%;
    background:#24a0ed ;
}
img{
    border-radius: 50%;
    object-fit: cover;
}
</style>