<template>
  <main class="main is-visible" data-dropzone-area="">
    <div class="container h-100">
      <div class="d-flex flex-column h-100 position-relative">
        <!-- Chat: Header -->
        <div class="chat-header border-bottom py-3">
          <div class="row align-items-center">
            <!-- Mobile: close -->
            <div class="col-2 d-xl-none">
              <a class="icon icon-lg text-muted" href="#" data-toggle-chat="">
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
                  class="feather feather-chevron-left"
                >
                  <polyline points="15 18 9 12 15 6"></polyline>
                </svg>
              </a>
            </div>
            <!-- Mobile: close -->

            <!-- Content -->
            <div class="col-8 col-xl-12">
              <div class="row align-items-center text-center text-xl-start">
                <!-- Title -->
                <div class="col-12 col-xl-6">
                  <div class="row align-items-center gx-5">
                    <div class="col-auto">
                      <div
                        class="avatar avatar-online d-none d-xl-inline-block"
                      >
                        <img
                          class="avatar-img"
                          src="https://images.pexels.com/photos/341970/pexels-photo-341970.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
                          alt=""
                        />
                      </div>
                    </div>

                    <div class="col overflow-hidden">
                      <h5 class="text-truncate">Ollie Chandler</h5>
                      <p class="text-truncate text-small">
                        Typing<span class="typing-dots"
                          ><span>.</span><span>.</span><span>.</span></span
                        >
                      </p>
                    </div>
                  </div>
                </div>
                <!-- Title -->

                <!-- Toolbar -->
                <div class="col-xl-6 d-none d-xl-block">
                  <div class="row align-items-center justify-content-end gx-6">
                    <div class="col-auto">
                      <a
                        href="#"
                        class="icon icon-lg text-muted"
                        data-bs-toggle="offcanvas"
                        data-bs-target="#offcanvas-more"
                        aria-controls="offcanvas-more"
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
                          class="feather feather-more-horizontal"
                        >
                          <circle cx="12" cy="12" r="1"></circle>
                          <circle cx="19" cy="12" r="1"></circle>
                          <circle cx="5" cy="12" r="1"></circle>
                        </svg>
                      </a>
                    </div>
                  </div>
                </div>
                <!-- Toolbar -->
              </div>
            </div>
            <!-- Content -->

            <!-- Mobile: more -->
            <div class="col-2 d-xl-none text-end">
              <a
                href="#"
                class="icon icon-lg text-muted"
                data-bs-toggle="offcanvas"
                data-bs-target="#offcanvas-more"
                aria-controls="offcanvas-more"
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
            </div>
            <!-- Mobile: more -->
          </div>
        </div>
        <!-- Chat: Header -->

        <!-- Chat: Content -->
        <div class="chat-body hide-scrollbar flex-1 h-100">
          <div class="chat-body-inner">
            <div class="py-6 py-lg-12">
              <!-- Message -->
              <div v-for="(msg, index) in messages" :key="index">
                <div
                  class="message"
                  :class="{ 'message-out': msg.messageType === 'out' }"
                >
                  <a
                    href="#"
                    data-bs-toggle="modal"
                    data-bs-target="#modal-user-profile"
                    class="avatar avatar-responsive"
                  >
                    <img
                      class="avatar-img"
                      src="https://images.pexels.com/photos/341970/pexels-photo-341970.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1"
                      alt=""
                    />
                  </a>

                  <div class="message-inner">
                    <div class="message-body">
                      <div class="message-content" v-for="message in msg.messages" :key="message.id">
                        <div class="message-text">
                          <blockquote class="blockquote overflow-hidden" v-if="message.repliedTo !== null">
                       
                          <p class="small text-truncate">
                              {{ message.repliedDetails.message }}
                          </p>
                        </blockquote>
                          <p>
                            {{ message.message }}
                          </p>
                        </div>

                        <!-- Dropdown -->
                        <div class="message-action">
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
                                <a
                                  class="dropdown-item d-flex align-items-center"
                                  href="#"
                                >
                                  <span class="me-auto">Reply</span>
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
                                      class="feather feather-corner-up-left"
                                    >
                                      <polyline
                                        points="9 14 4 9 9 4"
                                      ></polyline>
                                      <path
                                        d="M20 20v-7a4 4 0 0 0-4-4H4"
                                      ></path>
                                    </svg>
                                  </div>
                                </a>
                              </li>
                    
                              <li>
                                <a
                                  class="dropdown-item d-flex align-items-center text-danger"
                                  href="#"
                                >
                                  <span class="me-auto">Delete</span>
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
                                      class="feather feather-trash-2"
                                    >
                                      <polyline
                                        points="3 6 5 6 21 6"
                                      ></polyline>
                                      <path
                                        d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                                      ></path>
                                      <line
                                        x1="10"
                                        y1="11"
                                        x2="10"
                                        y2="17"
                                      ></line>
                                      <line
                                        x1="14"
                                        y1="11"
                                        x2="14"
                                        y2="17"
                                      ></line>
                                    </svg>
                                  </div>
                                </a>
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                     
                    </div>

                    <div class="message-footer">
                      <span class="extra-small text-muted">{{getTime(msg.added)}}</span>
                    </div>
                  </div>
                </div>
                <!-- Divider -->
                 <!-- {{dividerCheck}} -->
                <!-- <div class="message-divider" v-if="dividerCheck === false">
                  <small class="text-muted">{{ getDate(msg.added) }}</small>
                </div> -->
              </div>
            </div>
          </div>
        </div>
        <!-- Chat: Content -->

        <!-- Chat: Footer -->
        <div
          class="chat-footer pb-3 pb-lg-7 position-absolute bottom-0 start-0 px-4"
        >
          <!-- Chat: Files -->
          <div
            class="dz-preview bg-dark"
            id="dz-preview-row"
            data-horizontal-scroll=""
          ></div>
          <!-- Chat: Files -->

          <!-- Chat: Form -->
          <form class="chat-form rounded-pill bg-light" data-emoji-form="">
            <div class="row d-flex align-items-center gx-0">
              <div class="col-auto d-flex align-items-center">
                <a
                  href="#"
                  class="btn btn-icon btn-link text-body rounded-circle d-flex align-items-center"
                  id="dz-btn"
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
                    class="feather feather-paperclip"
                  >
                    <path
                      d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"
                    ></path>
                  </svg>
                </a>
              </div>

              <div class="col">
                <div class="d-flex align-items-center">
                  <textarea
                    class="px-0"
                    placeholder="Type your message..."
                    rows="1"
                    data-emoji-input=""
                    data-autosize="true"
                  ></textarea>

                  <a
                    href="#"
                    class="input-group-text text-body pe-0"
                    data-emoji-btn=""
                  >
                    <span class="icon icon-lg">
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
                        class="feather feather-smile"
                      >
                        <circle cx="12" cy="12" r="10"></circle>
                        <path d="M8 14s1.5 2 4 2 4-2 4-2"></path>
                        <line x1="9" y1="9" x2="9.01" y2="9"></line>
                        <line x1="15" y1="9" x2="15.01" y2="9"></line>
                      </svg>
                    </span>
                  </a>
                </div>
              </div>

              <div class="col-auto">
                <button class="btn btn-icon btn-primary rounded-circle ms-5">
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
                    class="feather feather-send"
                  >
                    <line x1="22" y1="2" x2="11" y2="13"></line>
                    <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                  </svg>
                </button>
              </div>
            </div>
          </form>
          <!-- Chat: Form -->
        </div>
        <!-- Chat: Footer -->
      </div>
    </div>
  </main>
  <!-- Chat -->

  <!-- Chat: Info -->
  <div
    class="offcanvas offcanvas-end offcanvas-aside"
    data-bs-scroll="true"
    data-bs-backdrop="false"
    tabindex="-1"
    id="offcanvas-more"
  >
    <!-- Offcanvas Header -->
    <div class="offcanvas-header py-4 py-lg-7 border-bottom">
      <a class="icon icon-lg text-muted" href="#" data-bs-dismiss="offcanvas">
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
          class="feather feather-chevron-left"
        >
          <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
      </a>

      <div class="visibility-xl-invisible overflow-hidden text-center">
        <h5 class="text-truncate">Ollie Chandler</h5>
        <p class="text-truncate">last seen 5 minutes ago</p>
      </div>

      <!-- Dropdown -->
      <div class="dropdown">
        <a
          class="icon icon-lg text-muted"
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
            <a href="#" class="dropdown-item d-flex align-items-center">
              Edit
              <div class="icon ms-auto">
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
                  class="feather feather-edit-3"
                >
                  <path d="M12 20h9"></path>
                  <path
                    d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"
                  ></path>
                </svg>
              </div>
            </a>
          </li>
          <li>
            <a href="#" class="dropdown-item d-flex align-items-center">
              Mute
              <div class="icon ms-auto">
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
                  class="feather feather-bell"
                >
                  <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                  <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                </svg>
              </div>
            </a>
          </li>
          <li>
            <hr class="dropdown-divider" />
          </li>
          <li>
            <a
              href="#"
              class="dropdown-item d-flex align-items-center text-danger"
            >
              Leave
              <div class="icon ms-auto">
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
                  <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path>
                  <polyline points="16 17 21 12 16 7"></polyline>
                  <line x1="21" y1="12" x2="9" y2="12"></line>
                </svg>
              </div>
            </a>
          </li>
        </ul>
      </div>
    </div>
    <!-- Offcanvas Header -->

    <!-- Offcanvas Body -->
    <div class="offcanvas-body hide-scrollbar">
      <!-- Avatar -->
      <div class="text-center py-10">
        <div class="row gy-6">
          <div class="col-12">
            <div class="avatar avatar-xl mx-auto">
              <img src="https://images.pexels.com/photos/341970/pexels-photo-341970.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1" alt="#" class="avatar-img" />

              <a
                href="#"
                class="badge badge-lg badge-circle bg-primary text-white border-outline position-absolute bottom-0 end-0"
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
              </a>
            </div>
          </div>

          <div class="col-12">
            <h5>Ollie Chandler</h5>
           
          </div>
        </div>
      </div>
      <!-- Avatar -->

      <!-- Tabs -->
      <ul class="nav nav-pills nav-justified" role="tablist">
        <li class="nav-item">
          <a
            class="nav-link active"
            data-bs-toggle="pill"
            href="#offcanvas-tab-profile"
            role="tab"
            aria-controls="offcanvas-tab-profile"
            aria-selected="true"
          >
            Profile
          </a>
        </li>

        <li class="nav-item">
          <a
            class="nav-link"
            data-bs-toggle="pill"
            href="#offcanvas-tab-media"
            role="tab"
            aria-controls="offcanvas-tab-media"
            aria-selected="true"
          >
            Media
          </a>
        </li>

        <li class="nav-item">
          <a
            class="nav-link"
            data-bs-toggle="pill"
            href="#offcanvas-tab-files"
            role="tab"
            aria-controls="offcanvas-tab-files"
            aria-selected="false"
          >
            Files
          </a>
        </li>
      </ul>
      <!-- Tabs -->

      <!-- Tabs: Content -->
      <div class="tab-content py-2" role="tablist">
        <!-- Profile -->
        <div
          class="tab-pane fade show active"
          id="offcanvas-tab-profile"
          role="tabpanel"
        >
          <ul class="list-group list-group-flush">
            <li class="list-group-item">
              <div class="row align-items-center gx-6">
                <div class="col">
                  <h6>Phone</h6>
                  <p class="text-secondary">1-800-275-2273</p>
                </div>

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
                      class="feather feather-phone-call"
                    >
                      <path
                        d="M15.05 5A5 5 0 0 1 19 8.95M15.05 1A9 9 0 0 1 23 8.94m-1 7.98v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"
                      ></path>
                    </svg>
                  </div>
                </div>
              </div>
            </li>

            <li class="list-group-item">
              <div class="row align-items-center gx-6">
                <div class="col">
                  <h6>Location</h6>
                  <p class="text-secondary">USA, Houston</p>
                </div>

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
                      class="feather feather-globe"
                    >
                      <circle cx="12" cy="12" r="10"></circle>
                      <line x1="2" y1="12" x2="22" y2="12"></line>
                      <path
                        d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"
                      ></path>
                    </svg>
                  </div>
                </div>
              </div>
            </li>

            <li class="list-group-item">
              <div class="row align-items-center gx-6">
                <div class="col">
                  <h6>E-mail</h6>
                  <p class="text-secondary">chandler@ollie.com</p>
                </div>

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
                      class="feather feather-mail"
                    >
                      <path
                        d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"
                      ></path>
                      <polyline points="22,6 12,13 2,6"></polyline>
                    </svg>
                  </div>
                </div>
              </div>
            </li>
          </ul>

          <ul class="list-group list-group-flush border-top mt-8">
            <li class="list-group-item">
              <div class="row align-items-center gx-6">
                <div class="col">
                  <h6>Notifications</h6>
                  <p class="text-secondary">Enable sound notifications</p>
                </div>

                <div class="col-auto">
                  <div class="form-check form-switch">
                    <input
                      class="form-check-input"
                      type="checkbox"
                      id="accordion-security-check-5"
                    />
                    <label
                      class="form-check-label"
                      for="accordion-security-check-5"
                    ></label>
                  </div>
                </div>
              </div>
            </li>
          </ul>

          <ul class="list-group list-group-flush border-top mt-8">
         

            <li class="list-group-item">
              <a href="#" class="text-danger">Delete Chat</a>
            </li>
          </ul>
        </div>
        <!-- Profile -->

        <!-- Media -->
        <div class="tab-pane fade" id="offcanvas-tab-media" role="tabpanel">
          <div class="row row-cols-3 g-3 py-6">
            <div class="col" v-for="image in images" :key="image">
              <a
                href="#"
                data-bs-toggle="modal"
                data-bs-target="#modal-media-preview"
                :data-theme-img-url="image.image"
              >
                <img
                  class="img-fluid rounded"
                  :src="image.image"
                  alt=""
                />
              </a>
            </div>
          </div>
        </div>
        <!-- Media -->

        <!-- Files -->
        <div class="tab-pane fade" id="offcanvas-tab-files" role="tabpanel">
          <ul class="list-group list-group-flush">
            <!-- Item -->
            <li class="list-group-item">
              <div class="row align-items-center gx-5">
                <!-- Icons -->
                <div class="col-auto">
                  <div class="avatar-group">
                    <a href="#" class="avatar avatar-sm">
                      <img
                        src="assets/img/avatars/2.jpg"
                        class="avatar-img"
                        alt="#"
                      />
                    </a>

                    <a href="#" class="avatar avatar-sm">
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
                          class="feather feather-file-text"
                        >
                          <path
                            d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
                          ></path>
                          <polyline points="14 2 14 8 20 8"></polyline>
                          <line x1="16" y1="13" x2="8" y2="13"></line>
                          <line x1="16" y1="17" x2="8" y2="17"></line>
                          <polyline points="10 9 9 9 8 9"></polyline>
                        </svg>
                      </span>
                    </a>
                  </div>
                </div>
                <!-- Icons -->

                <!-- Text -->
                <div class="col overflow-hidden">
                  <h5 class="text-truncate">
                    <a href="#">E5419783-047D-4B4C-B30E-F24DD8247731.JPG</a>
                  </h5>
                  <ul class="list-inline m-0">
                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">79.2 KB</small>
                    </li>

                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">txt</small>
                    </li>
                  </ul>
                </div>
                <!-- Text -->

                <!-- Dropdown -->
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
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Download
                          <div class="icon ms-auto">
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
                              class="feather feather-download"
                            >
                              <path
                                d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
                              ></path>
                              <polyline points="7 10 12 15 17 10"></polyline>
                              <line x1="12" y1="15" x2="12" y2="3"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Share
                          <div class="icon ms-auto">
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
                              class="feather feather-share-2"
                            >
                              <circle cx="18" cy="5" r="3"></circle>
                              <circle cx="6" cy="12" r="3"></circle>
                              <circle cx="18" cy="19" r="3"></circle>
                              <line
                                x1="8.59"
                                y1="13.51"
                                x2="15.42"
                                y2="17.49"
                              ></line>
                              <line
                                x1="15.41"
                                y1="6.51"
                                x2="8.59"
                                y2="10.49"
                              ></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li><hr class="dropdown-divider" /></li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center text-danger"
                          href="#"
                        >
                          <span class="me-auto">Delete</span>
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
                              class="feather feather-trash-2"
                            >
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path
                                d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                              ></path>
                              <line x1="10" y1="11" x2="10" y2="17"></line>
                              <line x1="14" y1="11" x2="14" y2="17"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Dropdown -->
              </div>
            </li>

            <!-- Item -->
            <li class="list-group-item">
              <div class="row align-items-center gx-5">
                <!-- Icons-->
                <div class="col-auto">
                  <div class="avatar-group">
                    <a href="#" class="avatar avatar-sm">
                      <img
                        class="avatar-img"
                        src="assets/img/avatars/1.jpg"
                        alt="#"
                      />
                    </a>

                    <a href="#" class="avatar avatar-sm">
                      <span class="avatar-text bg-warning">
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
                          class="feather feather-film"
                        >
                          <rect
                            x="2"
                            y="2"
                            width="20"
                            height="20"
                            rx="2.18"
                            ry="2.18"
                          ></rect>
                          <line x1="7" y1="2" x2="7" y2="22"></line>
                          <line x1="17" y1="2" x2="17" y2="22"></line>
                          <line x1="2" y1="12" x2="22" y2="12"></line>
                          <line x1="2" y1="7" x2="7" y2="7"></line>
                          <line x1="2" y1="17" x2="7" y2="17"></line>
                          <line x1="17" y1="17" x2="22" y2="17"></line>
                          <line x1="17" y1="7" x2="22" y2="7"></line>
                        </svg>
                      </span>
                    </a>
                  </div>
                </div>
                <!-- Icons -->

                <!-- Text -->
                <div class="col overflow-hidden">
                  <h5 class="text-truncate">
                    <a href="#">E5419783-047D-4B4C-B30E-F24DD8247731.JPG</a>
                  </h5>
                  <ul class="list-inline m-0">
                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">54.2 KB</small>
                    </li>

                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">mp4</small>
                    </li>
                  </ul>
                </div>
                <!-- Text -->

                <!-- Dropdown -->
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
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Download
                          <div class="icon ms-auto">
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
                              class="feather feather-download"
                            >
                              <path
                                d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
                              ></path>
                              <polyline points="7 10 12 15 17 10"></polyline>
                              <line x1="12" y1="15" x2="12" y2="3"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Share
                          <div class="icon ms-auto">
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
                              class="feather feather-share-2"
                            >
                              <circle cx="18" cy="5" r="3"></circle>
                              <circle cx="6" cy="12" r="3"></circle>
                              <circle cx="18" cy="19" r="3"></circle>
                              <line
                                x1="8.59"
                                y1="13.51"
                                x2="15.42"
                                y2="17.49"
                              ></line>
                              <line
                                x1="15.41"
                                y1="6.51"
                                x2="8.59"
                                y2="10.49"
                              ></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li><hr class="dropdown-divider" /></li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center text-danger"
                          href="#"
                        >
                          <span class="me-auto">Delete</span>
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
                              class="feather feather-trash-2"
                            >
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path
                                d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                              ></path>
                              <line x1="10" y1="11" x2="10" y2="17"></line>
                              <line x1="14" y1="11" x2="14" y2="17"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Dropdown -->
              </div>
            </li>

            <!-- Item -->
            <li class="list-group-item">
              <div class="row align-items-center gx-5">
                <!-- Icons -->
                <div class="col-auto">
                  <div class="avatar-group">
                    <a href="#" class="avatar avatar-sm">
                      <img
                        class="avatar-img"
                        src="assets/img/avatars/2.jpg"
                        alt="#"
                      />
                    </a>

                    <a href="#" class="avatar avatar-sm">
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
                          class="feather feather-file-text"
                        >
                          <path
                            d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
                          ></path>
                          <polyline points="14 2 14 8 20 8"></polyline>
                          <line x1="16" y1="13" x2="8" y2="13"></line>
                          <line x1="16" y1="17" x2="8" y2="17"></line>
                          <polyline points="10 9 9 9 8 9"></polyline>
                        </svg>
                      </span>
                    </a>
                  </div>
                </div>
                <!-- Icons -->

                <!-- Text -->
                <div class="col overflow-hidden">
                  <h5 class="text-truncate">
                    <a href="#">E5419783-047D-4B4C-B30E-F24DD8247731.JPG</a>
                  </h5>
                  <ul class="list-inline m-0">
                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">64.8 KB</small>
                    </li>

                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">jpg</small>
                    </li>
                  </ul>
                </div>
                <!-- Text -->

                <!-- Dropdown -->
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
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Download
                          <div class="icon ms-auto">
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
                              class="feather feather-download"
                            >
                              <path
                                d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
                              ></path>
                              <polyline points="7 10 12 15 17 10"></polyline>
                              <line x1="12" y1="15" x2="12" y2="3"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Share
                          <div class="icon ms-auto">
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
                              class="feather feather-share-2"
                            >
                              <circle cx="18" cy="5" r="3"></circle>
                              <circle cx="6" cy="12" r="3"></circle>
                              <circle cx="18" cy="19" r="3"></circle>
                              <line
                                x1="8.59"
                                y1="13.51"
                                x2="15.42"
                                y2="17.49"
                              ></line>
                              <line
                                x1="15.41"
                                y1="6.51"
                                x2="8.59"
                                y2="10.49"
                              ></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li><hr class="dropdown-divider" /></li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center text-danger"
                          href="#"
                        >
                          <span class="me-auto">Delete</span>
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
                              class="feather feather-trash-2"
                            >
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path
                                d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                              ></path>
                              <line x1="10" y1="11" x2="10" y2="17"></line>
                              <line x1="14" y1="11" x2="14" y2="17"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Dropdown -->
              </div>
            </li>

            <!-- Item -->
            <li class="list-group-item">
              <div class="row align-items-center gx-5">
                <!-- Icons-->
                <div class="col-auto">
                  <div class="avatar-group">
                    <a href="#" class="avatar avatar-sm">
                      <img
                        class="avatar-img"
                        src="assets/img/avatars/1.jpg"
                        alt="#"
                      />
                    </a>

                    <a href="#" class="avatar avatar-sm">
                      <span class="avatar-text bg-warning">
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
                          class="feather feather-film"
                        >
                          <rect
                            x="2"
                            y="2"
                            width="20"
                            height="20"
                            rx="2.18"
                            ry="2.18"
                          ></rect>
                          <line x1="7" y1="2" x2="7" y2="22"></line>
                          <line x1="17" y1="2" x2="17" y2="22"></line>
                          <line x1="2" y1="12" x2="22" y2="12"></line>
                          <line x1="2" y1="7" x2="7" y2="7"></line>
                          <line x1="2" y1="17" x2="7" y2="17"></line>
                          <line x1="17" y1="17" x2="22" y2="17"></line>
                          <line x1="17" y1="7" x2="22" y2="7"></line>
                        </svg>
                      </span>
                    </a>
                  </div>
                </div>
                <!-- Icons-->

                <!-- Text -->
                <div class="col overflow-hidden">
                  <h5 class="text-truncate">
                    <a href="#">E5419783-047D-4B4C-B30E-F24DD8247731.JPG</a>
                  </h5>
                  <ul class="list-inline m-0">
                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">80.8 KB</small>
                    </li>

                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">mp4</small>
                    </li>
                  </ul>
                </div>
                <!-- Text -->

                <!-- Dropdown -->
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
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Download
                          <div class="icon ms-auto">
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
                              class="feather feather-download"
                            >
                              <path
                                d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
                              ></path>
                              <polyline points="7 10 12 15 17 10"></polyline>
                              <line x1="12" y1="15" x2="12" y2="3"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Share
                          <div class="icon ms-auto">
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
                              class="feather feather-share-2"
                            >
                              <circle cx="18" cy="5" r="3"></circle>
                              <circle cx="6" cy="12" r="3"></circle>
                              <circle cx="18" cy="19" r="3"></circle>
                              <line
                                x1="8.59"
                                y1="13.51"
                                x2="15.42"
                                y2="17.49"
                              ></line>
                              <line
                                x1="15.41"
                                y1="6.51"
                                x2="8.59"
                                y2="10.49"
                              ></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li><hr class="dropdown-divider" /></li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center text-danger"
                          href="#"
                        >
                          <span class="me-auto">Delete</span>
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
                              class="feather feather-trash-2"
                            >
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path
                                d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                              ></path>
                              <line x1="10" y1="11" x2="10" y2="17"></line>
                              <line x1="14" y1="11" x2="14" y2="17"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Dropdown -->
              </div>
            </li>

            <!-- Item -->
            <li class="list-group-item">
              <div class="row align-items-center gx-5">
                <!-- Icons-->
                <div class="col-auto">
                  <div class="avatar-group">
                    <a href="#" class="avatar avatar-sm">
                      <img
                        class="avatar-img"
                        src="assets/img/avatars/2.jpg"
                        alt="#"
                      />
                    </a>

                    <a href="#" class="avatar avatar-sm">
                      <span class="avatar-text bg-success">
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
                    </a>
                  </div>
                </div>
                <!-- Icons-->

                <!-- Text -->
                <div class="col overflow-hidden">
                  <h5 class="text-truncate">
                    <a href="#">E5419783-047D-4B4C-B30E-F24DD8247731.JPG</a>
                  </h5>
                  <ul class="list-inline m-0">
                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">100 KB</small>
                    </li>

                    <li class="list-inline-item">
                      <small class="text-uppercase text-muted">jpg</small>
                    </li>
                  </ul>
                </div>
                <!-- Text -->

                <!-- Dropdown -->
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
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Download
                          <div class="icon ms-auto">
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
                              class="feather feather-download"
                            >
                              <path
                                d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"
                              ></path>
                              <polyline points="7 10 12 15 17 10"></polyline>
                              <line x1="12" y1="15" x2="12" y2="3"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center"
                          href="#"
                        >
                          Share
                          <div class="icon ms-auto">
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
                              class="feather feather-share-2"
                            >
                              <circle cx="18" cy="5" r="3"></circle>
                              <circle cx="6" cy="12" r="3"></circle>
                              <circle cx="18" cy="19" r="3"></circle>
                              <line
                                x1="8.59"
                                y1="13.51"
                                x2="15.42"
                                y2="17.49"
                              ></line>
                              <line
                                x1="15.41"
                                y1="6.51"
                                x2="8.59"
                                y2="10.49"
                              ></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                      <li><hr class="dropdown-divider" /></li>
                      <li>
                        <a
                          class="dropdown-item d-flex align-items-center text-danger"
                          href="#"
                        >
                          <span class="me-auto">Delete</span>
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
                              class="feather feather-trash-2"
                            >
                              <polyline points="3 6 5 6 21 6"></polyline>
                              <path
                                d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"
                              ></path>
                              <line x1="10" y1="11" x2="10" y2="17"></line>
                              <line x1="14" y1="11" x2="14" y2="17"></line>
                            </svg>
                          </div>
                        </a>
                      </li>
                    </ul>
                  </div>
                </div>
                <!-- Dropdown -->
              </div>
            </li>
          </ul>
        </div>
        <!-- Files -->
      </div>
      <!-- Tabs: Content -->
    </div>
    <!-- Offcanvas Body -->
  </div>
