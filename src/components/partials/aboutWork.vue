<template>
    <div>
        <!-- workplace section -->
        <h5 class="mb-2">work</h5>
        <a class="text-primary cursor-pointer plus-button mt-3">
          <font-awesome-icon :icon="['fas', 'circle-plus']" /> 
          <span class="ms-2" @click="workplaceAddClick">Add Workplace</span>
        </a>
        <!-- add workplace fields -->
        <div class="form-group" v-if="workplaceAddFieldVisible">
                <input type="text" class="form-control mt-2" placeholder="Company Name" v-model="addWorkplace.name">
                <span class="text-danger">{{ addWorkplaceError.name }}</span>
                <input type="text" class="form-control mt-2" placeholder="Position" v-model="addWorkplace.position">
                <span class="text-danger">{{ addWorkplaceError.position }}</span>
                <input type="text" class="form-control mt-2" placeholder="Address" v-model="addWorkplace.address">
                <span class="text-danger">{{ addWorkplaceError.address }}</span>
                <textarea class="form-control mt-2" cols="30" rows="5" placeholder="Description" v-model="addWorkplace.desc"></textarea>
                <h6 class="mt-3">Time Period</h6>
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" v-model="addWorkplace.current" @change="addWorkplaceCurrent" id="defaultCheck1">
                  <label class="form-check-label" for="defaultCheck1">
                    I currently work here
                  </label>
                </div>
                <div class="mt-2 row">
                  
                  <div class="col-md-6">
                    <label for="">From</label>
                    <input type="date" class="form-control" v-model="addWorkplace.works_from">
                    <span class="text-danger">{{ addWorkplaceError.works_from }}</span>
                  </div>
                  <div class="col-md-6">
                    <label for="">To</label>
                    <input type="date" class="form-control" v-model="addWorkplace.works_to" :disabled="addWorkplace.current">
                    <span class="text-danger">{{ addWorkplaceError.works_to }}</span>
                  </div>
                </div>
               <h6 class="mt-3">Audience</h6>
                <select  class="mt-2 form-control" v-model="addWorkplace.audience">
                    <option value="0">Public</option>
                    <option value="1">Friends</option>
                    <option value="2">Only Me</option>
                </select>
                <div class="d-flex justify-content-end mt-2">
                  <button class="btn btn-secondary" @click="workplaceAddClick">Cancel</button>
                  <button class="btn btn-primary ms-2" @click="workplaceSave">Save</button>
                </div>
        </div>
        <!-- edit workplace fields -->
        <div class="form-group" v-if="workplaceEditFieldVisible">
                <input type="text" class="form-control mt-2" placeholder="Company Name" v-model="editWorkplace.name">
                <span class="text-danger">{{ editWorkplaceError.name }}</span>
                <input type="text" class="form-control mt-2" placeholder="Position" v-model="editWorkplace.position">
                <span class="text-danger">{{ editWorkplaceError.position }}</span>
                <input type="text" class="form-control mt-2" placeholder="Address" v-model="editWorkplace.address">
                <span class="text-danger">{{ editWorkplaceError.address }}</span>
                <textarea class="form-control mt-2" cols="30" rows="5" placeholder="Description" v-model="editWorkplace.desc"></textarea>
                <h6 class="mt-3">Time Period</h6>
                <div class="form-check">
                  <input class="form-check-input" type="checkbox" v-model="editWorkplace.current" @change="editWorkplaceCurrent" id="defaultCheck1">
                  <label class="form-check-label" for="defaultCheck1">
                    I currently work here
                  </label>
                </div>
                <div class="mt-2 row">
                  
                  <div class="col-md-6">
                    <label for="">From</label>
                    <input type="date" class="form-control" v-model="editWorkplace.works_from">
                    <span class="text-danger">{{ editWorkplaceError.works_from }}</span>
                  </div>
                  <div class="col-md-6">
                    <label for="">To</label>
                    <input type="date" class="form-control" v-model="editWorkplace.works_to" :disabled="editWorkplace.current">
                    <span class="text-danger">{{ editWorkplaceError.works_to }}</span>
                  </div>
                </div>
               <h6 class="mt-3">Audience</h6>
                <select  class="mt-2 form-control" v-model="editWorkplace.audience">
                    <option value="0">Public</option>
                    <option value="1">Friends</option>
                    <option value="2">Only Me</option>
                </select>
                <div class="d-flex justify-content-end mt-2">
                  <button class="btn btn-secondary" @click="workplaceEditClick">Cancel</button>
                  <button class="btn btn-primary ms-2" @click="updateWorkplace">Save</button>
                </div>
        </div>
        <ul style="list-style: none">
                <li class=" mt-2" v-for="(workplace,index) in workplaces" :key="workplace.id">
                  <div class="d-flex justify-content-between">
                    <div class="d-flex align-items-center">
                        <div class="d-flex flex-column ">
                            <span>{{ workplace.position }} at {{ workplace.name }}</span>
                            <span class="text-small text-secondary">{{ workplace.works_from }} to <span v-if="workplace.current">Present</span> <span v-else> {{ workplace.works_to }}</span>,<span>{{ workplace.address }}</span> </span>

                        </div>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                      <a class="me-2 text-dark cursor-pointer" @click="loadAudienceWorkplace(workplace.id,index)">

                        <font-awesome-icon v-if="workplace.audience =='0'" :icon="['fas', 'earth-americas']" />
                        <font-awesome-icon v-if="workplace.audience =='1'" :icon="['fas', 'users']" />
                        <font-awesome-icon v-if="workplace.audience =='2'" :icon="['fas', 'lock']" />
                      </a>
                      <div class="dropdown">
                        <a  class="ms-4 text-dark cursor-pointer  rounded-circle bg-light edit-btn" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          <font-awesome-icon :icon="['fas', 'ellipsis']" />
                        </a>
                        <div class="dropdown-menu">
                          <a class="dropdown-item" @click="loadWorkPlace(workplace.id)">Edit Workplace</a>
                          <a class="dropdown-item"  @click="workplaceDelete(workplace.id)">Delete Workplace</a>
               
                        </div>
                      </div>
                     
                    </div>
                  </div>
                  <div class="mt-2 form-group" v-if="workplaceAudience[index] && workplaceAudience[index].isEditing">
                    <h6 class="mt-3">Select Audience</h6>
                <select  class="mt-2 form-control" v-model="editWorkplace.audience">
                    <option value="0">Public</option>
                    <option value="1">Friends</option>
                    <option value="2">Only Me</option>
                </select>
                <div class="d-flex justify-content-end mt-2">
                  <button class="btn btn-secondary" @click="workplaceAudience[index].isEditing = false;">Cancel</button>
                  <button class="btn btn-primary ms-2" @click="updateWorkplace">Save</button>
                </div>
                  </div>
                </li>
        </ul>
        <!-- college section -->
        <h5 class="mb-2 mt-3">College/School</h5>
        <a class="text-primary cursor-pointer plus-button mt-3" @click="openCloseAddCollege">
          <font-awesome-icon :icon="['fas', 'circle-plus']" /> 
          <span class="ms-2">Add college/School</span>
        </a>
        <!-- add college fields -->
        <div class="form-group" v-if="collegeAddFieldVisible">
                <input type="text" class="form-control mt-2" placeholder="College/School name" v-model="addCollege.name">
                <span class="text-danger">{{ addCollegeError.name }}</span>
                <input type="text" class="form-control mt-2" placeholder="Degree" v-model="addCollege.degree">
                <span class="text-danger">{{ addCollegeError.degree }}</span>
                <input type="text" class="form-control mt-2" placeholder="Address" v-model="addCollege.address">
                <span class="text-danger">{{ addCollegeError.address }}</span>
                <textarea class="form-control mt-2" cols="30" rows="5" placeholder="Description" v-model="addCollege.desc"></textarea>
                <h6 class="mt-3">Time Period</h6>
                
                <div class="mt-2 row">
                  
                  <div class="col-md-6">
                    <label for="">From</label>
                    <input type="date" class="form-control" v-model="addCollege.attend_from">
                    <span class="text-danger">{{ addCollegeError.attend_from }}</span>
                  </div>
                  <div class="col-md-6">
                    <label for="">To</label>
                    <input type="date" class="form-control" v-model="addCollege.attend_to" >
                    <span class="text-danger">{{ addCollegeError.attend_to }}</span>
                  </div>
                </div>
               <h6 class="mt-3">Audience</h6>
                <select  class="mt-2 form-control" v-model="addCollege.audience">
                    <option value="0">Public</option>
                    <option value="1">Friends</option>
                    <option value="2">Only Me</option>
                </select>
                <div class="d-flex justify-content-end mt-2">
                  <button class="btn btn-secondary" @click="openCloseAddCollege">Cancel</button>
                  <button class="btn btn-primary ms-2" @click="collegeAdd">Save</button>
                </div>
        </div>
        <!-- edit college Fields -->
        <div class="form-group" v-if="collegeEditFieldVisible">
                <input type="text" class="form-control mt-2" placeholder="College/School name" v-model="editCollege.name">
                <span class="text-danger">{{ editCollegeError.name }}</span>
                <input type="text" class="form-control mt-2" placeholder="Degree" v-model="editCollege.degree">
                <span class="text-danger">{{ editCollegeError.degree }}</span>
                <input type="text" class="form-control mt-2" placeholder="Address" v-model="editCollege.address">
                <span class="text-danger">{{ editCollegeError.address }}</span>
                <textarea class="form-control mt-2" cols="30" rows="5" placeholder="Description" v-model="editCollege.desc"></textarea>
                <h6 class="mt-3">Time Period</h6>
                
                <div class="mt-2 row">
                  
                  <div class="col-md-6">
                    <label for="">From</label>
                    <input type="date" class="form-control" v-model="editCollege.attend_from">
                    <span class="text-danger">{{ editCollegeError.attend_from }}</span>
                  </div>
                  <div class="col-md-6">
                    <label for="">To</label>
                    <input type="date" class="form-control" v-model="editCollege.attend_to" >
                    <span class="text-danger">{{ editCollegeError.attend_to }}</span>
                  </div>
                </div>
               <h6 class="mt-3">Audience</h6>
                <select  class="mt-2 form-control" v-model="editCollege.audience">
                    <option value="0">Public</option>
                    <option value="1">Friends</option>
                    <option value="2">Only Me</option>
                </select>
                <div class="d-flex justify-content-end mt-2">
                  <button class="btn btn-secondary" @click="collegeFieldClose">Cancel</button>
                  <button class="btn btn-primary ms-2" @click="updateCollege">Save</button>
                </div>
        </div>
        <!-- list colleges -->
        <ul style="list-style: none;">
                <li class=" mt-2" v-for="(college,index) in college" :key="college.id">
                  <div class="d-flex justify-content-between">
                    <div class="d-flex align-items-center">
                        <div class="d-flex flex-column ">
                            <span>{{ college.name }}</span>
                            <span class="text-small text-secondary">{{ college.degree }} </span>
                            <span class="text-small text-secondary">{{ college.address }} {{ college.attend_from }} to {{ college.attend_to }}</span>

                        </div>
                    </div>
                    <div class="d-flex justify-content-end align-items-center">
                      <a class="me-2 text-dark cursor-pointer" @click="loadAudienceCollege(college.id,index)">

                        <font-awesome-icon v-if="college.audience =='0'" :icon="['fas', 'earth-americas']" />
                        <font-awesome-icon v-if="college.audience =='1'" :icon="['fas', 'users']" />
                        <font-awesome-icon v-if="college.audience =='2'" :icon="['fas', 'lock']" />
                      </a>
                      <div class="dropdown">
                        <a  class="ms-4 text-dark cursor-pointer  rounded-circle bg-light edit-btn" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          <font-awesome-icon :icon="['fas', 'ellipsis']" />
                        </a>
                        <div class="dropdown-menu">
                          <a class="dropdown-item" @click="loadCollege(college.id)">Edit College/School</a>
                          <a class="dropdown-item"  @click="collegeDelete(college.id)">Delete College/School</a>
               
                        </div>
                      </div>
                     
                    </div>
                    </div>
                    <div class="mt-2 form-group" v-if="collegeAudience[index] && collegeAudience[index].isEditing">
                       <h6 class="mt-3">Audience</h6>
                <select  class="mt-2 form-control" v-model="editCollege.audience">
                    <option value="0">Public</option>
                    <option value="1">Friends</option>
                    <option value="2">Only Me</option>
                </select>
                <div class="d-flex justify-content-end mt-2">
                  <button class="btn btn-secondary" @click="collegeAudience[index].isEditing = false">Cancel</button>
                  <button class="btn btn-primary ms-2" @click="updateCollege">Save</button>
                </div>
                    </div>
                </li>
        </ul>
    </div>
