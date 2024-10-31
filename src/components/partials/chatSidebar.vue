<template>
  <aside class="sidebar bg-light">
    <div class="tab-content h-100" role="tablist">
      <!-- Create -->
      <div
        class="tab-pane fade h-100"
        id="tab-content-create-chat"
        role="tabpanel"
      >
        <div class="d-flex flex-column h-100">
          <div class="hide-scrollbar">
            <div class="container py-8">
              <!-- Title -->
              <div class="mb-8">
                <h5 class="fw-bold m-0">Create chat</h5>
              </div>

              <!-- Search -->
              <div class="mb-6">
                <div class="mb-5">
                  <div class="search">
                    <span class="search-icon"
                      ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
                    /></span>
                    <input type="text" placeholder="Search Friends" />
                  </div>
                </div>

                <ul class="nav nav-pills nav-justified" role="tablist">
                  <li class="nav-item">
                    <a
                      class="nav-link active"
                      data-bs-toggle="pill"
                      href="#create-chat-info"
                      role="tab"
                      aria-controls="create-chat-info"
                      aria-selected="true"
                    >
                      Details
                    </a>
                  </li>

                  <li class="nav-item">
                    <a
                      class="nav-link"
                      data-bs-toggle="pill"
                      href="#create-chat-members"
                      role="tab"
                      aria-controls="create-chat-members"
                      aria-selected="true"
                    >
                      People
                    </a>
                  </li>
                </ul>
              </div>

              <!-- Tabs content -->
              <div class="tab-content" role="tablist">
                <div
                  class="tab-pane fade show active"
                  id="create-chat-info"
                  role="tabpanel"
                >
                  <div class="card border-0">
                    <div class="profile">
                      <div class="profile-img text-primary rounded-top">
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          fill="currentColor"
                          viewBox="0 0 400 140.74"
                        >
                          <g>
                            <g>
                              <path
                                d="M400,125A1278.49,1278.49,0,0,1,0,125V0H400Z"
                              />
                              <path
                                class="cls-2"
                                d="M361.13,128c.07.83.15,1.65.27,2.46h0Q380.73,128,400,125V87l-1,0a38,38,0,0,0-38,38c0,.86,0,1.71.09,2.55C361.11,127.72,361.12,127.88,361.13,128Z"
                              />
                              <path
                                class="cls-2"
                                d="M12.14,119.53c.07.79.15,1.57.26,2.34v0c.13.84.28,1.66.46,2.48l.07.3c.18.8.39,1.59.62,2.37h0q33.09,4.88,66.36,8,.58-1,1.09-2l.09-.18a36.35,36.35,0,0,0,1.81-4.24l.08-.24q.33-.94.6-1.9l.12-.41a36.26,36.26,0,0,0,.91-4.42c0-.19,0-.37.07-.56q.11-.86.18-1.73c0-.21,0-.42,0-.63,0-.75.08-1.51.08-2.28a36.5,36.5,0,0,0-73,0c0,.83,0,1.64.09,2.45C12.1,119.15,12.12,119.34,12.14,119.53Z"
                              />
                              <circle
                                class="cls-2"
                                cx="94.5"
                                cy="57.5"
                                r="22.5"
                              />
                              <path
                                class="cls-2"
                                d="M276,0a43,43,0,0,0,43,43A43,43,0,0,0,362,0Z"
                              />
                            </g>
                          </g>
                        </svg>
                      </div>

                      <div class="profile-body p-0">
                        <div class="avatar avatar-lg">
                          <span class="avatar-text bg-primary">
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              width="24"
                              height="24"
                              viewBox="0 0 24 24"
                              fill="none"
                              stroke="currentColor"
                              stroke-width="2"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="feather feather-image"
                            >
                              <rect
                                x="3"
                                y="3"
                                width="18"
                                height="18"
                                rx="2"
                                ry="2"
                              ></rect>
                              <circle cx="8.5" cy="8.5" r="1.5"></circle>
                              <polyline points="21 15 16 10 5 21"></polyline>
                            </svg>
                          </span>

                          <div
                            class="badge badge-lg badge-circle bg-primary border-outline position-absolute bottom-0 end-0"
                          >
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              width="24"
                              height="24"
                              viewBox="0 0 24 24"
                              fill="none"
                              stroke="currentColor"
                              stroke-width="2"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="feather feather-plus"
                            >
                              <line x1="12" y1="5" x2="12" y2="19"></line>
                              <line x1="5" y1="12" x2="19" y2="12"></line>
                            </svg>
                          </div>

                          <input
                            id="upload-chat-img"
                            class="d-none"
                            type="file"
                          />
                          <label
                            class="stretched-label mb-0"
                            for="upload-chat-img"
                          ></label>
                        </div>
                      </div>
                    </div>

                    <div class="card-body">
                      <form autocomplete="off">
                        <div class="row gy-6">
                          <div class="col-12">
                            <div class="form-floating">
                              <input
                                type="text"
                                class="form-control"
                                id="floatingInput"
                                placeholder="Enter a chat name"
                              />
                              <label for="floatingInput"
                                >Enter group name</label
                              >
                            </div>
                          </div>
                          <div class="col-12 mt-2">
                            <div class="form-floating">
                              <textarea
                                class="form-control"
                                placeholder="Description"
                                id="floatingTextarea"
                                rows="8"
                                data-autosize="true"
                                style="min-height: 100px"
                              ></textarea>
                              <label for="floatingTextarea"
                                >What's your purpose?</label
                              >
                            </div>
                          </div>
                        </div>
                      </form>
                    </div>
                  </div>

                  <div class="d-flex align-items-center mt-4 px-6">
                    <small class="text-muted me-auto"
                      >Enter chat name and add an optional photo.</small
                    >
                  </div>

                  <!-- Options -->
                  <div class="mt-8">
                    <div class="d-flex align-items-center mb-4 px-6">
                      <small class="text-muted me-auto">Options</small>
                    </div>

                    <div class="card border-0">
                      <div class="card-body">
                        <div class="row gx-5">
                          <div class="col-auto">
                            <div class="btn btn-sm btn-icon btn-dark">
                              <svg
                                xmlns="http://www.w3.org/2000/svg"
                                width="24"
                                height="24"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                stroke-width="2"
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                class="feather feather-lock"
                              >
                                <rect
                                  x="3"
                                  y="11"
                                  width="18"
                                  height="11"
                                  rx="2"
                                  ry="2"
                                ></rect>
                                <path d="M7 11V7a5 5 0 0 1 10 0v4"></path>
                              </svg>
                            </div>
                          </div>
                          <div class="col">
                            <h5>Make Private</h5>
                            <p>Can only be viewed by invites</p>
                          </div>
                          <div class="col-auto align-self-center">
                            <div class="form-check form-switch ps-0">
                              <input
                                class="form-check-input"
                                type="checkbox"
                                id="new-chat-options-1"
                              />
                              <label
                                class="form-check-label"
                                for="new-chat-options-1"
                              ></label>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <!-- Members -->
                <div
                  class="tab-pane fade"
                  id="create-chat-members"
                  role="tabpanel"
                >
                  <nav>
                    <!-- Card -->
                    <div
                      class="card border-0 mt-5"
                      v-for="user in users"
                      :key="user.id"
                    >
                      <div class="card-body">
                        <div class="row align-items-center gx-5">
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
                            <h6>
                              {{
                                user.firstName +
                                " " +
                                user.middleName +
                                " " +
                                user.lastName
                              }}
                            </h6>
                            <p class="text-secondary small">
                              {{ user.status }}
                            </p>
                          </div>
                          <div class="col-auto">
                            <div class="form-check">
                              <input
                                class="form-check-input"
                                type="checkbox"
                                :value="user.id"
                                :id="'id-member-' + user.id"
                              />
                              <label
                                class="form-check-label"
                                :for="'id-member-' + user.id"
                              ></label>
                            </div>
                          </div>
                        </div>
                        <label
                          class="stretched-label"
                          :for="'id-member-' + user.id"
                        ></label>
                      </div>
                    </div>

                    <!-- Card -->
                  </nav>
                </div>
              </div>
              <!-- Tabs content -->
            </div>
          </div>

          <!-- Button -->
          <div class="container mt-n4 mb-8 position-relative">
            <button
              class="btn btn-lg btn-primary w-100 d-flex align-items-center"
              type="button"
              style="font-size: 1rem"
            >
              Start chat
              <span class="icon ms-auto">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  class="feather feather-chevron-right"
                >
                  <polyline points="9 18 15 12 9 6"></polyline>
                </svg>
              </span>
            </button>
          </div>
          <!-- Button -->
        </div>
      </div>

      <!-- Friends -->
      <div class="tab-pane fade h-100" id="tab-content-friends" role="tabpanel">
        <div class="d-flex flex-column h-100">
          <div class="hide-scrollbar">
            <div class="container py-8">
              <!-- Title -->
              <div class="mb-8">
                <h5 class="fw-bold m-0">Friends</h5>
              </div>

              <!-- Search -->
              <div class="mb-6">
                <div class="mb-5">
                  <div class="search">
                    <span class="search-icon"
                      ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
                    /></span>
                    <input type="text" placeholder="Search Friends" />
                  </div>
                </div>
              </div>

              <!-- List -->
              <div class="card-list">
                <div
                      class="card border-0 mt-5"
                      v-for="user in users"
                      :key="user.id"
                    >
                      <div class="card-body">
                        <div class="row align-items-center gx-5">
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
                            <h6>
                              {{
                                user.firstName +
                                " " +
                                user.middleName +
                                " " +
                                user.lastName
                              }}
                            </h6>
                            <p class="text-secondary small">
                              {{ user.status }}
                            </p>
                          </div>
                          <div class="col-auto">
                            <div class="dropdown">
                          <a
                            class="icon text-muted"
                            href="#"
                            role="button"
                            data-bs-toggle="dropdown"
                            aria-expanded="false"
                          >
                            <svg
                              xmlns="http://www.w3.org/2000/svg"
                              width="24"
                              height="24"
                              viewBox="0 0 24 24"
                              fill="none"
                              stroke="currentColor"
                              stroke-width="2"
                              stroke-linecap="round"
                              stroke-linejoin="round"
                              class="feather feather-more-vertical"
                            >
                              <circle cx="12" cy="12" r="1"></circle>
                              <circle cx="12" cy="5" r="1"></circle>
                              <circle cx="12" cy="19" r="1"></circle>
                            </svg>
                          </a>

                          <ul class="dropdown-menu">
                            <li>
                              <a class="dropdown-item" href="#">New message</a>
                            </li>
                           
                            <li>
                              <a class="dropdown-item text-danger" href="#"
                                >Block user</a
                              >
                            </li>
                          </ul>
                        </div>
                          </div>
                        </div>
                    
                      </div>
                    </div>
             
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Chats -->
      <div
        class="tab-pane fade h-100 show active"
        id="tab-content-chats"
        role="tabpanel"
      >
        <div class="d-flex flex-column h-100 position-relative">
          <div class="hide-scrollbar">
            <div class="container py-8">
              <!-- Title -->
              <div class="mb-8">
                <h5 class="fw-bold m-0">Chats</h5>
              </div>

              <!-- Search -->
              <div class="mb-6">
                <div class="mb-5">
                  <div class="search">
                    <span class="search-icon"
                      ><font-awesome-icon :icon="['fas', 'magnifying-glass']"
                    /></span>
                    <input type="text" placeholder="Search Friends" />
                  </div>
                </div>
              </div>
         

              <!-- Chats -->
              <div class="card-list">
              
                <chat_personVue   v-for="user in users"
                :key="user.id" :user="user"/>
                <!-- Card -->
               
                <!-- Card -->
              </div>
              <!-- Chats -->
            </div>
          </div>
        </div>
      </div>

      <!-- Settings -->
      <div
        class="tab-pane fade h-100"
        id="tab-content-settings"
        role="tabpanel"
      >
        <div class="d-flex flex-column h-100">
          <div class="hide-scrollbar">
            <div class="container py-8">
              <!-- Title -->
              <div class="mb-8">
                <h5 class="fw-bold m-0">Settings</h5>
              </div>

           

              <!-- Profile -->
              <div class="card border-0">
                <div class="card-body">
                  <div class="row align-items-center gx-5">
                    <div class="col-auto">
                      <div class="avatar">
                        <img
                          src="https://st2.depositphotos.com/2944867/8579/i/450/depositphotos_85791042-stock-photo-autumnal-in.jpg"
                          alt="#"
                          class="avatar-img"
                        />

                       
                        <input
                          id="upload-profile-photo"
                          class="d-none"
                          type="file"
                        />
                        <label
                          class="stretched-label mb-0"
                          for="upload-profile-photo"
                        ></label>
                      </div>
                    </div>
                    <div class="col">
                      <h6>William Pearson</h6>
                      <p class="text-secondary small">wright@studio.com</p>
                    </div>
                    <div class="col-auto">
                      <a href="#" class="text-muted">
                        <div class="icon">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            width="24"
                            height="24"
                            viewBox="0 0 24 24"
                            fill="none"
                            stroke="currentColor"
                            stroke-width="2"
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            class="feather feather-log-out"
                          >
                            <path
                              d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"
                            ></path>
                            <polyline points="16 17 21 12 16 7"></polyline>
                            <line x1="21" y1="12" x2="9" y2="12"></line>
                          </svg>
                        </div>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Profile -->

              <!-- Storage -->
              <div class="mt-8">
                <div class="d-flex align-items-center my-4 px-6">
                  <small class="text-muted me-auto">Storage</small>

                  <div class="flex align-items-center text-muted">
                    <a href="#" class="text-muted small">Clear storage</a>

                    <div class="icon icon-xs">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="feather feather-bar-chart-2"
                      >
                        <line x1="18" y1="20" x2="18" y2="10"></line>
                        <line x1="12" y1="20" x2="12" y2="4"></line>
                        <line x1="6" y1="20" x2="6" y2="14"></line>
                      </svg>
                    </div>
                  </div>
                </div>

                <div class="card border-0">
                  <div class="card-body py-2">
                    <!-- Accordion -->
                    <div
                      class="accordion accordion-flush"
                      id="accordion-storage"
                    >
                    

                      <div class="accordion-item">
                        <div class="accordion-header">
                          <div class="row align-items-center">
                            <div class="col">
                              <h6>Keep media</h6>
                              <p class="text-secondary small">Photos, videos and other files</p>
                            </div>
                            <div class="col-auto">
                              <div class="form-check form-switch">
                                <input
                                  class="form-check-input"
                                  type="checkbox"
                                  id="accordion-storage-check-1"
                                />
                                <label
                                  class="form-check-label"
                                  for="accordion-storage-check-1"
                                ></label>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Storage -->

              <!-- Notifications -->
              <div class="mt-8">
                <div class="d-flex align-items-center my-4 px-6">
                  <small class="text-muted me-auto">Notifications</small>
                </div>

                <!-- Accordion -->
                <div class="card border-0">
                  <div class="card-body py-2">
                    <div
                      class="accordion accordion-flush"
                      id="accordion-notifications"
                    >
                      <div class="accordion-item">
                        <div
                          class="accordion-header"
                          id="accordion-notifications-1"
                        >
                          <a
                            href="#"
                            class="accordion-button text-reset collapsed"
                            data-bs-toggle="collapse"
                            data-bs-target="#accordion-notifications-body-1"
                            aria-expanded="false"
                            aria-controls="accordion-notifications-body-1"
                          >
                            <div>
                              <h6>Message</h6>
                              <p class="text-secondary small">Set custom notifications for users</p>
                            </div>
                          </a>
                        </div>

                        <div
                          id="accordion-notifications-body-1"
                          class="accordion-collapse collapse"
                          aria-labelledby="accordion-notifications-1"
                          data-parent="#accordion-notifications"
                        >
                          <div class="accordion-body">
                            <div class="row align-items-center">
                              <div class="col">
                                <h6>Text</h6>
                                <p class="text-secondary small">Show text in notifications</p>
                              </div>

                              <div class="col-auto">
                                <div class="form-check form-switch">
                                  <input
                                    class="form-check-input"
                                    type="checkbox"
                                    id="accordion-notifications-check-1"
                                  />
                                  <label
                                    class="form-check-label"
                                    for="accordion-notifications-check-1"
                                  ></label>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>

                      <div class="accordion-item">
                        <div class="accordion-header">
                          <div class="row align-items-center">
                            <div class="col">
                              <h6>Sound</h6>
                              <p class="text-secondary small">Enable sound notifications</p>
                            </div>
                            <div class="col-auto">
                              <div class="form-check form-switch">
                                <input
                                  class="form-check-input"
                                  type="checkbox"
                                  id="accordion-notifications-check-3"
                                />
                                <label
                                  class="form-check-label"
                                  for="accordion-notifications-check-3"
                                ></label>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>

                      <div class="accordion-item">
                        <div class="accordion-header">
                          <div class="row align-items-center">
                            <div class="col">
                              <h6>Browser notifications</h6>
                              <p class="text-secondary small">Enable browser notifications</p>
                            </div>
                            <div class="col-auto">
                              <div class="form-check form-switch">
                                <input
                                  class="form-check-input"
                                  type="checkbox"
                                  id="accordion-notifications-check-2"
                                  checked
                                />
                                <label
                                  class="form-check-label"
                                  for="accordion-notifications-check-2"
                                ></label>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- Notifications -->

              <!-- Devices -->
              <div class="mt-8">
                <div class="d-flex align-items-center my-4 px-6">
                  <small class="text-muted me-auto">Devices</small>

                  <div class="flex align-items-center text-muted">
                    <a href="#" class="text-muted small">End all sessions</a>

                    <div class="icon icon-xs">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        stroke-width="2"
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        class="feather feather-log-out"
                      >
                        <path
                          d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"
                        ></path>
                        <polyline points="16 17 21 12 16 7"></polyline>
                        <line x1="21" y1="12" x2="9" y2="12"></line>
                      </svg>
                    </div>
                  </div>
                </div>

                <div class="card border-0">
                  <div class="card-body py-3">
                    <ul class="list-group list-group-flush">
                      <li class="list-group-item">
                        <div class="row align-items-center">
                          <div class="col">
                            <h6>Windows ⋅ USA, Houston</h6>
                            <p class="text-secondary small">Today at 2:48 pm ⋅ Browser: Chrome</p>
                          </div>
                          <div class="col-auto">
                            <span class="text-primary extra-small">active</span>
                          </div>
                        </div>
                      </li>

                      <li class="list-group-item">
                        <div class="row align-items-center">
                          <div class="col">
                            <h6>iPhone ⋅ USA, Houston</h6>
                            <p class="text-secondary small">Yesterday at 2:48 pm ⋅ Browser: Chrome</p>
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>
              </div>
              <!-- Devices -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </aside>
