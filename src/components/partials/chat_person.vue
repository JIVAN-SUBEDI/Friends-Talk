<template>
  <a href="chat-direct.html" class="card border-0 text-reset">
    <div class="card-body">
      <div class="row gx-5">
        <div class="col-auto">
          <div
            class="avatar"
            :class="{
              'avatar-online': user.status === 'online',
            }"
          >
            <img
              class="avatar-img"
              :src="user.image"
              alt="User Image"
              v-if="user.image !== ''"
            />
            <span v-else class="avatar-text">
              {{ user.firstName.charAt(0) }}
            </span>
          </div>
        </div>

        <div class="col">
          <div class="d-flex align-items-center mb-3">
            <h6 class="me-auto mb-0">
              {{ user.firstName + " " + user.middleName + " " + user.lastName }}
            </h6>
            <span class="text-muted extra-small ms-2">08:45 PM</span>
          </div>

          <div class="d-flex align-items-center">
            <div class="line-clamp me-auto text-small text-secondary">
              {{ user.messageDetails.message }}
            </div>

            <div class="badge badge-circle bg-primary ms-5">
              <span v-if="user.messageDetails.unseenMessages > 0">{{
                user.messageDetails.unseenMessages
              }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- .card-body -->
  </a>
</template>
<script>
export default {
  name: "chat_person",
  props: ["user"],
};
</script>
<style scoped>
.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}
.avatar .avatar-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}
</style>