</template>
<script>
import { ref } from "vue";

export default {
  name: "chats_section",
  setup() {
    const messages = ref([
      {
        added: "2024-08-26T10:00:00Z",
        messages: [
          {
            id: 1,
            message: "Good morning!",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: null,
            repliedDetails: null,
          },
          {
            id: 2,
            message: "How was your weekend?",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: null,
            repliedDetails: null,
          },
        ],
        messageType: "in",
      },
      {
        added: "2024-08-26T10:05:00Z",
        messages: [
          {
            id: 3,
            message: "Morning! It was great, thanks!",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 2,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
              message:"it is test"
            },
          },
          {
            id: 4,
            message: "How about yours?",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 2,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
              message:"it is test"
            },
          },
        ],
        messageType: "out",
      },
      {
        added: "2024-08-26T10:10:00Z",
        messages: [
          {
            id: 5,
            message: "Mine was good, too. Relaxing.",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: 4,
            repliedDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
              message:"it is test"
            },
          },
        ],
        messageType: "in",
      },
      {
        added: "2024-08-26T10:15:00Z",
        messages: [
          {
            id: 6,
            message: "Glad to hear that!",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 5,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
          {
            id: 7,
            message: "Do you have any plans for today?",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 5,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
        ],
        messageType: "out",
      },
      {
        added: "2024-08-26T10:20:00Z",
        messages: [
          {
            id: 8,
            message: "Just work and maybe some reading later.",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: 7,
            repliedDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
          },
        ],
        messageType: "in",
      },
      {
        added: "2024-08-26T10:25:00Z",
        messages: [
          {
            id: 9,
            message: "That sounds nice. What are you reading?",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 8,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
        ],
        messageType: "out",
      },
      {
        added: "2024-08-26T10:30:00Z",
        messages: [
          {
            id: 10,
            message: "I'm reading a new mystery novel.",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: 9,
            repliedDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
          },
          {
            id: 11,
            message: "It's really good so far.",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: 9,
            repliedDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
          },
        ],
        messageType: "in",
      },
      {
        added: "2024-08-26T10:35:00Z",
        messages: [
          {
            id: 12,
            message: "Sounds intriguing! I love a good mystery.",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 11,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
        ],
        messageType: "out",
      },
      {
        added: "2024-08-26T10:40:00Z",
        messages: [
          {
            id: 13,
            message: "Do you read a lot of mysteries?",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: 12,
            repliedDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
          },
        ],
        messageType: "in",
      },
      {
        added: "2024-08-26T10:45:00Z",
        messages: [
          {
            id: 14,
            message: "I do, but I also enjoy thrillers and fantasy.",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 13,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
          {
            id: 15,
            message: "How about you?",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 13,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
        ],
        messageType: "out",
      },
      {
        added: "2024-08-26T10:50:00Z",
        messages: [
          {
            id: 16,
            message: "I like mysteries and historical fiction.",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: 15,
            repliedDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
          },
        ],
        messageType: "in",
      },
      {
        added: "2024-08-27T10:55:00Z",
        messages: [
          {
            id: 17,
            message: "Historical fiction is fascinating!",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 16,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
        ],
        messageType: "out",
      },
      {
        added: "2024-08-27T11:00:00Z",
        messages: [
          {
            id: 18,
            message: "Do you have a favorite book?",
            userDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
            repliedTo: 17,
            repliedDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
          },
        ],
        messageType: "in",
      },
      {
        added: "2024-08-28T11:05:00Z",
        messages: [
          {
            id: 19,
            message: "I love 'Pride and Prejudice'! You?",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 18,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
          {
            id: 20,
            message: "It's a classic.",
            userDetails: {
              userId: 102,
              userName: "Jane Smith",
              image: "jane_smith_image.jpg",
            },
            repliedTo: 18,
            repliedDetails: {
              userId: 101,
              userName: "John Doe",
              image: "john_doe_image.jpg",
            },
          },
        ],
        messageType: "out",
      },
    ]);
    const images = ref([
  {
    id: 1,
    image: 'https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0'
  },
  {
    id: 2,
    image: 'https://images.unsplash.com/photo-1506748686215-84aa4a99a6d4'
  },
  {
    id: 3,
    image: 'https://images.unsplash.com/photo-1506748686216-3f32e275fc2b'
  },
  {
    id: 4,
    image: 'https://images.unsplash.com/photo-1506748686217-d3fc1b2e7e5a'
  },
  {
    id: 5,
    image: 'https://images.unsplash.com/photo-1506748686218-58f664f5309d'
  },
  {
    id: 6,
    image: 'https://images.unsplash.com/photo-1506748686219-ccf9a8ed354b'
  },
  {
    id: 7,
    image: 'https://images.unsplash.com/photo-1506748686220-ccf9a8ed354c'
  },
  {
    id: 8,
    image: 'https://images.unsplash.com/photo-1506748686221-58f664f5309e'
  },
  {
    id: 9,
    image: 'https://images.unsplash.com/photo-1506748686222-ccf9a8ed354d'
  },
  {
    id: 10,
    image: 'https://images.unsplash.com/photo-1506748686223-58f664f5309f'
  },
  {
    id: 11,
    image: 'https://images.unsplash.com/photo-1506748686224-ccf9a8ed354e'
  },
  {
    id: 12,
    image: 'https://images.unsplash.com/photo-1506748686225-58f664f530a0'
  },
  {
    id: 13,
    image: 'https://images.unsplash.com/photo-1506748686226-ccf9a8ed354f'
  },
  {
    id: 14,
    image: 'https://images.unsplash.com/photo-1506748686227-58f664f530a1'
  },
  {
    id: 15,
    image: 'https://images.unsplash.com/photo-1506748686228-ccf9a8ed3550'
  }
]);

    const getTime=(time)=>{
      const date = new Date(time);
      const hours = date.getHours() > 12? date.getHours() - 12 : date.getHours();
      const meridiem = date.getHours() >12 ?'PM':'AM';
      const newTime = hours+':'+date.getMinutes()+' '+meridiem;
      return newTime;
    }
    const getDate = (time)=>{

      const months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
];

      const date = new Date(time);
      return months[date.getMonth()]+' '+date.getDate()+', '+date.getFullYear();

    }
    const dividerCheck = (time, index) => {
    if (index + 1 >= messages.value.length) {
        return false; // Return false if index + 1 is out of bounds
    }
    
    const date = new Date(time);
    const checkMsg = messages[index + 1].value;
    const checkDate = new Date(checkMsg.added);

    // Compare year, month, and date
    return (
        date.getFullYear() === checkDate.getFullYear() &&
        date.getMonth() === checkDate.getMonth() &&
        date.getDate() === checkDate.getDate()
    );
};
    return { messages, getTime,getDate,dividerCheck,images };
  },
};
</script>
<style scoped>
.chat-form {
  width: 100%;
}
textarea {
  width: 100%;
  border: none;
  background: transparent;
  resize: none;
}
textarea:focus {
  border: none;
}
.input-group-text {
  border: none;
}
.avatar{
  width:50px;
  height:50px;
  border-radius:50%;
  
}
.avatar.avatar-responsive{
  width:30px;
  height:30px;
  border-radius:50%;
  
}
.avatar.avatar-responsive .avatar-img{
  width:30px;
  height:30px;
  border-radius: 50%;  
  object-fit:cover;
}
.avatar .avatar-img{
  width:50px;
  height:50px;
  border-radius:50%;
  object-fit:cover;

}
.avatar.avatar-xl{
  width:80px;
  height:80px;
  border-radius:50%;
  
}
.avatar.avatar-xl .avatar-img{
  width:80px;
  height:80px;
  border-radius: 50%;  
  object-fit:cover;
}
</style>