<template>
  <div class="d-flex flex-column h-100 position-relative hide-scrollbar">
    <div class="hide-scrollbar">
      <div class="container py-8">
        <!-- Title -->
        <div class="mb-8">
          <h4 class="m-0">Chats</h4>
        </div>

        <!-- Search -->
        <div class="mb-4">
          <div class="search">
            <span class="search-icon"
              ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
            /></span>
            <input type="text" placeholder="Search Friends" />
          </div>
        </div>

        <!-- Chats -->
        <div class="card-list">
          <!-- Card -->
          <a href="chat-direct.html" class="card border-0 text-reset">
            <div class="card-body">
              <div class="row gx-5">
                <div class="col-auto">
                  <div class="avatar avatar-online">
                    <img
                      src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRYOB6GkyxctiwfJieHOvgp9ohwOV2jUg32jA&s"
                      alt="#"
                      class="avatar-img"
                    />
                  </div>
                </div>

                <div class="col">
                  <div class="d-flex align-items-center mb-2">
                    <h6 class="me-auto mb-0">Ollie Chandler</h6>
                    <span class="text-muted extra-small ms-2">08:45 PM</span>
                  </div>

                  <div class="d-flex align-items-center">
                    <div class="line-clamp me-auto text-secondary text-small">
                      Hello! Yeah, I'm going to meet friend of mine at the
                      departments stores now.
                    </div>

                    <div class="badge badge-circle bg-primary ms-5">
                      <span>3</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- .card-body -->
          </a>
          <!-- Card -->

          <!-- Card -->
          <a href="#" class="card border-0 text-reset">
            <div class="card-body">
              <div class="row gx-5">
                <div class="col-auto">
                  <div class="avatar avatar-online">
                    <span class="avatar-text">M</span>
                  </div>
                </div>

                <div class="col">
                  <div class="d-flex align-items-center mb-2">
                    <h6 class="me-auto mb-0">Marshall Wallaker</h6>
                    <span class="text-muted extra-small ms-2">12:18 PM</span>
                  </div>

                  <div class="d-flex align-items-center">
                    <div class="line-clamp me-auto text-secondary text-small">
                      Hello! Yeah, I'm going to meet my friend of mine at the
                      departments stores as soon as possible.
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- .card-body -->
          </a>
          <!-- Card -->

          <!-- Card -->
          <a href="chat-direct.html" class="card border-0 text-reset">
            <div class="card-body">
              <div class="row gx-5">
                <div class="col-auto">
                  <div class="avatar">
                    <svg
                      class="avatar-img placeholder-img"
                      width="100%"
                      height="100%"
                      xmlns="http://www.w3.org/2000/svg"
                      role="img"
                      aria-label="Placeholder"
                      preserveAspectRatio="xMidYMid slice"
                      focusable="false"
                    >
                      <title>Placeholder</title>
                      <rect width="100%" height="100%" fill="#868e96"></rect>
                    </svg>
                  </div>
                </div>

                <div class="col">
                  <div class="d-flex align-items-center mb-2">
                    <h5 class="placeholder-glow w-100 mb-0">
                      <span class="placeholder col-5"></span>
                    </h5>
                  </div>

                  <div class="placeholder-glow">
                    <span class="placeholder col-12"></span>
                    <span class="placeholder col-8"></span>
                  </div>
                </div>
              </div>
            </div>
            <!-- .card-body -->
          </a>
          <!-- Card -->

          <!-- Card -->
          <a href="chat-direct.html" class="card border-0 text-reset">
            <div class="card-body">
              <div class="row gx-5">
                <div class="col-auto">
                  <div class="avatar">
                    <svg
                      class="avatar-img placeholder-img"
                      width="100%"
                      height="100%"
                      xmlns="http://www.w3.org/2000/svg"
                      role="img"
                      aria-label="Placeholder"
                      preserveAspectRatio="xMidYMid slice"
                      focusable="false"
                    >
                      <title>Placeholder</title>
                      <rect width="100%" height="100%" fill="#868e96"></rect>
                    </svg>
                  </div>
                </div>

                <div class="col">
                  <div class="d-flex align-items-center mb-3">
                    <h5 class="placeholder-glow w-100 mb-0">
                      <span class="placeholder col-5"></span>
                    </h5>
                  </div>

                  <div class="placeholder-glow">
                    <span class="placeholder col-12"></span>
                    <span class="placeholder col-8"></span>
                  </div>
                </div>
              </div>
            </div>
            <!-- .card-body -->
          </a>
          <!-- Card -->
        </div>
        <!-- Chats -->
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "chat_sidebar",
};
</script>
<style scoped>
* {
  text-decoration: none;
}
.search {
  position: relative;
  height: 100%;
}
.search input {
  height: 45px;
  width: 100%;
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
.avatar-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}
.avatar {
  width: 50px;
  height: 50px;
}
.text-small {
  font-size: 0.9rem;
}
.h-100{
    height:calc(100vh - 75px) !important;
    overflow: hidden;
}
</style>
