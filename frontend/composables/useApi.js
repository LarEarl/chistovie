export const useApi = () => {
  const config = useRuntimeConfig()
  const baseURL = config.public.apiBase

  const fetchAPI = async (endpoint, options = {}) => {
    try {
      const response = await $fetch(`${baseURL}${endpoint}`, {
        ...options,
        headers: {
          ...options.headers,
        }
      })
      return response
    } catch (error) {
      console.error('API Error:', error)
      throw error
    }
  }

  return {
    // Products
    getProducts: (params = {}) => fetchAPI('/products/', { params }),
    getProduct: (slug) => fetchAPI(`/products/${slug}/`),
    getNewProducts: () => fetchAPI('/products/new_products/'),
    getSaleProducts: () => fetchAPI('/products/sale_products/'),
    
    // Categories
    getCategories: () => fetchAPI('/categories/'),
    getCategory: (slug) => fetchAPI(`/categories/${slug}/`),
    
    // Promos
    getBanners: () => fetchAPI('/promos/'),
  }
}
