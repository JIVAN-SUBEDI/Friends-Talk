<template>
  <div>
      <!-- Workplace Section -->
      <h5 class="mb-2">Work</h5>

      <ul style="list-style: none;" v-if="workplaces.length">
          <li class="mt-2" v-for="workplace in workplaces" :key="workplace.id">
              <div class="d-flex justify-content-between">
                  <div class="d-flex align-items-center">
                      <div class="d-flex flex-column">
                          <span>{{ workplace.position }} at {{ workplace.name }}</span>
                          <span class="text-small text-secondary">{{ workplace.works_from }} to 
                              <span v-if="workplace.current">Present</span>
                              <span v-else>{{ workplace.works_to }}</span>,
                              <span>{{ workplace.address }}</span>
                          </span>
                      </div>
                  </div>
              </div>
          </li>
      </ul>
      <div class="text-center text-secondary mb-2" v-else>No workplace available!</div>

      <!-- College/School Section -->
      <h5 class="mb-2 mt-3">College/School</h5>

      <!-- List Colleges -->
      <ul style="list-style: none;" v-if="colleges.length">
          <li class="mt-2" v-for="college in colleges" :key="college.id">
              <div class="d-flex justify-content-between">
                  <div class="d-flex align-items-center">
                      <div class="d-flex flex-column">
                          <span>{{ college.name }}</span>
                          <span class="text-small text-secondary">{{ college.degree }}</span>
                          <span class="text-small text-secondary">
                              {{ college.address }} {{ college.attend_from }} to {{ college.attend_to }}
                          </span>
                      </div>
                  </div>
              </div>
          </li>
      </ul>
      <div class="text-center text-secondary mb-2" v-else>No college/School available!</div>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: "about_work",
  setup() {
      const store = useStore();
      
      // Wrap the state access in a function to properly create computed properties
      const colleges = computed(() => store.state.userProfile?.collage || []);
      const workplaces = computed(() => store.state.userProfile?.work || []);
      
      return { colleges, workplaces };
  }
}
</script>

<style>
.cursor-pointer {
  cursor: pointer;
}

.plus-button {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.plus-button:hover {
  text-decoration: underline;
}

.plus-button svg {
  font-size: 1.5rem;
}

.text-small {
  font-size: 0.8rem;
}

.text-big {
  font-size: 1.7rem;
}

.edit-btn {
  padding: 5px 10px;
}

.edit-btn:hover {
  opacity: 0.8;
}
</style>
