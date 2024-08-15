<template>
  <div class="card border-0 mt-3">
    <div class="card-body">
      <div class="row">
        <div class="col d-flex justify-content-end">
          <img
            src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4="
            alt=""
            class="rounded-circle border"
            width="60px"
            height="60px"
          />
        </div>
        <div class="col-10">
          <button
            class="create-post-btn"
            data-bs-toggle="modal"
            data-bs-target="#addPost"
          >
            What's on you mind, Jivan?
          </button>
        </div>
      </div>
      <hr />
      <div class="d-flex justify-content-between">
        <button class="btn btn-custom">
          <font-awesome-icon
            :icon="['fas', 'image']"
            class="text-success me-2"
          /><span> Photo</span>
        </button>
        <button
          class="btn btn-custom"
          data-bs-toggle="modal"
          data-bs-target="#feeling"
        >
          <font-awesome-icon
            :icon="['fas', 'face-smile']"
            class="text-warning me-2"
          /><span> Feeling</span>
        </button>
        <button class="btn btn-custom">
          <font-awesome-icon
            :icon="['fas', 'person-running']"
            class="text-secondary me-2"
          /><span> Activity</span>
        </button>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="addPost"
    tabindex="-1"
    role="dialog"
    aria-labelledby="add post"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header d-flex justify-content-between">
          <h5 class="modal-title">Create Post</h5>
          <button
            type="button"
            class="close btn"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <font-awesome-icon :icon="['fas', 'xmark']" />
          </button>
        </div>
        <div class="modal-body">
          <div class="post-header d-flex align-items-center">
            <div class="d-flex align-items-center">
              <img
                src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4="
                alt=""
                class="rounded-circle border me-2"
                width="50px"
                height="50px"
              />
              Andrew tate
            </div>
            <span>&ThickSpace;is celebrating Birthday. </span>
          </div>
          <div class="mt-3">
            <textarea
              style="resize: none"
              class="custom-texarea"
              cols="30"
              rows="10"
              placeholder="What's on your mind, Jivan?"
            ></textarea>
          </div>
          <div
            class="border d-flex justify-content-between align-items-center ps-2 pe-2 rounded"
          >
            <button class="btn btn-custom">
              <font-awesome-icon
                :icon="['fas', 'image']"
                class="text-success me-2"
              /><span> Photo</span>
            </button>
            <button class="btn btn-custom">
              <font-awesome-icon
                :icon="['fas', 'face-smile']"
                class="text-warning me-2"
              /><span> Feeling</span>
            </button>
            <button class="btn btn-custom">
              <font-awesome-icon
                :icon="['fas', 'person-running']"
                class="text-secondary me-2"
              /><span> Activity</span>
            </button>
          </div>
        </div>
        <div class="modal-footer d-flex">
          <button type="button" class="btn btn-primary post-btn">Post</button>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="feeling"
    tabindex="-1"
    role="dialog"
    aria-labelledby="feelingmodal"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header d-flex justify-content-between">
          <h5 class="modal-title">How are you feeling?</h5>
          <button
            type="button"
            class="close btn"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <font-awesome-icon :icon="['fas', 'xmark']" />
          </button>
        </div>
        <div class="modal-body">
          <div class="search">
            <span class="search-icon"
              ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
            /></span>
            <input type="text" placeholder="Search..." />
          </div>
          <div class="mt-3">

              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
            </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="activity"
    tabindex="-1"
    role="dialog"
    aria-labelledby="activitymodal"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered" role="document">
      <div class="modal-content">
        <div class="modal-header d-flex justify-content-between">
          <h5 class="modal-title">How are you feeling?</h5>
          <button
            type="button"
            class="close btn"
            data-bs-dismiss="modal"
            aria-label="Close"
          >
            <font-awesome-icon :icon="['fas', 'xmark']" />
          </button>
        </div>
        <div class="modal-body">
          <div class="search">
            <span class="search-icon"
              ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
            /></span>
            <input type="text" placeholder="Search..." />
          </div>
          <div class="mt-3">

              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
              <div class="row">
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128512;</span></div>
                      <div>Happy</div>
                  </button>
                  <button class="btn btn-custom col d-flex align-items-center">
                      <div class="emoji me-2"><span>&#128514;</span></div>
                      <div>Joy</div>
                  </button>
                 
                </div>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "create_post",
};
</script>
<style scoped>
img {
  object-fit: cover;
}
.create-post-btn {
  width: 100%;
  height: 50px;
  border: none;
  border-radius: 25px;
  text-align: left;
  padding-left: 2rem;
}
.btn-custom {
  outline: none;
  /* color: #b4b4b4; */
}
.btn-custom svg {
  font-size: 1.3rem;
}
.btn-custom:hover {
  background: #f2f2f2;
}
.text-success {
  color: rgb(17, 206, 17) !important;
}
.custom-texarea {
  width: 100%;
  height: 10rem;
  border: none;
  outline: none;
  font-size: 1.2rem;
}
.post-btn {
  width: 100%;
}
.search {
  position: relative;
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
.emoji{
    height: 40px;
    width: 40px;
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 50%;
    background: #f2f2f2;
    font-size: 1.1rem;
}
</style>
