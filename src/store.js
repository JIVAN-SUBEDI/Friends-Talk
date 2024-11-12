// store/index.js
import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import axios from 'axios';
import axiosInstance from './axios';
import router from './route';


export default createStore({
  state: {
    access_token: null,
    refresh_token: null,
    isAuth: false,
    isUserLoaded: false,
    user: {
      first_name: "",
      last_name: "",
      email: "",
      gender: "",
      bio: "",
      profile_image: "",
      cover_image: "",
      phone_number: "",
      dob: "",
    },
    workplaces: [],
    colleges: [],
    places:[],
    profile:[],
    friends:[],
    search:{ 
      results: [],
      next: null,
  },
    userProfile:[],
    feeling:[],
    activity:[],
    posts: {
      results: [],
      next: null,
    },
    loading: false,
    images:[],
    imageIndex:0,
    post:[],
    share:null
  },
  mutations: {
    setTokens(state, { access_token, refresh_token }) {
      state.access_token = access_token;
      state.refresh_token = refresh_token;
      state.isAuth = true;
    },

    logout(state) {
      state.access_token = null;
      state.refresh_token = null;
      state.isAuth = false;
      state.user = "";
      state.isUserLoaded = false;
      axios.defaults.headers.common['Authorization'] = ''
    },
    refreshToken(state, newToken) {
      state.access_token = newToken;
    },
    setProfile(state, { user }) {
      state.user = user
      state.isUserLoaded = true;
    },
    SET_WORKPLACES(state, workplaces) {
      state.workplaces = workplaces;
    },
    ADD_WORKPLACE(state, workplace) {
      state.workplaces.push(workplace);
    },
    REMOVE_WORKPLACE(state, id) {
      state.workplaces = state.workplaces.filter(item => item.id !== id);
    },
    UPDATE_WORKPLACE(state, updatedWorkplace) {
      const index = state.workplaces.findIndex(item => item.id === updatedWorkplace.id);
      if (index !== -1) {
        state.workplaces[index] = updatedWorkplace;
      }
    },
    SET_COLLEGES(state, colleges) {
      state.colleges = colleges;
    },
    ADD_COLLEGE(state, college) {
      state.colleges.push(college);
    },
    REMOVE_COLLEGE(state, id) {
      state.colleges = state.colleges.filter(item => item.id !== id);
    },
    UPDATE_COLLEGE(state, updatedCollege) {
      const index = state.colleges.findIndex(item => item.id === updatedCollege.id);
      if (index !== -1) {
        state.colleges[index] = updatedCollege;
      }
    },
    SET_PLACES(state, places) {
      state.places = places;
    },
    ADD_PLACE(state, place) {
      state.places.push(place);
    },
    UPDATE_PLACE(state, updatedPlace) {
      const index = state.places.findIndex(place => place.id === updatedPlace.id);
      if (index !== -1) {
        state.places.splice(index, 1, updatedPlace);
      }
    },
    DELETE_PLACE(state, placeId) {
      state.places = state.places.filter(place => place.id !== placeId);
    },
    SET_PROFILE(state,profile){
      state.profile = profile
    },
    UPDATE_GENDER(state,gender){
      state.profile.gender = gender.gender
      state.profile.gender_audience = gender.gender_audience
    },
    UPDATE_DOB(state,dob){
      state.profile.date_of_birth = dob.date_of_birth
      state.profile.date_of_birth_audience = dob.date_of_birth_audience
    },
    UPDATE_RELATIONSHIP(state,relationship){
      state.profile.relationship = relationship.relationship
      state.profile.relationship_audience = relationship.relationship_audience
    },
    UPDATE_PRIMARY(state,primary_phone_number){
      state.profile.primary_phone_number = primary_phone_number.primary_phone_number
      state.profile.primary_phone_number_audience = primary_phone_number.primary_phone_number_audience
    },
    UPDATE_SECONDARY(state,secondary_phone_number){
      state.profile.secondary_phone_number = secondary_phone_number.secondary_phone_number
      state.profile.secondary_phone_number_audience = secondary_phone_number.secondary_phone_number_audience
    },
    UPDATE_BIO(state,bio){
      state.profile.bio = bio
    },
  
    SET_SEARCH_RESULTS(state, results) {
      state.search = results;
    },
    UPDATE_FRIEND_STATUS(state,{id,status}){
      const user = state.search.results.find(user=>user.id == id)
      if(user){
        user.status = status;
      }
    },
    UPDATE_FRIEND_USER_STATUS(state,{id,status}){
      const user = state.userProfile.friends.find(user=>user.details.id == id)
  
      if(user){
        user.status = status;
   
      }
    },
    UPDATE_USER_PROFILE_STATUS(state,status){
      state.userProfile.status = status
    },
    SET_USER_PROFILE(state,details){
    state.userProfile = details;
    },
    SET_FRIENDS(state,data){
      state.friends = data
    },
    REMOVE_FRIENDS(state,id){
      state.friends = state.friends.filter(item => item.id !== id);
    },
    SET_FEELING(state,data){
      state.feeling = data
    },
    SET_ACTIVITY(state,data){
      state.activity = data
    },
    SET_POSTS(state, posts) {
      state.posts = posts;
    },
    ADD_POST_SELF(state,post){
      
      state.posts.results.unshift(post);
    },
    ADD_POSTS(state, morePosts) {
      state.posts.results.push(...morePosts.results);
      state.posts.next = morePosts.next;
    },
    SET_LOADING(state, isLoading) {
      state.loading = isLoading;
    },
    RESET_POSTS(state) {
      state.posts = { results: [], next: null };
    },
    UPDATE_LIKE(state,{id,status}){
      const post = state.posts.results.find(post=>post.id === id);
      if(post){
        post.liked = status;
        if(status){
          
          post.likes_count+=1;
        }else{
          post.likes_count-=1;
          
        }
        
      }
    },
    UPDATE_COMMENTS(state, { id, data }) {
 
      const post = state.posts.results.find(post => post.id === id);

      // Check if the post exists
      if (post) {
        // Ensure the post has a comments array
        if (!post.comments) {
          post.comments = [];
        }
        
        // Add the new comment to the beginning of the comments array
        post.comments.unshift(data);
      } else {
        console.error(`Post with id ${id} not found.`);
      }
    },
    DELETE_COMMENT(state, { id, cmtId }) {
      const post = state.posts.results.find(post => post.id === id);
      if (post) {
        // Filter out the comment by commentId
        post.comments = post.comments.filter(comment => comment.id !== cmtId);
      }
    },
    SET_IMAGES(state,{images,index}){
      state.images = images
      state.imageIndex = index
    },
    SET_POST(state,post){
      state.post =post;
      
    },
    SET_SHARE(state,post){
      state.share = post;
      
    }
  },
  actions: {
    login({ commit }, { access_token, refresh_token }) {
      commit('setTokens', { access_token, refresh_token });
    },
    logout({ commit }) {
      commit('logout');
      router.push('/login')
    },
    async loadProfile({ commit, state, dispatch }) {
      if (!state.isUserLoaded) {
        await axiosInstance.get('profile/').then(resp => {
          const user = resp.data
          commit('setProfile', { user });
        }).catch(() => {
          dispatch('logout')
        })
      }
    },
    async loadProfileforce({ commit, dispatch }) {

      await axiosInstance.get('profile/').then(resp => {
        const user = resp.data
        commit('setProfile', { user });
      }).catch(() => {
        dispatch('logout')
      })

    },
    async performSearch({ commit }, query) {
      await axiosInstance.get(`search/${query}/`).then(resp=>{
        commit('SET_SEARCH_RESULTS', resp.data);

      });
    },
    async fetchUser({commit},id){
      await axiosInstance.get(`profile/view/${id}`).then(resp=>{
        commit('SET_USER_PROFILE',resp.data)
      }).catch(()=>{
        router.push('/');
      })
    },
    async fetchActiviyFeeling({commit,state}){
      if(state.feeling == '' ){
        
        await axiosInstance.get('feeling/').then(resp=>{
          commit('SET_FEELING',resp.data)
        });
      }
      if(state.activity == '' ){
      await axiosInstance.get('activity/').then(resp=>{
        commit('SET_ACTIVITY',resp.data)
      });
    }
    },
    async fetchPosts({ commit }) {
      commit('SET_LOADING', true);
      try {
        const response = await axiosInstance.get('/posts'); // Replace with your API endpoint
        commit('SET_POSTS', response.data);
      } catch (error) {
        console.error("Error fetching posts:", error);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async fetchMorePosts({ commit }, nextUrl) {
      if (!nextUrl) return;
      
      commit('SET_LOADING', true);
      try {
        const response = await axiosInstance.get(nextUrl);
        commit('ADD_POSTS', response.data);
      } catch (error) {
        console.error("Error fetching more posts:", error);
      } finally {
        commit('SET_LOADING', false);
      }
    },
    resetPosts({ commit }) {
      commit('RESET_POSTS');
    },


  },
  getters:{
      getHometown: (state) => {
          const hometownObject = state.places.find(obj => obj.type === 0);

          return hometownObject ? hometownObject : null;
      },
      getCurrentCity: (state) => {
          const currentCityObject = state.places.find(obj => obj.type === 1);

          return currentCityObject ? currentCityObject : null;
      },
      getLatestCollege: (state) => {
        if (state.colleges.length === 0) {
          return { message: null, data: null };  // Return null if there are no colleges
        }
  
        // Find the college where attend_to is "Present"
        const currentCollege = state.colleges.find(college => college.attend_to === "Present");
        
        if (currentCollege) {
          return {
            message: `Went to ${currentCollege.name}`,
            data: currentCollege
          };
        } else {
          // Sort by attend_to (latest first) to get the most recent past college
          const latestPastCollege = [...state.colleges]
            .filter(college => college.attend_to !== "Present")
            .sort((a, b) => new Date(b.attend_to) - new Date(a.attend_to))[0];
          
          return latestPastCollege
            ? { message: `Studied at ${latestPastCollege.name}`, data: latestPastCollege }
            : { message: null, data: null };
        }
      },
      getCurrentOrLatestWorkplace: (state) => {
        if (state.workplaces.length === 0) {
          return null;  // Return null if there are no workplaces
        }
  
        // Find the workplace where current is true or works_to is null
        const currentWorkplace = state.workplaces.find(workplace => workplace.current === true || workplace.works_to === null);
        
        if (currentWorkplace) {
          return currentWorkplace; // Return the current workplace data
        } else {
          // Sort by works_from (latest first) to get the most recent past workplace
          const latestPastWorkplace = [...state.workplaces]
            .filter(workplace => workplace.works_to !== null) // Only past jobs (works_to not null)
            .sort((a, b) => new Date(b.works_from) - new Date(a.works_from))[0];
          
          return latestPastWorkplace || null; // Return the latest past workplace data or null
        }
      }
    
      
  
  },
  plugins: [createPersistedState({
    paths: ['access_token', 'refresh_token', 'isAuth']
  })],
});
