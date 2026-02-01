<template>
  <section class="py-16 bg-gray-50">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between mb-10">
        <h2 class="text-4xl font-bold font-display text-gray-800">
          {{ title }}
        </h2>
        <NuxtLink 
          v-if="viewAllLink"
          :to="viewAllLink"
          class="text-primary-400 hover:text-primary-500 font-medium flex items-center gap-2 group transition-all duration-300"
        >
          <span class="text-lg">Смотреть все</span>
          <svg class="w-6 h-6 transform group-hover:translate-x-2 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" />
          </svg>
        </NuxtLink>
      </div>

      <div class="swiper-container" ref="swiperContainer">
        <div class="swiper-wrapper">
          <div 
            v-for="product in products" 
            :key="product.id"
            class="swiper-slide"
          >
            <ProductCard :product="product" />
          </div>
        </div>

        <!-- Navigation -->
        <div class="swiper-button-prev-custom"></div>
        <div class="swiper-button-next-custom"></div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import Swiper from 'swiper'
import { Navigation } from 'swiper/modules'
import 'swiper/css'
import 'swiper/css/navigation'

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  products: {
    type: Array,
    default: () => []
  },
  viewAllLink: {
    type: String,
    default: null
  }
})

const swiperContainer = ref(null)
let swiper = null

onMounted(() => {
  if (swiperContainer.value && props.products.length > 0) {
    swiper = new Swiper(swiperContainer.value, {
      modules: [Navigation],
      slidesPerView: 1,
      spaceBetween: 20,
      navigation: {
        nextEl: '.swiper-button-next-custom',
        prevEl: '.swiper-button-prev-custom',
      },
      breakpoints: {
        640: {
          slidesPerView: 2,
          spaceBetween: 20,
        },
        768: {
          slidesPerView: 3,
          spaceBetween: 24,
        },
        1024: {
          slidesPerView: 4,
          spaceBetween: 24,
        },
      },
    })
  }
})

onUnmounted(() => {
  if (swiper) {
    swiper.destroy()
  }
})
</script>

<style scoped>
.swiper-container {
  position: relative;
  padding: 0 60px;
}

.swiper-button-prev-custom,
.swiper-button-next-custom {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, rgba(217, 70, 239, 0.9), rgba(249, 115, 22, 0.9));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  border: 2px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 24px rgba(217, 70, 239, 0.4);
}

.swiper-button-prev-custom:hover,
.swiper-button-next-custom:hover {
  background: linear-gradient(135deg, rgba(217, 70, 239, 1), rgba(249, 115, 22, 1));
  transform: translateY(-50%) scale(1.15);
  box-shadow: 0 12px 32px rgba(217, 70, 239, 0.6);
  border-color: white;
}

.swiper-button-prev-custom {
  left: 0;
}

.swiper-button-next-custom {
  right: 0;
}

.swiper-button-prev-custom::after,
.swiper-button-next-custom::after {
  content: '';
  border: solid white;
  border-width: 0 3px 3px 0;
  display: inline-block;
  padding: 5px;
}

.swiper-button-prev-custom::after {
  transform: rotate(135deg);
}

.swiper-button-next-custom::after {
  transform: rotate(-45deg);
}

@media (max-width: 768px) {
  .swiper-container {
    padding: 0 50px;
  }
  
  .swiper-button-prev-custom,
  .swiper-button-next-custom {
    width: 40px;
    height: 40px;
  }
}
</style>
