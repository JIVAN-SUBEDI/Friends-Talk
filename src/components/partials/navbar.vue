<template>
  <div class="navbar ps-3 pe-3">
    <div class="navbar-brand">Friends Talk</div>
    <div class="search">
      <span class="search-icon"
        ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
      /></span>
      <input type="text" placeholder="Search Friends" />
    </div>
    <ul>
      <li class="search-responsive">
        <a class="navbar-items"
          ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
        /></a>
      </li>
      <li>
        <a class="navbar-items"
          ><font-awesome-icon :icon="['fas', 'message']" /><span class="count"
            >9+</span
          ></a
        >
      </li>
      <li class="dropdown">
        <a class="navbar-items"  data-bs-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
          ><font-awesome-icon :icon="['fas', 'bell']" /><span class="count"
            >9+</span
          ></a
        >
        <div class="dropdown-menu  notifications-menu">
            <div class="d-flex justify-content-between align-items-center">

                <h5 class="ms-3 mb-2 mt-2">Notifications</h5>
                <a href="" class="me-3 text-decoration-none">See All</a>
            </div>
          <a class="dropdown-item" href="#">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYOB6GkyxctiwfJieHOvgp9ohwOV2jUg32jA&s"  class="rounded-circle border me-2">
            <div> <b>Jasmin James</b> sent you a friend Request.</div>
          </a>
       
      
        </div>
      </li>
      <li class="dropdown">
        <a
          class="navbar-items"
          data-bs-toggle="dropdown"
          aria-haspopup="true"
          aria-expanded="false"
          ><img
            src="https://st2.depositphotos.com/2944867/8579/i/450/depositphotos_85791042-stock-photo-autumnal-in.jpg"
            class="rounded-circle"
            alt="" />
          <span class="dropdown-icon"
            ><font-awesome-icon :icon="['fas', 'chevron-down']" /></span
        ></a>
        <div class="dropdown-menu dropdown-menu-right">
          <a class="dropdown-item d-flex align-items-center" href="#">
            <span class="navbar-items me-2"
              ><font-awesome-icon :icon="['fas', 'user']"
            /></span>
            Profile</a
          >
          <a class="dropdown-item d-flex align-items-center" href="#">
            <span class="navbar-items me-2"
              ><font-awesome-icon :icon="['fas', 'gear']"
            /></span>
            settings</a
          >
          <a class="dropdown-item d-flex align-items-center" href="#">
            <span class="navbar-items me-2"
              ><font-awesome-icon :icon="['fas', 'comment']"
            /></span>
            Give Feedback</a
          >
          <a class="dropdown-item d-flex align-items-center" href="#">
            <span class="navbar-items me-2"
              ><font-awesome-icon :icon="['fas', 'arrow-right-from-bracket']"
            /></span>
            Logout</a
          >
        </div>
      </li>
    </ul>
  </div>
</template>
<script>
export default {
  name: "navbar_section",
};
</script>
<style scoped>
.navbar {
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  height: 75px;
  display: flex;
  align-items: center;
}
.navbar-brand {
  height: 100%;
}

ul {
  display: flex;
  list-style: none;
  align-items: center;
  gap: 1rem;
  height: 100%;
}
img {
  width: 40px;
  height: 40px;
}
ul li .navbar-items {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 1.1rem;
  color: black;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  background: #f2f2f2;
  text-decoration: none;
  position: relative;
  cursor: pointer;
}
.navbar-items:hover {
  background: #cccbcb;
}
.search {
  position: relative;
  height: 100%;
}
.search input {
  height: 45px;
  width: 25rem;
  border-radius: 45px;
  outline: none;
  border: none;
  background: #f2f2f2;
  padding-left: 3rem;
}
.search-icon {
  position: absolute;
  top: calc(22.5px - 0.6rem);
  left: 0.8rem;
  color: #636c72;
}
.count {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: red;
  font-size: 0.7rem;
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  position: absolute;
  top: -5px;
  right: -5px;
}
.dropdown-icon {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: #f2f2f2;
  font-size: 0.7rem;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #636c72;
  position: absolute;
  bottom: -5px;
  right: -5px;
}
.dropdown-menu-right {
  position: absolute !important;
  left: -10rem !important;
  top: 3.5rem !important;
}
.search-responsive {
  display: none;
}
.notifications-menu{
    width: 21rem;
    position: absolute !important;
  left: -20rem !important;
  top: 3.5rem !important;
}
.dropdown-item{
    display: flex;
    align-items: center;
    white-space: normal;
    padding: 0.5rem;
}

.dropdown-item img{
    width: 70px;
    height: 60px;
    object-fit: cover;

}

@media (max-width: 800px) {
  .search-responsive {
    display: flex;
  }
  .search {
    display: none;
  }
}
</style>
