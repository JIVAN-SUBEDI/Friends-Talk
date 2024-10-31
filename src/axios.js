// Axios instance
import axios from 'axios';
import store from './store';  // Assuming you have Vuex or other store
axios.defaults.baseURL ='http://localhost:8000/api/';
const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/',
});

// Add a request interceptor
axiosInstance.interceptors.request.use(
  async (config) => {
    const accessToken = store.state.access_token; // Get access token from Vuex
    if (accessToken) {
      config.headers['Authorization'] = `Bearer ${accessToken}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Add a response interceptor to handle 401 errors (access token expired)
axiosInstance.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    
    // If the error is a 401 (token expired) and the request has not been retried yet
    console.log(error)
    if (error.response.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      const refreshToken = store.state.refresh_token; // Get refresh token
      try{

        // Call the refresh token endpoint
        const response = await axios.post('token/refresh/', { refresh: refreshToken });
        store.commit('refreshToken', response.data.access);
        originalRequest.headers['Authorization'] = `Bearer ${response.data.access}`;
      }catch{
        store.dispatch('logout')
      }
      
      
      // Retry the original request with the new token
      return axiosInstance(originalRequest);
    }
    
    return Promise.reject(error);
  }
);

export default axiosInstance;

