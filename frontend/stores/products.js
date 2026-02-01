import { defineStore } from 'pinia'

export const useProductStore = defineStore('products', {
  state: () => ({
    products: [],
    product: null,
    categories: [],
    banners: [],
    loading: false,
    error: null,
  }),

  actions: {
    async fetchProducts(params = {}) {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        this.products = await api.getProducts(params)
      } catch (error) {
        this.error = error
        console.error('Error fetching products:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchProduct(slug) {
      this.loading = true
      this.error = null
      try {
        const api = useApi()
        this.product = await api.getProduct(slug)
      } catch (error) {
        this.error = error
        console.error('Error fetching product:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchCategories() {
      try {
        const api = useApi()
        this.categories = await api.getCategories()
      } catch (error) {
        console.error('Error fetching categories:', error)
      }
    },

    async fetchBanners() {
      try {
        const api = useApi()
        this.banners = await api.getBanners()
      } catch (error) {
        console.error('Error fetching banners:', error)
      }
    },
  },
})
