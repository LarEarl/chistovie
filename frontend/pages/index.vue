<template>
  <div class="min-h-screen">
    <!-- Hero Carousel -->
    <PromoSlider v-if="banners.length > 0" :items="banners" />

    <!-- New Products -->
    <ProductCarousel 
      v-if="newProducts.length > 0"
      title="Новинки"
      :products="newProducts"
    />

    <!-- Sale Products -->
    <ProductCarousel 
      v-if="saleProducts.length > 0"
      title="Акции"
      :products="saleProducts"
    />

    <!-- All Products -->
    <section class="py-16 bg-white">
      <div class="container mx-auto px-4">
        <h2 class="text-4xl font-bold font-display mb-10 text-gray-800">
          Каталог товаров
        </h2>

        <!-- Category Filter -->
        <div class="flex flex-wrap gap-3 mb-10">
          <button
            @click="selectedCategory = null"
            :class="[
              'px-6 py-3 rounded-full font-medium transition-all duration-300',
              selectedCategory === null
                ? 'bg-primary-500 text-white shadow-lg shadow-primary-500/30 scale-105'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-300'
            ]"
          >
            Все
          </button>
          <button
            v-for="category in categories"
            :key="category.id"
            @click="selectedCategory = category.id"
            :class="[
              'px-6 py-3 rounded-full font-medium transition-all duration-300',
              selectedCategory === category.id
                ? 'bg-primary-500 text-white shadow-lg shadow-primary-500/30 scale-105'
                : 'bg-gray-100 text-gray-700 hover:bg-gray-200 border border-gray-300'
            ]"
          >
            {{ category.name }}
          </button>
        </div>

        <!-- Products Grid -->
        <div v-if="loading" class="text-center py-12">
          <div class="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500"></div>
          <p class="mt-4 text-gray-600">Загрузка...</p>
        </div>

        <div v-else-if="filteredProducts.length > 0" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <ProductCard 
            v-for="product in filteredProducts" 
            :key="product.id"
            :product="product"
          />
        </div>

        <div v-else class="text-center py-12">
          <p class="text-gray-600 text-lg">Товары не найдены</p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useProductStore } from '~/stores/products'
import { useApi } from '~/composables/useApi'

const api = useApi()
const productStore = useProductStore()

const loading = ref(true)
const banners = ref([])
const newProducts = ref([])
const saleProducts = ref([])
const allProducts = ref([])
const categories = ref([])
const selectedCategory = ref(null)

const filteredProducts = computed(() => {
  if (selectedCategory.value === null) {
    return allProducts.value
  }
  return allProducts.value.filter(p => p.category === selectedCategory.value)
})

onMounted(async () => {
  try {
    // Fetch all data in parallel
    const [bannersData, newProdsData, saleProdsData, categoriesData, allProdsData] = await Promise.all([
      api.getBanners().catch(() => ({ results: [] })),
      api.getNewProducts().catch(() => []),
      api.getSaleProducts().catch(() => []),
      api.getCategories().catch(() => []),
      api.getProducts().catch(() => ({ results: [] }))
    ])

    // Handle paginated responses - banners come as paginated
    const bannersList = bannersData?.results || bannersData || []
    banners.value = Array.isArray(bannersList) 
      ? bannersList.filter(b => b.is_active)
      : []
    
    newProducts.value = Array.isArray(newProdsData) ? newProdsData : []
    saleProducts.value = Array.isArray(saleProdsData) ? saleProdsData : []
    categories.value = Array.isArray(categoriesData) ? categoriesData : []
    
    // Handle paginated response for products
    if (allProdsData && allProdsData.results) {
      allProducts.value = Array.isArray(allProdsData.results) ? allProdsData.results : []
    } else if (Array.isArray(allProdsData)) {
      allProducts.value = allProdsData
    } else {
      allProducts.value = []
    }

    console.log('✓ Loaded banners:', banners.value.length, banners.value)
    console.log('✓ Loaded products:', allProducts.value.length)
    console.log('✓ API Banners response:', bannersData)
  } catch (error) {
    console.error('✗ Error loading data:', error)
  } finally {
    loading.value = false
  }
})

useHead({
  title: 'Главная - Chistovye',
  meta: [
    { name: 'description', content: 'Каталог качественных товаров для вашего дома' }
  ]
})
</script>
