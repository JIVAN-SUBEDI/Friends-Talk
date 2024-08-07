<template>
  <div class="card mt-3 border-0">
    <div class="card-body">
      <div class="post-header d-flex align-items-center">
        <div class="d-flex align-items-center">
          <img
            src="https://media.gettyimages.com/id/609686580/photo/girl-in-st-petersburg.jpg?s=612x612&w=gi&k=20&c=8qAfrDx1GAn_-o6uDnaCMGt7wmUcJv6LSOvQlH_1-w4="
            alt=""
            class="rounded-circle border me-2"
            width="50px"
            height="50px"
          />
          <div class="d-flex flex-column">
            <span>
              Jasmine James
              <span>&ThickSpace;is celebrating Birthday. </span>
            </span>
            <span class="text-secondary"> 24h ago </span>
          </div>
        </div>
      </div>
      <div class="mt-4">
        <div :class="{ 'text-truncate-after-8': !expanded }" ref="textContainer">

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam, nesciunt provident qui minus aspernatur quibusdam temporibus odit alias quas perspiciatis. Earum soluta veritatis distinctio nisi delectus temporibus similique ducimus molestiae reiciendis iste enim id minima rerum, ea corporis esse cumque qui voluptas ab atque cupiditate voluptate exercitationem neque. Ut optio amet, magnam totam iusto molestias odio velit voluptatibus numquam labore facilis odit, quo laborum quis sequi similique animi quos reiciendis officiis quisquam mollitia, doloribus vitae? Doloribus iure similique, cupiditate tempore repellat dolores id assumenda labore soluta, totam sequi quod quae blanditiis aut dolor. Voluptas beatae sit laudantium, sequi reiciendis amet iusto dicta aspernatur officia architecto quam exercitationem dolor odio impedit esse cumque voluptates nostrum facere ea a consequatur. Optio aspernatur cupiditate iusto architecto illum similique ducimus laudantium dolorum dolorem aliquid minima odio, debitis voluptas fuga nemo totam a labore deleniti ipsum. Maxime accusamus accusantium impedit, consequuntur ipsam alias molestias laboriosam soluta blanditiis repellat tempora at corrupti esse temporibus fuga distinctio porro perspiciatis a mollitia odio perferendis dolorum incidunt itaque! Doloribus, quisquam quae! Velit fuga rerum facere, minima animi, nostrum dolor officia totam laborum maxime explicabo debitis repellat accusamus quos facilis ratione a quo! Voluptas doloremque illum veritatis, molestias tempore et.
        </div>
        <a href="#" @click.prevent="toggleText">
      {{ expanded ? 'See Less' : 'See More' }}
    </a>
      </div>
      <div class="mt-2" :class="{'single-image': post.images.length === 1, 'image-grid': post.images.length > 1}">
    <img v-for="(image, index) in post.images" :key="index" :src="image" :alt="'Image ' + (index + 1)" />
  </div>
    </div>
  </div>
</template>
<script>
import { ref,onMounted } from 'vue';

export default {
  name: "post_card.",
  props:['post'],
  setup(){
    const expanded = ref(false);
    const textContainer = ref(null);
    const isOverflowing = ref(false);

    const checkOverflow = () => {
      const el = textContainer.value;
      const lineHeight = parseFloat(window.getComputedStyle(el).lineHeight);
      const maxHeight = lineHeight * 8;
      isOverflowing.value = el.scrollHeight > maxHeight;
    };

    onMounted(() => {
      checkOverflow();
    });

    const toggleText = () => {
      expanded.value = !expanded.value;
    };

    return {
      expanded,
      textContainer,
      isOverflowing,
      toggleText
    };
  }
};
</script>
<style scoped>
.text-secondary {
  font-size: 0.9rem;
}
.text-truncate-after-8 {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 8;
  overflow: hidden;
}
.single-image {
  display: flex;
  justify-content: center;
  align-items: center;
}

.single-image img {
  max-width: 100%;
  max-height: 100%;
}

.image-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 10px;
}

.image-grid img {
  width: 100%;
  height: auto;
  object-fit: cover;
}
</style>
