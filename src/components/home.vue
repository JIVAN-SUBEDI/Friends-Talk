<template>
    <div>
        <navbarVue/>
        <div class="container-fluid bg-light custom-container">
            <div class="row">
                <div class="col-md-3">

                    <leftSection/>
                </div>
                <div class="col-md-6">

                    <mainSection />
                </div>
                <div class="col-md-3">

                    <rightSection/>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
import navbarVue from './partials/navbar.vue'
import leftSection from './partials/leftSection.vue';
import rightSection from './partials/rightSection.vue';
import mainSection from './partials/mainSection.vue';



export default {
    name:"home_page",
    components:{navbarVue,leftSection,rightSection,mainSection},
  
} 
</script>
<style scoped>
.custom-container{
    min-height: calc(100vh - 75px);
}
</style>