<template>
  <div class="min-h-screen bg-gray-50 py-12">
    <div class="container mx-auto px-4">
      <!-- Back Button -->
      <button 
        @click="$router.back()"
        class="flex items-center gap-2 text-gray-600 hover:text-primary-500 mb-6 transition-colors"
      >
        <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        Назад
      </button>

      <div v-if="loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
      </div>

      <div v-else-if="product" class="bg-white rounded-2xl shadow-lg overflow-hidden">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 p-8">
          <!-- Images -->
          <div>
            <div class="mb-4 aspect-square bg-gray-100 rounded-xl overflow-hidden">
              <img 
                v-if="currentImage"
                :src="currentImage" 
                :alt="product.title"
                class="w-full h-full object-cover"
              />
              <div v-else class="w-full h-full flex items-center justify-center text-gray-400">
                <svg class="w-24 h-24" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
                </svg>
              </div>
            </div>

            <!-- Thumbnails -->
            <div v-if="productImages.length > 1" class="grid grid-cols-4 gap-2">
              <div 
                v-for="(image, index) in productImages" 
                :key="index"
                @click="currentImageIndex = index"
                :class="[
                  'aspect-square rounded-lg overflow-hidden cursor-pointer border-2 transition-all',
                  currentImageIndex === index ? 'border-primary-500' : 'border-transparent hover:border-gray-300'
                ]"
              >
                <img :src="image" :alt="`${product.title} ${index + 1}`" class="w-full h-full object-cover" />
              </div>
            </div>
          </div>

          <!-- Details -->
          <div>
            <!-- Badges -->
            <div class="flex gap-2 mb-4">
              <span v-if="product.promo === 'new'" class="badge badge-new">
                Новинка
              </span>
              <span v-if="product.promo === 'sale'" class="badge badge-sale">
                Акция
              </span>
            </div>

            <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ product.title }}</h1>

            <p v-if="product.category_name" class="text-gray-600 mb-6">
              Категория: <span class="font-medium">{{ product.category_name }}</span>
            </p>

            <div class="mb-6">
              <div class="flex items-end gap-3">
                <p class="text-4xl font-bold text-primary-500">
                  {{ formatPrice(product.price) }} ₸
                </p>
                <p v-if="product.old_price" class="text-xl text-gray-400 line-through mb-1">
                  {{ formatPrice(product.old_price) }} ₸
                </p>
              </div>
              <p v-if="product.old_price" class="text-green-600 font-medium mt-2">
                Скидка {{ calculateDiscount }}%
              </p>
            </div>

            <div v-if="product.description" class="mb-8">
              <h3 class="text-lg font-semibold mb-2">Описание</h3>
              <p class="text-gray-600 leading-relaxed">{{ product.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-12">
        <p class="text-gray-600 text-lg">Товар не найден</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { useApi } from '~/composables/useApi'

const route = useRoute()
const api = useApi()

const loading = ref(true)
const product = ref(null)
const currentImageIndex = ref(0)

const productImages = computed(() => {
  if (!product.value?.images) return []
  return product.value.images.map(img => typeof img === 'string' ? img : img.image)
})

const currentImage = computed(() => {
  return productImages.value[currentImageIndex.value]
})

const calculateDiscount = computed(() => {
  if (!product.value?.old_price || !product.value?.price) return 0
  const discount = ((product.value.old_price - product.value.price) / product.value.old_price) * 100
  return Math.round(discount)
})

const formatPrice = (price) => {
  return new Intl.NumberFormat('ru-RU').format(price)
}

onMounted(async () => {
  try {
    product.value = await api.getProduct(route.params.slug)
  } catch (error) {
    console.error('Error loading product:', error)
  } finally {
    loading.value = false
  }
})

useHead({
  title: computed(() => product.value ? `${product.value.title} - Chistovye` : 'Товар - Chistovye'),
  meta: computed(() => [
    { name: 'description', content: product.value?.description || 'Описание товара' }
  ])
})
</script>
