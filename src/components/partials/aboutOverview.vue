<template>
    <ul>
        <li class="d-flex justify-content-between">
            <div class="d-flex align-items-center">
                <font-awesome-icon :icon="['fas', 'suitcase']" class="text-secondary text-big" />
                <div class="d-flex flex-column align-items-center ms-3">
                    <span class="d-flex flex-column " v-if="workplace">
                        <span>{{ workplace.position }} at {{ workplace.name }}</span>
                        <span class="text-small text-secondary">{{ workplace.works_from }} to <span v-if="workplace.works_to == ''">Present</span> <span v-else>{{ workplace.works_to }}</span></span>
                    </span>
                    <span v-else>
                        Not working yet
                    </span>
                </div>
            </div>
          
            
            <div v-if="workplace">
                <font-awesome-icon v-if="workplace.audience == '0'" :icon="['fas', 'earth-americas']" />
                <font-awesome-icon v-if="workplace.audience == '1'" :icon="['fas', 'users']" />
                <font-awesome-icon v-if="workplace.audience == '2'" :icon="['fas', 'lock']" />
            </div>
            
          
        </li>
        <li class="d-flex justify-content-between mt-3">
            <div class="d-flex align-items-center">
                <font-awesome-icon :icon="['fas', 'graduation-cap']" class="text-secondary text-big" />
                <span class="ms-3" v-if="college">{{ college.message }}</span>
            </div>
            <div v-if="college && college.data">
                <font-awesome-icon v-if="college.data.audience == '0'" :icon="['fas', 'earth-americas']" />
                <font-awesome-icon v-if="college.data.audience == '1'" :icon="['fas', 'users']" />
                <font-awesome-icon v-if="college.data.audience == '2'" :icon="['fas', 'lock']" />
            </div>
        </li>
        <li class="d-flex justify-content-between mt-3">
            <div class="d-flex align-items-center">
                <font-awesome-icon :icon="['fas', 'home']" class="text-secondary text-big" />
                <span class="ms-3">
                    <span v-if="currentCity"> Lives in {{ currentCity.city }} </span>
                    <span v-else>Current city not added yet.</span>
                </span>
            </div>
            <div v-if="currentCity">
                <font-awesome-icon v-if="currentCity.audience == '0'" :icon="['fas', 'earth-americas']" />
                <font-awesome-icon v-if="currentCity.audience == '1'" :icon="['fas', 'users']" />
                <font-awesome-icon v-if="currentCity.audience == '2'" :icon="['fas', 'lock']" />
            </div>
        </li>
        <li class="d-flex justify-content-between mt-3">
            <div class="d-flex align-items-center">
                <font-awesome-icon :icon="['fas', 'location-dot']" class="text-secondary text-big" />
                <span class="ms-4">
                    <span v-if="Hometown"> From {{ Hometown.city }}</span>
                    <span v-else>Hometown not added yet.</span>
                </span>
            </div>
            <div v-if="Hometown">
                <font-awesome-icon v-if="Hometown.audience == '0'" :icon="['fas', 'earth-americas']" />
                <font-awesome-icon v-if="Hometown.audience =='1'" :icon="['fas', 'users']" />
                <font-awesome-icon v-if="Hometown.audience =='2'" :icon="['fas', 'lock']" />
            </div>
        </li>
        <li class="d-flex justify-content-between mt-3">
            <div class="d-flex align-items-center">
                <font-awesome-icon :icon="['fas', 'heart']" class="text-secondary text-big" />
                <span class="ms-3">{{ contact.relationship }}</span>
            </div>
            <font-awesome-icon v-if="contact.relationship_audience == '0'" :icon="['fas', 'earth-americas']" />
            <font-awesome-icon v-if="contact.relationship_audience == '1'" :icon="['fas', 'users']" />
            <font-awesome-icon v-if="contact.relationship_audience == '2'" :icon="['fas', 'lock']" />
        </li>
        <li class="d-flex justify-content-between mt-3">
            <div class="d-flex align-items-center">
                <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big" />
                <span class="ms-3">{{ contact.primary_phone_number }}</span>
            </div>
            <font-awesome-icon v-if="contact.primary_phone_number_audience == '0'" :icon="['fas', 'earth-americas']" />
            <font-awesome-icon v-if="contact.primary_phone_number_audience =='1'" :icon="['fas', 'users']" />
            <font-awesome-icon v-if="contact.primary_phone_number_audience == '2'" :icon="['fas', 'lock']" />
        </li>
    </ul>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
    name: "overview_section",
    setup() {
        const store = useStore();
        const contact = computed(() => store.state.profile);
        const Hometown = computed(() => store.getters.getHometown);
        const currentCity = computed(() => store.getters.getCurrentCity);
        const college = computed(() => store.getters.getLatestCollege);
        const workplace = computed(() => store.getters.getCurrentOrLatestWorkplace);
        return { contact, Hometown, currentCity, college, workplace };
    }
}
</script>
