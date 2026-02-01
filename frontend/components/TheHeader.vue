<template>
  <header class="bg-primary-500 backdrop-blur-md border-b border-white/20 sticky top-0 z-50 shadow-2xl">
    <div class="container mx-auto px-4">
      <div class="flex items-center justify-between h-20">
        <!-- Logo -->
        <NuxtLink to="/" class="flex items-center space-x-3 group">
          <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center transform group-hover:scale-110 group-hover:rotate-6 transition-all duration-300 shadow-lg shadow-white/30">
            <span class="text-white text-2xl font-bold font-display">Ч</span>
          </div>
          <span class="text-2xl font-bold font-display text-white group-hover:text-white/90 transition-all">
            Чистовье
          </span>
        </NuxtLink>

        <!-- Desktop Navigation -->
        <nav class="hidden md:flex items-center space-x-8">
          <NuxtLink 
            to="/" 
            class="nav-link"
            active-class="text-primary-400"
          >
            Главная
          </NuxtLink>
          <NuxtLink 
            to="/about" 
            class="nav-link"
            active-class="text-primary-400"
          >
            О нас
          </NuxtLink>
        </nav>

        <!-- Mobile Menu Button -->
        <button 
          @click="toggleMenu" 
          class="md:hidden p-2 rounded-lg hover:bg-white/10 transition-colors text-white"
          aria-label="Меню"
        >
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path 
              v-if="!menuOpen" 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M4 6h16M4 12h16M4 18h16"
            />
            <path 
              v-else 
              stroke-linecap="round" 
              stroke-linejoin="round" 
              stroke-width="2" 
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </div>

      <!-- Mobile Menu -->
      <Transition name="slide-fade">
        <nav v-if="menuOpen" class="md:hidden py-4 border-t border-white/10">
          <NuxtLink 
            to="/" 
            class="block py-3 px-4 hover:bg-white/5 rounded-lg transition-colors text-gray-200"
            @click="toggleMenu"
          >
            Главная
          </NuxtLink>
          <NuxtLink 
            to="/about" 
            class="block py-3 px-4 hover:bg-white/5 rounded-lg transition-colors text-gray-200"
            @click="toggleMenu"
          >
            О нас
          </NuxtLink>
        </nav>
      </Transition>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue'

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}
</script>

<style scoped>
.nav-link {
  @apply text-white font-medium hover:text-white/80 transition-all duration-300 relative;
  font-size: 1.05rem;
  letter-spacing: 0.5px;
}

.nav-link::after {
  content: '';
  @apply absolute -bottom-1 left-0 w-0 h-0.5 bg-white transition-all duration-300;
}

.nav-link:hover::after,
.nav-link.router-link-active::after {
  @apply w-full;
}

.slide-fade-enter-active {
  transition: all 0.3s ease-out;
}

.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(1, 0.5, 0.8, 1);
}

.slide-fade-enter-from,
.slide-fade-leave-to {
  transform: translateY(-10px);
  opacity: 0;
}
</style>
