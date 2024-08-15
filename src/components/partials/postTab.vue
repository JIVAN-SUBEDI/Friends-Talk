<template>
      <div class="row">
          <div class="col-md-4">
            <div class="card border-0">
              <div class="card-body">
                <h5>Intro</h5>
                <div class="d-flex flex-column">
                    <span>
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora quaerat beatae repellat facilis molestiae libero aspernatur consequatur atque quam, odit unde ex vero consectetur officiis saepe officia similique, quidem modi distinctio facere sed deserunt dicta natus hic! Nobis dignissimos placeat quibusdam ea? 
                    </span>
                    <button class="btn edit-btn mt-2">Edit bio</button>
                </div>
                <div class="d-flex flex-column mt-3">
                    <div class="d-flex mt-2"><font-awesome-icon :icon="['fas', 'suitcase']" class="text-secondary" /> <span class="ms-2">Not yet Working</span></div>
                    <div class="d-flex mt-2"> <font-awesome-icon :icon="['fas', 'house']"  class="text-secondary"/><span class="ms-2">Lives in Jhapa,nepal</span></div>
                    <div class="d-flex mt-2"> <font-awesome-icon :icon="['fas', 'location-dot']"  class="text-secondary"/><span class="ms-2">From Damak</span></div>
                    <button class="btn edit-btn mt-2">Edit details</button>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-8">
            <mainSection/>
          </div>
        </div>
</template>
<script>
import mainSection from './mainSection.vue';
export default {
    name:"postTab",
    components:{mainSection}
}
</script>
<style scoped>
.edit-btn{
    background: #e7e4e4;
}
.edit-btn:hover{
    background: #d4d3d3;

}
</style>