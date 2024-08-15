<template>
  <div class="card border-0">
    <div class="card-body">
      <h5>About</h5>
      <div class="row mt-3">
        <div class="col-md-4 border-right">
          <nav class="nav flex-column nav-pills nav-justified border-right">
            <a class="nav-item nav-link text-secondary active" href="#overview"
              >Overview</a
            >
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tabs" href="#work"
              >Work and education</a
            >
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tabs" href="#places"
              >Places lived</a
            >
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tabs" href="#contact"
              >Contact & basic info</a
            >
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tabs" href="#family"
              >Family & relationship</a
            >
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tabs" href="#details"
              >Details about you</a
            >
          </nav>
        </div>
        <div class="col-md-8">
          <div class="tab-content" id="myTabContent">
            <div
              class="tab-pane fade show active"
              id="overview"
              role="tabpanel"
              aria-labelledby="home-tab"
            >
            <ul>
                <li class="d-flex justify-content-between">
                    <div class="d-flex align-items-center">
                        <font-awesome-icon :icon="['fas', 'suitcase']" class="text-secondary text-big" /> 
                        <div class="d-flex flex-column align-items-center ms-3">
                            <span>Not Yet Working</span>
                            <span class="text-small text-secondary">24 june 2019 present</span>
                        </div>
                    </div>
                    <font-awesome-icon :icon="['fas', 'earth-americas']" />
                </li>
                <li class="d-flex justify-content-between mt-3">
                    <div class="d-flex align-items-center">
                        <font-awesome-icon :icon="['fas', 'graduation-cap']" class="text-secondary text-big" /> 
                       
                            <span class="ms-3">Went to central campus of technology</span>
                          
                    </div>
                    <font-awesome-icon :icon="['fas', 'earth-americas']" />
                </li>
                <li class="d-flex justify-content-between mt-3">
                    <div class="d-flex align-items-center">
                        <font-awesome-icon :icon="['fas', 'home']" class="text-secondary text-big" /> 
                       
                            <span class="ms-3">Lives in Dharan, Nepal</span>
                          
                    </div>
                    <font-awesome-icon :icon="['fas', 'earth-americas']" />
                </li>
                <li class="d-flex justify-content-between mt-3">
                    <div class="d-flex align-items-center">
                        <font-awesome-icon :icon="['fas', 'location-dot']" class="text-secondary text-big" /> 
                       
                            <span class="ms-3">From Damak</span>
                          
                    </div>
                    <font-awesome-icon :icon="['fas', 'lock']" />
                </li>
                <li class="d-flex justify-content-between mt-3">
                    <div class="d-flex align-items-center">
                        <font-awesome-icon :icon="['fas', 'heart']" class="text-secondary text-big" /> 
                       
                            <span class="ms-3">Single</span>
                          
                    </div>
                    <font-awesome-icon :icon="['fas', 'earth-americas']" />
                </li>
                <li class="d-flex justify-content-between mt-3">
                    <div class="d-flex align-items-center">
                        <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big" /> 
                       
                            <span class="ms-3">9860402354</span>
                          
                    </div>
                    <font-awesome-icon :icon="['fas', 'lock']" />
                </li>
     
            </ul>
            </div>
            <div
              class="tab-pane fade"
              id="work"
              role="tabpanel"
              aria-labelledby="profile-tab"
            >
              ...
            </div>
            <div
              class="tab-pane fade"
              id="places"
              role="tabpanel"
              aria-labelledby="contact-tab"
            >
              ...
            </div>
            <div
              class="tab-pane fade"
              id="contact"
              role="tabpanel"
              aria-labelledby="contact-tab"
            >
              ...
            </div>
            <div
              class="tab-pane fade"
              id="family"
              role="tabpanel"
              aria-labelledby="contact-tab"
            >
              ...
            </div>
            <div
              class="tab-pane fade"
              id="details"
              role="tabpanel"
              aria-labelledby="contact-tab"
            >
              ...
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "about_tab",
};
</script>
<style scoped>
.nav-link.active {
  color: white !important;
}
.text-small {
  font-size: 0.9rem;
}
.text-big{
    font-size: 1.7rem;
}
</style>
