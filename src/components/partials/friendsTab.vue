<template>
  <div class="card border-0">
    <div class="card-body">
      <h5>Friends</h5>
      <div class="d-flex justify-content-between mt-3">
        <div class="search">
          <span class="search-icon"
            ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
          /></span>
          <input type="text" placeholder="Search Friends" />
        </div>
        <a href="#" class="text-decoration-none">Friend Request</a>
      </div>
      <div class="row g-3 mt-3">
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between">
                <div class="d-flex align-items-center">
                  <img
                    src="https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg"
                    alt=""
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>Jasmine Doe</h5>
                    <span class="text-secondary text-small"
                      >2 Mutual Friends</span
                    >
                  </div>
                </div>
                <div class="d-flex align-items-center">
                  <button class="btn btn-danger">
                    <font-awesome-icon :icon="['fas', 'trash']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between">
                <div class="d-flex align-items-center">
                  <img
                    src="https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg"
                    alt=""
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>Jasmine Doe</h5>
                    <span class="text-secondary text-small"
                      >2 Mutual Friends</span
                    >
                  </div>
                </div>
                <div class="d-flex align-items-center">
                  <button class="btn btn-danger">
                    <font-awesome-icon :icon="['fas', 'trash']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between">
                <div class="d-flex align-items-center">
                  <img
                    src="https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg"
                    alt=""
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>Jasmine Doe</h5>
                    <span class="text-secondary text-small"
                      >2 Mutual Friends</span
                    >
                  </div>
                </div>
                <div class="d-flex align-items-center">
                  <button class="btn btn-danger">
                    <font-awesome-icon :icon="['fas', 'trash']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between">
                <div class="d-flex align-items-center">
                  <img
                    src="https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg"
                    alt=""
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>Jasmine Doe</h5>
                    <span class="text-secondary text-small"
                      >2 Mutual Friends</span
                    >
                  </div>
                </div>
                <div class="d-flex align-items-center">
                  <button class="btn btn-danger">
                    <font-awesome-icon :icon="['fas', 'trash']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between">
                <div class="d-flex align-items-center">
                  <img
                    src="https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg"
                    alt=""
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>Jasmine Doe</h5>
                    <span class="text-secondary text-small"
                      >2 Mutual Friends</span
                    >
                  </div>
                </div>
                <div class="d-flex align-items-center">
                  <button class="btn btn-danger">
                    <font-awesome-icon :icon="['fas', 'trash']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card">
            <div class="card-body">
              <div class="d-flex justify-content-between">
                <div class="d-flex align-items-center">
                  <img
                    src="https://st2.depositphotos.com/1000824/8294/i/450/depositphotos_82947324-stock-photo-russian-beauty-young-brunette-girl.jpg"
                    alt=""
                    class="rounded"
                    width="100px"
                    height="100px"
                  />
                  <div class="ms-3 d-flex flex-column">
                    <h5>Jasmine Doe</h5>
                    <span class="text-secondary text-small"
                      >2 Mutual Friends</span
                    >
                  </div>
                </div>
                <div class="d-flex align-items-center">
                  <button class="btn btn-danger">
                    <font-awesome-icon :icon="['fas', 'trash']" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "friends_tab",
};
</script>
<style scoped>
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
.text-small {
  font-size: 0.9rem;
}
</style>
