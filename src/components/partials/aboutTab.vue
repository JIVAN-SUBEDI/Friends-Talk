<template>
  <div class="card border-0">
    <div class="card-body">
      <h5>About</h5>
      <div class="row mt-3">
        <div class="col-md-4 border-right">
          <nav class="nav flex-column nav-pills nav-justified border-right">
            <a class="nav-item nav-link text-secondary active" data-bs-toggle="tab" href="#overview">Overview</a>
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tab" href="#work">Work and education</a>
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tab" href="#places">Places lived</a>
            <a class="nav-item nav-link text-secondary" data-bs-toggle="tab" href="#contact">Contact & basic info</a>
          </nav>
        </div>
        <div class="col-md-8">
          <div class="tab-content" id="myTabContent">
            <div class="tab-pane fade show active" id="overview" role="tabpanel">
                <aboutOverview/>
            </div>
            <div class="tab-pane fade" id="work" role="tabpanel">
              <aboutWork />
            </div>
            <div class="tab-pane fade" id="places" role="tabpanel">
              <aboutPlaces />
            </div>
            <div class="tab-pane fade" id="contact" role="tabpanel">
              <aboutContact />
            </div>
  
         
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import aboutWork from './aboutWork.vue';
import aboutPlaces from './aboutPlaces.vue';
import aboutContact from './aboutContact.vue';
import aboutOverview from './aboutOverview.vue';

export default {
  name: "about_tab",
  components:{aboutWork,aboutPlaces,aboutContact,aboutOverview},
 
 
};
</script>

<style scoped>
.nav-link.active {
  color: white !important;
}
.text-small {
  font-size: 0.9rem;
}
.text-big {
  font-size: 1.6rem;
}

</style>

