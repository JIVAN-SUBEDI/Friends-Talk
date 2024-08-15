<template>
  <div class="bg-light d-flex justify-content-center align-items-center height">
    <div class="">
      <div class="card border-0 w-60">
        <div class="card-body">
          <div class="row">
            <div class="col">
              <h4 class="mt-3">Friends Talk</h4>
              <p class="text-secondary">Welcome Back,</p>
              <p class="text-secondary">
                We're glad to see you again! Log in to connect with your
                friends, share your moments, and explore what's happening around
                the world. Your community is just a click away!
              </p>
              <div class="d-flex justify-content-center">
                <button
                  class="btn btn-success mt-3"
                  data-bs-toggle="modal"
                  data-bs-target="#signup"
                >
                  Create new account
                </button>
              </div>
            </div>
            <div class="col">
              <h4 class="text-center mt-3">Login</h4>
              <div class="mt-3">
                <div class="form-group">
                  <label for="">Email Address</label>
                  <input
                    type="email"
                    class="form-control mt-2"
                    placeholder="Email Address"
                  />
                </div>
                <div class="form-group mt-3 mb-3">
                  <label for="">Password</label>
                  <input
                    type="password"
                    class="form-control mt-2"
                    placeholder="Password"
                  />
                </div>

                <a href="" class="text-decoration-none">Forgot Password?</a>
                <div class="mt-4 d-flex">
                  <button class="btn btn-primary btn-custom">Login</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="signup"
    tabindex="-1"
    aria-labelledby="signupLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="signupLabel">Signup</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row form-group">
            <div class="col-md-6">
              <label for="">First name</label>
              <input
                type="text"
                placeholder="First name"
                class="form-control"
              />
            </div>
            <div class="col-md-6">
              <label for="">Last name</label>
              <input type="text" placeholder="Last name" class="form-control" />
            </div>
          </div>
          <div class="form-group mt-2">
            <label for="">Email Address</label>
            <input
              type="email"
              class="form-control"
              placeholder="someone@example.com"
            />
          </div>
          <div class="form-group mt-2">
            <label for="">Password</label>
            <input
              type="password"
              class="form-control"
              placeholder="password"
            />
          </div>
          <div class="form-group mt-2">
            <label for="">Date of birth</label>
            <input
              type="date"
              class="form-control"
              placeholder="Date of birth"
            />
          </div>
          <label for="" class="mt-2">Gender</label>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gender"
              id="male"
              checked
       
            />
            <label class="form-check-label" for="male">
              Male
            </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gender"
              id="female"
       
            />
            <label class="form-check-label" for="female">
              Female
            </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gender"
              id="Others"
       
       
            />
            <label class="form-check-label" for="Others">
              Others
            </label>
          </div>
          <div class="d-flex justify-content-center">
            <button class="btn btn-success">Signup</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "login_page",
};
</script>
<style scoped>
.height {
  height: 100vh;
}
.w-60 {
  width: 55vw;
}
.btn-custom {
  width: 100%;
}
</style>
