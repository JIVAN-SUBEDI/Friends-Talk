<template>
    <ul>
        <li class="d-flex align-items-center">
            <div class="d-flex flex-grow-1">
                <font-awesome-icon :icon="['fas', 'suitcase']" class="text-secondary text-big me-3" />
                <div class=" flex-grow-1">
                    <span class="d-flex flex-column " v-if="workplace && workplace.name">
                        <span>{{ workplace.position }} at {{ workplace.name }}</span>
                        <span class="text-small text-secondary">{{ workplace.works_from }} to 
                            <span v-if="workplace.works_to == ''">Present</span>
                            <span v-else>{{ workplace.works_to }}</span>
                        </span>
                    </span>
                    <span v-else >
                        Not working yet
                    </span>
                </div>
            </div>
        </li>

        <li class="d-flex align-items-center mt-3">
            <font-awesome-icon :icon="['fas', 'graduation-cap']" class="text-secondary text-big me-3" />
            <div class=" flex-grow-1">
                <span v-if="college && college.message">{{ college.message }}</span>
                <span  v-else>None</span>
            </div>
        </li>

        <li class="d-flex align-items-center mt-3">
            <font-awesome-icon :icon="['fas', 'home']" class="text-secondary text-big me-3" />
            <div class="flex-grow-1">
                
                    <span v-if="currentCity"> From {{ currentCity.city }}</span>
                    <span v-else>None</span>
                
            </div>
        </li>

        <li class="d-flex align-items-center mt-3">
            <font-awesome-icon :icon="['fas', 'location-dot']" class="text-secondary text-big me-3" />
            <div class="flex-grow-1">
                <span >
                    <span v-if="hometown"> From {{ hometown.city }}</span>
                    <span v-else>None</span>
                </span>
            </div>
        </li>

        <li class="d-flex align-items-center mt-3">
            <font-awesome-icon :icon="['fas', 'heart']" class="text-secondary text-big me-3" />
            <div class="flex-grow-1">
                <span  v-if="info.relationship == null || info.relationship == ''">None</span>
                <span  v-else>{{ info.relationship }}</span>
            </div>
        </li>

        <li class="d-flex align-items-center mt-3">
            <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big me-3" />
            <div class="flex-grow-1">
                <span  v-if="info.primary_phone_number == null || info.primary_phone_number == ''">None</span>
                <span  v-else>{{ info.primary_phone_number }}</span>
            </div>
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
        const workplace = computed(() => store.state.userProfile?.latestWorkplace || {});
        const college = computed(() => store.state.userProfile?.latestCollage || {});
        const info = computed(() => store.state.userProfile?.basicInfo || {})
        const places = computed(() => store.state.userProfile?.lived || [])
        const currentCity = computed(() => places.value.find(place => place.type === 0) || {});
        const hometown = computed(() => places.value.find(place => place.type === 1) || {});

        return { workplace, college, info, places, currentCity, hometown }
    }
}
</script>
<style>
svg{
  width: 30px;
  height: 30px;  
}
</style>
