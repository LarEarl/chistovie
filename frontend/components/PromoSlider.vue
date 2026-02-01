<template>
  <section v-if="items.length" class="w-full bg-gray-100 relative overflow-hidden">
    
    <div class="slider-layout relative z-10">
      <!-- Левая стрелка -->
      <div class="swiper-button-prev"></div>

      <!-- Слайдер -->
      <div class="swiper" ref="slider">
        <div class="swiper-wrapper">
          <div 
            v-for="item in items"
            :key="item.id"
            class="swiper-slide"
          >
            <div class="relative w-full h-[400px] sm:h-[500px] md:h-[600px] lg:h-[700px]">
              <img
                :src="item.image"
                :alt="item.title"
                class="w-full h-full object-cover opacity-60"
              />

              <!-- Градиентный оверлей -->
              <div class="absolute inset-0 bg-gradient-to-r from-primary-500/30 via-primary-500/10 to-transparent"></div>

              <!-- Контент -->
              <div class="absolute inset-0 flex items-center">
                <div class="container mx-auto px-6 sm:px-12">
                  <h2 v-if="item.title" class="font-display text-white font-bold text-4xl sm:text-6xl lg:text-7xl mb-6 leading-tight">
                    {{ item.title }}
                  </h2>

                  <a 
                    v-if="item.link"
                    :href="item.link"
                    class="btn-primary-elegant inline-flex items-center gap-3"
                  >
                    <span>Подробнее</span>
                    <svg class="w-5 h-5 transform group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/>
                    </svg>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- пагинация -->
        <div class="swiper-pagination"></div>
      </div>

      <!-- Правая стрелка -->
      <div class="swiper-button-next"></div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import Swiper from 'swiper'
import { Navigation, Pagination, Autoplay } from 'swiper/modules'

import 'swiper/css'
import 'swiper/css/navigation'
import 'swiper/css/pagination'

const props = defineProps({
  items: Array
})

const slider = ref(null)
let swiper = null

const init = () => {
  if (!slider.value) return

  if (swiper) {
    swiper.destroy()
    swiper = null
  }

  swiper = new Swiper(slider.value, {
    modules: [Navigation, Pagination, Autoplay],
    slidesPerView: 1,
    loop: props.items.length > 1,
    autoplay: props.items.length > 1 ? { delay: 4000 } : false,

    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev'
    },

    pagination: {
      el: '.swiper-pagination',
      clickable: true
    }
  })
}

onMounted(init)
watch(() => props.items, init, { deep: true })
onUnmounted(() => swiper?.destroy())
</script>

<style scoped>
.slider-layout {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1.5rem;
  padding: 2rem 1rem;
  max-width: 1920px;
  margin: 0 auto;
}

.swiper {
  width: 85%;
  max-width: 1400px;
  height: auto;
  position: relative;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.5);
}

.swiper-slide {
  overflow: hidden;
}

.swiper-slide img {
  transition: transform 0.8s cubic-bezier(0.4, 0, 0.2, 1);
}

.swiper-slide:hover img {
  transform: scale(1.08);
}

.swiper-button-prev,
.swiper-button-next {
  position: static;
  color: white;
  background: linear-gradient(135deg, rgba(217, 70, 239, 0.8), rgba(249, 115, 22, 0.8));
  padding: 0;
  border-radius: 50%;
  width: 56px;
  height: 56px;
  min-width: 56px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  border: 2px solid rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(12px);
  box-shadow: 0 8px 24px rgba(217, 70, 239, 0.4);
  margin: 0;
  flex-shrink: 0;
}

.swiper-button-prev:hover,
.swiper-button-next:hover {
  background: linear-gradient(135deg, rgba(217, 70, 239, 1), rgba(249, 115, 22, 1));
  border-color: white;
  box-shadow: 0 12px 32px rgba(217, 70, 239, 0.7);
  transform: scale(1.15);
}

.swiper-button-prev.swiper-button-disabled,
.swiper-button-next.swiper-button-disabled {
  opacity: 0.3;
  cursor: not-allowed;
}

.swiper-button-prev::after,
.swiper-button-next::after {
  font-size: 24px;
  font-weight: bold;
}

:deep(.swiper-pagination) {
  bottom: 24px;
  display: flex;
  justify-content: center;
  gap: 10px;
}

:deep(.swiper-pagination-bullet) {
  width: 12px;
  height: 12px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  cursor: pointer;
  transition: all 0.3s ease;
  border: 2px solid rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(4px);
}

:deep(.swiper-pagination-bullet-active) {
  background: linear-gradient(135deg, #d946ef, #f97316);
  width: 32px;
  border-radius: 6px;
  box-shadow: 0 4px 16px rgba(217, 70, 239, 0.6);
}

.btn-primary-elegant {
  @apply px-8 py-4 font-semibold text-base;
  background: linear-gradient(135deg, #d946ef, #c026d3, #f97316);
  color: white;
  border-radius: 12px;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 24px rgba(217, 70, 239, 0.4);
  position: relative;
  overflow: hidden;
}

.btn-primary-elegant::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, #f97316, #ea580c, #d946ef);
  opacity: 0;
  transition: opacity 0.4s ease;
}

.btn-primary-elegant:hover::before {
  opacity: 1;
}

.btn-primary-elegant:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 32px rgba(217, 70, 239, 0.6);
}

.btn-primary-elegant span,
.btn-primary-elegant svg {
  position: relative;
  z-index: 1;
}

.btn-primary-elegant:active {
  transform: translateY(-2px);
}

/* анимация при появлении текста */
h2 {
  animation: slideInFromLeft 1s cubic-bezier(0.4, 0, 0.2, 1) 0.2s both;
}

.btn-primary-elegant {
  animation: slideInFromLeft 1s cubic-bezier(0.4, 0, 0.2, 1) 0.5s both;
}

@keyframes slideInFromLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

/* Gradient overlay улучшение */
.absolute {
  animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Адаптив для мобильных */
@media (max-width: 768px) {
  .slider-layout {
    gap: 0.75rem;
    padding: 1rem 0.5rem;
  }

  .swiper {
    width: 80%;
  }

  .swiper-button-prev,
  .swiper-button-next {
    width: 44px;
    height: 44px;
    min-width: 44px;
  }

  .swiper-button-prev::after,
  .swiper-button-next::after {
    font-size: 20px;
  }
}

@media (max-width: 480px) {
  .swiper {
    width: 75%;
  }

  .swiper-button-prev,
  .swiper-button-next {
    width: 40px;
    height: 40px;
    min-width: 40px;
  }
}
</style>
