<template>
  <div class="layout overflow-hidden">
    <chat_navbarVue/>
    <chatSidebarVue/>
    <chatsVue/>
  </div>
  <chats_modalVue/>
</template>
<script>
import "@/assets/template.bundle.css";
import chatSidebarVue from "./partials/chatSidebar.vue";
import chatsVue from "./partials/chats.vue";
import chat_navbarVue from './partials/chat_navbar.vue';
import chats_modalVue from './partials/chats_modal.vue';
export default {
  name: "chat_page",
  components: { chat_navbarVue, chatSidebarVue,
     chatsVue,
     chats_modalVue },
};
</script>

