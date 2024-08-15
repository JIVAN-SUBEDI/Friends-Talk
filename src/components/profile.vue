<template>
  <navbarVue />
  <div class="container mt-3">
    <div class="cover-image bg-light rounded">
      <img
        src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4="
        alt=""
        class="rounded"
      />
      <button class="rounded ">
        <font-awesome-icon :icon="['fas', 'camera']" />
        <span>Add cover photo</span>
      </button>
    </div>
    <div class="d-flex justify-content-between ps-2 pe-2">
      <div class="d-flex align-items-center">
        <div class="image-container">
          <img
            src="https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg"
            alt=""
          />
          <button class="edit-btn"><font-awesome-icon :icon="['fas', 'camera']" /></button>
        </div>
        <div class="d-flex flex-column ms-3">
          <h5>Jasmine Doe</h5>
          <span class="text-secondary">150 Friends</span>
        </div>
      </div>
      <div class="d-flex align-items-center">
        <button class="btn edit-btn">
          <font-awesome-icon :icon="['fas', 'pen']" />
          <span class="ms-2">Edit profile</span>
        </button>
      </div>
    </div>
    <hr />
    <ul class="nav" id="myTab" role="tablist">
      <li class="nav-item">
        <a
          class="nav-link active"
          data-bs-toggle="tab"
          href="#posts"
          role="tab"
          aria-controls="posts"
          aria-selected="true"
          >Posts</a
        >
      </li>
      <li class="nav-item">
        <a
          class="nav-link"
          data-bs-toggle="tab"
          href="#about"
          role="tab"
          aria-controls="about"
          aria-selected="false"
          >About</a
        >
      </li>
      <li class="nav-item">
        <a
          class="nav-link"
          data-bs-toggle="tab"
          href="#friends"
          role="tab"
          aria-controls="friends"
          aria-selected="false"
          >Friends</a
        >
      </li>
    </ul>
    <div class="tab-content bg-light mt-3" id="myTabContent">
      <div
        class="tab-pane fade show active p-3"
        id="posts"
        role="tabpanel"
        aria-labelledby="Posts-tab"
      >
      <postTabVue/>
      </div>
      <div
        class="tab-pane fade p-3"
        id="about"
        role="tabpanel"
        aria-labelledby="About-tab"
      >
        <aboutTab/>
      </div>
      <div
        class="tab-pane fade p-3"
        id="friends"
        role="tabpanel"
        aria-labelledby="Friends-tab"
      >
        <friendsTabVue/>
      </div>
    </div>
  </div>
</template>
<script>
import navbarVue from "./partials/navbar.vue";
import postTabVue from './partials/postTab.vue';
import aboutTab from "./partials/aboutTab.vue";
import friendsTabVue from './partials/friendsTab.vue'

export default {
  name: "profile_page",
  components: { navbarVue,postTabVue,aboutTab,friendsTabVue },
};
</script>
<style scoped>
.cover-image {
  height: 60vh;
  position: relative;
}
.cover-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.cover-image button {
  position: absolute;
  right: 2rem;
  bottom: 2rem;
  padding: 0.5rem 1rem;
  border: none;
  background: white;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
.cover-image button:hover {
  background: #f2f2f2;
}
.cover-image button svg {
  font-size: 1.1rem;
}
.image-container {
  width: 10rem;
  height: 10rem;
  border-radius: 50%;
  border: 4px solid #636c72;
  position: relative;
  top: -15%;
}
.image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
}
.image-container button {
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  position: absolute;
  bottom: 0;
  right: 0.4rem;
}

.nav-link {
  border: none !important;
  color: #636c72;
}
.nav-link.active {
  border-bottom: 2px solid #24a0ed !important;
  color: #24a0ed;
}
.edit-btn{
    background: #e7e4e4;
}
.edit-btn:hover{
    background: #d4d3d3;

}
</style>
