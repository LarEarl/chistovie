<template>
  <div 
    class="card group cursor-pointer product-card bg-white border border-gray-200 hover:border-primary-500 transition-all duration-500"
    @click="navigateToProduct"
  >
    <!-- Image Container -->
    <div class="relative overflow-hidden aspect-square bg-gray-100">
      <img 
        v-if="product.images && product.images.length > 0"
        :src="product.images[0]" 
        :alt="product.title"
        class="w-full h-full object-cover transform group-hover:scale-110 transition-transform duration-700 opacity-90 group-hover:opacity-100"
        loading="lazy"
      />
      <div v-else class="w-full h-full flex items-center justify-center text-gray-600">
        <svg class="w-16 h-16" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" />
        </svg>
      </div>

      <!-- Badges -->
      <div class="absolute top-3 right-3 flex flex-col gap-2">
        <span v-if="product.promo === 'new'" class="badge badge-new">
          Новинка
        </span>
        <span v-if="product.promo === 'sale'" class="badge badge-sale">
          Акция
        </span>
      </div>
    </div>

    <!-- Content -->
    <div class="p-5">
      <h3 class="text-lg font-semibold text-gray-800 mb-2 line-clamp-2 group-hover:text-primary-500 transition-colors duration-300">
        {{ product.title }}
      </h3>

      <p v-if="product.category_name" class="text-sm text-gray-600 mb-3">
        {{ product.category_name }}
      </p>

      <div class="flex items-end justify-between">
        <div>
          <p class="text-2xl font-bold text-primary-500">
            {{ formatPrice(product.price) }} ₸
          </p>
          <p v-if="product.old_price" class="text-sm text-gray-400 line-through">
            {{ formatPrice(product.old_price) }} ₸
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({
  product: {
    type: Object,
    required: true,
    validator: (value) => {
      return value && value.id && value.slug
    }
  }
})

const router = useRouter()

const formatPrice = (price) => {
  if (!price) return '0'
  return new Intl.NumberFormat('ru-RU').format(price)
}

const navigateToProduct = () => {
  if (props.product && props.product.slug) {
    router.push(`/products/${props.product.slug}`)
  }
}
</script>

<style scoped>
.product-card {
  animation: fadeInUp 0.6s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.product-card:hover {
  box-shadow: 0 12px 40px rgba(217, 70, 239, 0.3);
  transform: translateY(-4px);
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.badge {
  @apply px-3 py-1.5 rounded-full text-xs font-bold uppercase tracking-wide backdrop-blur-md;
}

.badge-new {
  background: linear-gradient(135deg, rgba(34, 197, 94, 0.9), rgba(22, 163, 74, 0.9));
  color: white;
  box-shadow: 0 4px 12px rgba(34, 197, 94, 0.4);
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

.badge-sale {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.9), rgba(220, 38, 38, 0.9));
  color: white;
  box-shadow: 0 4px 12px rgba(239, 68, 68, 0.4);
  animation: bounce 2s infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.8;
  }
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-4px);
  }
}
</style>