</template>
<script>
import { ref } from "vue";

import chat_personVue from './chat_person.vue';
export default {
  name: "chat_sidebar",
  components:{chat_personVue},
  setup() {
    const users = ref([
      {
        id: 1,
        firstName: "John",
        middleName: "A.",
        lastName: "Doe",
        lastOnline: "2024-08-24T14:30:00Z",
        messageDetails: {
          message: "Hey, how are you?",
          time: "2024-08-24T14:31:00Z",
        },
        status: "online",
        image:
          "https://st2.depositphotos.com/2944867/8579/i/450/depositphotos_85791042-stock-photo-autumnal-in.jpg",
      },
      {
        id: 2,
        firstName: "Jane",
        middleName: "B.",
        lastName: "Smith",
        lastOnline: "2024-08-24T13:45:00Z",
        messageDetails: {
          message: "Let's catch up later.",
          time: "2024-08-24T13:46:00Z",
        },
        status: "offline",
        image: "",
      },
      {
        id: 3,
        firstName: "Michael",
        middleName: "",
        lastName: "Johnson",
        lastOnline: "2024-08-24T09:20:00Z",
        messageDetails: {
          message: "Meeting at 3 PM?",
          time: "2024-08-24T09:25:00Z",
          status: "offline",
        },
        image:
          "https://st2.depositphotos.com/2944867/8579/i/450/depositphotos_85791042-stock-photo-autumnal-in.jpg",
      },
      {
        id: 4,
        firstName: "Emily",
        middleName: "C.",
        lastName: "Davis",
        lastOnline: "2024-08-24T11:50:00Z",
        messageDetails: {
          message: "I'll send the report soon.",
          time: "2024-08-24T11:55:00Z",
        },
        status: "offline",
        image: "",
      },
      {
        id: 5,
        firstName: "David",
        middleName: "E.",
        lastName: "Miller",
        lastOnline: "2024-08-24T10:15:00Z",
        messageDetails: {
          message: "Can you join the call?",
          time: "2024-08-24T10:20:00Z",
        },
        image:
          "https://st2.depositphotos.com/2944867/8579/i/450/depositphotos_85791042-stock-photo-autumnal-in.jpg",
        status: "online",
      },
    ]);
    return { users };
  },
};
</script>
<style scoped>
a {
  text-decoration: none;
}
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