</template>
<script>
import axiosInstance from '@/axios';
import { onMounted, reactive, ref,computed, watch } from 'vue';
import { useStore } from 'vuex';
export default {
    name:"about_work",
    setup(){
    const store = useStore();
    const addWorkplace = reactive({
      name:"",
      position:"",
      address:"",
      desc:"",
      works_from:"",
      works_to:"",
      audience:"0",
      current:false

    });
    const editWorkplace = reactive({
      id:"",
      name:"",
      position:"",
      address:"",
      desc:"",
      works_from:"",
      works_to:"",
      audience:"0",
      current:false

    });
    const addWorkplaceError = reactive({
      name:"",
      position:"",
      address:"",
      works_from:"",
      works_to:"",
     

    });
    const editWorkplaceError = reactive({
      name:"",
      position:"",
      address:"",
      works_from:"",
      works_to:"",
     

    });
    const workplaceAddFieldVisible = ref(false);
    const workplaceEditFieldVisible = ref(false);
    const workplaces = computed(() => store.state.workplaces);
    const college = computed(() => store.state.colleges);
    const addCollege = reactive({
        name:"",
        degree:"",
        attend_from:"",
        attend_to:"",
        desc:"",
        audience:"0",
        address:""
    });
    const addCollegeError = reactive({
        name:"",
        degree:"",
        attend_from:"",
        attend_to:"",
        address:""
    });
    const editCollege = reactive({
        id:"",
        name:"",
        degree:"",
        attend_from:"",
        attend_to:"",
        desc:"",
        audience:"0",
        address:""
    });
    const editCollegeError = reactive({
        name:"",
        degree:"",
        attend_from:"",
        attend_to:"",
        address:""
    });
    const collegeAddFieldVisible = ref(false);
    const collegeEditFieldVisible = ref(false);
    const workplaceAudience = ref([]);
    const collegeAudience = ref([]);
    
    onMounted(async () => {
      await fetchWorkplaces();
      await fetchColleges();
    });
    watch(workplaces,(newWorkplace)=>{
      workplaceAudience.value = [];
      for(let i=0; i<newWorkplace.length; i++ ){
        workplaceAudience.value.push({isEditing:false});
      }
    });
    watch(college,(newCollege)=>{
      collegeAudience.value = [];
      for(let i=0; i<newCollege.length; i++ ){
        collegeAudience.value.push({isEditing:false});
      }
      console.log(collegeAudience.value)
    });
    //for fetching workplaces
    const fetchWorkplaces = async () => {
      try {
        const resp = await axiosInstance.get('workplace/');
        store.commit('SET_WORKPLACES', resp.data);
      } catch (error) {
        console.error("Error occurred while fetching workplaces");
      }
    };
    //for fetching colleges
    const fetchColleges = async () => {
      try {
        const resp = await axiosInstance.get('college/');
        store.commit('SET_COLLEGES', resp.data);
      } catch (error) {
        console.error("Error occurred while fetching colleges");
      }
    };
    //for opening and closing add workplace
    const workplaceAddClick = ()=>{
      collegeAddFieldVisible.value = false;
      workplaceEditFieldVisible.value = false;
      collegeEditFieldVisible.value = false;
      collegeAudience.value.map(item=>item.isEditing = false)
      workplaceAudience.value.map(item=>item.isEditing = false)
      workplaceAddFieldVisible.value = !workplaceAddFieldVisible.value;
    }
    //for adding workplace
    const workplaceSave = async () => {
      try {
        const resp = await axiosInstance.post('workplace/', addWorkplace);
        store.commit('ADD_WORKPLACE', resp.data);
        workplaceAddFieldVisible.value = false;
      } catch (error) {
        console.error("Error occurred while adding workplace");
      }
    };
    //for deleting workplace
    const workplaceDelete = async (id) => {
      collegeAddFieldVisible.value = false;
      workplaceAddFieldVisible.value = false;
      workplaceEditFieldVisible.value = false;
      collegeEditFieldVisible.value = false;
      collegeAudience.value.map(item=>item.isEditing = false)
      workplaceAudience.value.map(item=>item.isEditing = false)
      try {
        await axiosInstance.delete(`workplace/${id}`);
        store.commit('REMOVE_WORKPLACE', id);
      } catch (error) {
        console.error(error);
      }
    };
    //for loading workplace in edit workplace while edit workplace btn clicked
    const loadWorkPlace = async(id)=>{
      collegeAddFieldVisible.value = false;
      workplaceAddFieldVisible.value = false;
      collegeEditFieldVisible.value = false;
      collegeAudience.value.map(item=>item.isEditing = false)
      workplaceAudience.value.map(item=>item.isEditing = false)
      await axiosInstance.get('workplace/'+id).then(resp=>{
 
        editWorkplace.id = resp.data.id
        editWorkplace.name = resp.data.name
        editWorkplace.position = resp.data.position
        editWorkplace.address = resp.data.address
        editWorkplace.current = resp.data.current
        editWorkplace.works_from = resp.data.works_from
        editWorkplace.works_to = resp.data.works_to
        editWorkplace.address = resp.data.address
        editWorkplace.audience = resp.data.audience
        workplaceEditFieldVisible.value = true;
      }).catch(err=>{
        console.error(err)
      })
    }
    //for updating workpalace
    const updateWorkplace = async () => {
      try {
        const resp = await axiosInstance.put(`workplace/${editWorkplace.id}/`, editWorkplace);
        store.commit('UPDATE_WORKPLACE', resp.data);
        workplaceEditFieldVisible.value =false;
        workplaceAudience.value.map(item=>item.isEditing = false)
      } catch (error) {
        console.error("Error occurred while updating workplace");
      }
    };
    //for removing to date from edit workplace while i currently work here is checked
    const workplaceEditClick = ()=>{
      workplaceEditFieldVisible.value = false;
    }
    //for removing to date from add workplace while i currently work here is checked
    const addWorkplaceCurrent = ()=>{
      if(addWorkplace.current === true){
        addWorkplace.works_to = ""
      }
    }
    //for removing to date while i currently work here is checked
    const editWorkplaceCurrent = ()=>{
      if(editWorkplace.current === true){
        editWorkplace.works_to = ""
      }
    }
    //for college
    //for opening and closing add college/school field
    const openCloseAddCollege = ()=>{

        workplaceAddFieldVisible.value = false;
        workplaceEditFieldVisible.value = false;
        collegeEditFieldVisible.value = false;
        collegeAudience.value.map(item=>item.isEditing = false)
        workplaceAudience.value.map(item=>item.isEditing = false)
        collegeAddFieldVisible.value = !collegeAddFieldVisible.value;
    }
    //for adding college/school
    const collegeAdd = async () => {
      try {
        const resp = await axiosInstance.post('college/', addCollege);
        store.commit('ADD_COLLEGE', resp.data);
        collegeAddFieldVisible.value = false;
      } catch (error) {
        console.error("Error occurred while adding college");
      }
    };
    //for deleting college/School
    const collegeDelete = async (id) => {
      collegeAddFieldVisible.value = false;
      workplaceAddFieldVisible.value = false;
      workplaceEditFieldVisible.value = false;
      collegeEditFieldVisible.value = false;
      workplaceAudience.value.map(item=>item.isEditing = false)
      collegeAudience.value.map(item=>item.isEditing = false)
      try {
        await axiosInstance.delete(`college/${id}/`);
        store.commit('REMOVE_COLLEGE', id);
      } catch (error) {
        console.error(error);
      }
    };
    //for loading college in edit college while edit college btn clicked
    const loadCollege = async(id)=>{
      collegeAddFieldVisible.value = false;
      workplaceAddFieldVisible.value = false;
      workplaceEditFieldVisible.value = false;
      collegeAudience.value.map(item=>item.isEditing = false)
      workplaceAudience.value.map(item=>item.isEditing = false)
      await axiosInstance.get('college/'+id).then(resp=>{
 
        editCollege.id = resp.data.id
        editCollege.name = resp.data.name
        editCollege.degree = resp.data.degree
        editCollege.address = resp.data.address
        editCollege.attend_from = resp.data.attend_from
        editCollege.attend_to = resp.data.attend_to
        editCollege.address = resp.data.address
        editCollege.audience = resp.data.audience
        collegeEditFieldVisible.value = true;
      }).catch(err=>{
        console.error(err)
      })
    }
    //for closing edit college fields
    const collegeFieldClose =()=>{
        collegeEditFieldVisible.value = false;
    }
    //for updating College
    const updateCollege = async () => {
      try {
        const resp = await axiosInstance.put(`college/${editCollege.id}/`, editCollege);
        store.commit('UPDATE_COLLEGE', resp.data);
        collegeEditFieldVisible.value = false;
        collegeAudience.value.map(item=>item.isEditing = false)
      } catch (error) {
        console.error("Error occurred while updating college");
      }
    };
    const loadAudienceWorkplace = async(id,index)=>{
      const index_pr = index
      collegeAddFieldVisible.value = false;
      workplaceAddFieldVisible.value = false;
      collegeEditFieldVisible.value = false;
      workplaceEditFieldVisible.value = false;
      collegeAudience.value.map(item=>item.isEditing = false)
      workplaceAudience.value.map(item=>item.isEditing = false)
      await axiosInstance.get('workplace/'+id).then(resp=>{
 
        editWorkplace.id = resp.data.id
        editWorkplace.name = resp.data.name
        editWorkplace.position = resp.data.position
        editWorkplace.address = resp.data.address
        editWorkplace.current = resp.data.current
        editWorkplace.works_from = resp.data.works_from
        editWorkplace.works_to = resp.data.works_to
        editWorkplace.address = resp.data.address
        editWorkplace.audience = resp.data.audience
        workplaceAudience.value[index_pr].isEditing = true;
        
      }).catch(err=>{
        console.error(err)
      })
    }
    const loadAudienceCollege = async(id,index)=>{
      const index_pr = index;
      collegeAddFieldVisible.value = false;
      workplaceAddFieldVisible.value = false;
      workplaceEditFieldVisible.value = false;
      workplaceAudience.value.map(item=>item.isEditing = false)
      collegeAudience.value.map(item=>item.isEditing = false)
      collegeEditFieldVisible.value = false;
      await axiosInstance.get('college/'+id).then(resp=>{
 
        editCollege.id = resp.data.id
        editCollege.name = resp.data.name
        editCollege.degree = resp.data.degree
        editCollege.address = resp.data.address
        editCollege.attend_from = resp.data.attend_from
        editCollege.attend_to = resp.data.attend_to
        editCollege.address = resp.data.address
        editCollege.audience = resp.data.audience
        collegeAudience.value[index_pr].isEditing = true;
        
      }).catch(err=>{
        console.error(err)
      })
    }

    return {addWorkplace,workplaceAddClick,workplaceAddFieldVisible,workplaces,workplaceSave,addWorkplaceError,workplaceDelete,loadWorkPlace,editWorkplace,workplaceEditFieldVisible,editWorkplaceError,updateWorkplace,workplaceEditClick,addWorkplaceCurrent,editWorkplaceCurrent,addCollege,college,addCollegeError,collegeAddFieldVisible,openCloseAddCollege,collegeAdd,collegeDelete,loadCollege,editCollegeError,editCollege,collegeEditFieldVisible,collegeFieldClose,updateCollege,workplaceAudience,loadAudienceWorkplace,collegeAudience,loadAudienceCollege}
  }
}
</script>
<style>
.cursor-pointer{
  cursor: pointer;
}


.plus-button{
  display:flex;
  align-items: center;
  text-decoration: none;
}
.plus-button:hover{
  text-decoration: underline;
}
.plus-button svg{
font-size:1.5rem;
}
.text-small {
  font-size: 0.8rem;
}
.text-big {
  font-size: 1.7rem;
}
.edit-btn{
padding: 5px 10px ;
}
.edit-btn:hover{
  opacity: 0.8;
}
</style>