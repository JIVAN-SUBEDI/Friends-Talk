<template>
  <div>
    <h5 class="mb-2">Places Lived</h5>
    <ul v-if="places.length">
      <li class="mt-2" v-for="place in places" :key="place.id" style="list-style: none">
        <div class="d-flex justify-content-between">
          <div class="d-flex align-items-center">
            <div class="d-flex flex-column">
              <span>{{ place.city }}</span>
              <span class="text-small text-secondary">
                <span v-if="place.type === 0">Hometown</span>
                <span v-else-if="place.type === 1">Current City</span>
                <span v-else>Moved on {{ place.moved }}</span>
              </span>
            </div>
          </div>
        </div>
      </li>
    </ul>
    <div class="text-center text-secondary mb-2" v-else>No places lived available!</div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: "about_places",
  setup() {
    const store = useStore();
    // Use a computed function to get the places from the Vuex store
    const places = computed(() => store.state.userProfile?.lived || []); // Default to an empty array

    return { places };
  },
};
</script>

<style scoped>
.edit-btn {
  padding: 5px 10px;
}
.edit-btn:hover {
  opacity: 0.8;
}
</style>
