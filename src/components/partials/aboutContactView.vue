<template>
  <div>
    <h5>Basic Info</h5>
    <ul>
      <li class="d-flex align-items-center mt-2">
        <font-awesome-icon :icon="['fas', 'user']" class="text-secondary text-big me-3" />
        <div class="flex-grow-1">
          <span>Gender</span>
          <span v-if="info.gender == null || info.gender == ''" class="text-small text-secondary d-block">None</span>
          <span v-else class="text-small text-secondary d-block">{{ info.gender }}</span>
        </div>
      </li>

      <li class="d-flex align-items-center mt-2">
        <font-awesome-icon :icon="['fas', 'cake-candles']" class="text-secondary text-big me-3" />
        <div class="flex-grow-1">
          <span>Date of birth</span>
          <span v-if="info.date_of_birth == null || info.date_of_birth == ''" class="text-small text-secondary d-block">None</span>
          <span v-else class="text-small text-secondary d-block">{{ info.date_of_birth }}</span>
        </div>
      </li>

      <li class="d-flex align-items-center mt-2">
        <font-awesome-icon :icon="['fas', 'heart']" class="text-secondary text-big me-3" />
        <div class="flex-grow-1">
          <span>Relationship</span>
          <span v-if="info.relationship == null || info.relationship == ''" class="text-small text-secondary d-block">None</span>
          <span v-else class="text-small text-secondary d-block">{{ info.relationship }}</span>
        </div>
      </li>

      <li class="d-flex align-items-center mt-2">
        <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big me-3" />
        <div class="flex-grow-1">
          <span>Primary Phone Number</span>
          <span v-if="info.primary_phone_number == null || info.primary_phone_number == ''" class="text-small text-secondary d-block">None</span>
          <span v-else class="text-small text-secondary d-block">{{ info.primary_phone_number }}</span>
        </div>
      </li>

      <li class="d-flex align-items-center mt-2">
        <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big me-3" />
        <div class="flex-grow-1">
          <span>Secondary Phone Number</span>
          <span v-if="info.secondary_phone_number == null || info.secondary_phone_number == ''" class="text-small text-secondary d-block">None</span>
          <span v-else class="text-small text-secondary d-block">{{ info.secondary_phone_number }}</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: "about_contact",
  setup() {
    const store = useStore();
    const info = computed(() => store.state.userProfile?.basicInfo || {});
    return { info };
  }
};
</script>
<style scoped>
svg{
  width: 30px;
  height: 30px;  
}
</style>

