<template>
  <div>
    <h5>Basic Info</h5>
    <ul>
      <li class="d-flex justify-content-between mt-2" v-if="!genderFieldVisible && !genderFieldVisibleAudience">
        <div class="d-flex align-items-center">
          <font-awesome-icon
            :icon="['fas', 'user']"
            class="text-secondary text-big"
          />
          <div class="d-flex flex-column ms-2">
            <span>Gender</span>
            <span class="text-small ms-2 text-secondary">{{ gender.gender }}</span>
          </div>
        </div>
        <div class="d-flex justify-content-end align-items-center">
          <a class="me-2 text-dark cursor-pointer" @click="genderFieldVisibleAudienceChange">
            <font-awesome-icon v-if="gender.gender_audience == '0'" :icon="['fas', 'earth-americas']" />
            <font-awesome-icon v-if="gender.gender_audience=='1'" :icon="['fas', 'users']" />
            <font-awesome-icon v-if="gender.gender_audience =='2'" :icon="['fas', 'lock']" />
          </a>
      
            <a
              class="ms-4 text-dark cursor-pointer rounded-circle bg-light edit-btn" @click="genderFieldVisibleChange"
              
            >
              <font-awesome-icon :icon="['fas', 'pen']" />
            </a>
            
   
        </div>
        
      </li>
      <div class="mt-3 form-group" v-if="genderFieldVisible">
            <select  class="form-control" v-model="gender.gender">
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="others">Others</option>
            </select>
          <h6 class="mt-3">Audience</h6>
          <select class="mt-2 form-control"  v-model="gender.gender_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="genderFieldVisibleChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateGender">
              Save
            </button>
          </div>
    </div>
      <div class="mt-3 form-group" v-if="genderFieldVisibleAudience">
    
          <h6 class="mt-3">Select Audience</h6>
          <select class="mt-2 form-control"  v-model="gender.gender_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="genderFieldVisibleAudienceChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateGender">
              Save
            </button>
          </div>
    </div>
      <li class="d-flex justify-content-between mt-2" v-if="!dateFieldVisible && !dateFieldVisibleAudience">
        <div class="d-flex align-items-center">
          <font-awesome-icon
            :icon="['fas', 'cake-candles']"
            class="text-secondary text-big"
          />
          <div class="d-flex flex-column ms-2">
            <span>Date of birth</span>
            <span class="text-small ms-2 text-secondary">{{ dob.date_of_birth }}</span>
          </div>
        </div>
        <div class="d-flex justify-content-end align-items-center">
          <a class="me-2 text-dark cursor-pointer" @click="dobFieldVisibleAudienceChange">
            <font-awesome-icon v-if="dob.date_of_birth_audience == '0'" :icon="['fas', 'earth-americas']" />
            <font-awesome-icon v-if="dob.date_of_birth_audience =='1'" :icon="['fas', 'users']" />
            <font-awesome-icon v-if="dob.date_of_birth_audience =='2'" :icon="['fas', 'lock']" />
          </a>
        
            <a class="ms-4 text-dark cursor-pointer rounded-circle bg-light edit-btn" @click="dobFieldVisibleChange">
              <font-awesome-icon :icon="['fas', 'pen']" />
            </a>
        
        
        </div>
      </li>
      <div class="mt-3 form-group" v-if="dateFieldVisible">
          <input type="date" class="form-control" v-model="dob.date_of_birth">
          <h6 class="mt-3">Audience</h6>
          <select class="mt-2 form-control"  v-model="dob.date_of_birth_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="dobFieldVisibleChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateDob">
              Save
            </button>
          </div>
    </div>
      <div class="mt-3 form-group" v-if="dateFieldVisibleAudience">
         
          <h6 class="mt-3">Select Audience</h6>
          <select class="mt-2 form-control"  v-model="dob.date_of_birth_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="dobFieldVisibleAudienceChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateDob">
              Save
            </button>
          </div>
    </div>
      <li class="d-flex justify-content-between mt-2" v-if="!relationshipFieldVisible && !relationshipFieldVisibleAudience">
        <div class="d-flex align-items-center">
          <font-awesome-icon
            :icon="['fas', 'heart']"
            class="text-secondary text-big"
          />
          <div class="d-flex flex-column ms-2">
            <span> Relationship</span>
            <span v-if="relationship.relationship ==''" class="text-small ms-2 text-secondary">None</span>
            <span v-else class="text-small ms-2 text-secondary">{{ relationship.relationship }}</span>
          </div>
        </div>
        <div class="d-flex justify-content-end align-items-center">
          <a class="me-2 text-dark cursor-pointer" @click="relationshipFieldAudienceVisibleChange">
            <font-awesome-icon v-if="relationship.relationship_audience == '0'" :icon="['fas', 'earth-americas']" />
            <font-awesome-icon v-if="relationship.relationship_audience =='1'" :icon="['fas', 'users']" />
            <font-awesome-icon v-if="relationship.relationship_audience =='2'" :icon="['fas', 'lock']" />
          </a>
         
            <a
              class="ms-4 text-dark cursor-pointer rounded-circle bg-light edit-btn" @click="relationshipFieldVisibleChange"
          
            >
              <font-awesome-icon :icon="['fas', 'pen']" />
            </a>
            
        </div>
      </li>
      <div class="mt-3 form-group" v-if="relationshipFieldVisible">
            <select  class="form-control" v-model="relationship.relationship">
                <option value="">Status</option>
                <option value="single">Single</option>
                <option value="married">Married</option>
                <option value="in a relationship">in a Relationship</option>
                <option value="divorced">Divorced</option>
                <option value="widowed">Widowed</option>
                <option value="seprated">Seprated</option>
            </select>
          <h6 class="mt-3">Audience</h6>
          <select class="mt-2 form-control"  v-model="relationship.relationship_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="relationshipFieldVisibleChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateRelationship">
              Save
            </button>
          </div>
    </div>
      <div class="mt-3 form-group" v-if="relationshipFieldVisibleAudience">
    
          <h6 class="mt-3">Select Audience</h6>
          <select class="mt-2 form-control"  v-model="relationship.relationship_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="relationshipFieldAudienceVisibleChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateRelationship">
              Save
            </button>
          </div>
    </div>
    <li class="d-flex justify-content-between mt-2" v-if="!primaryFieldVisible && !primaryFieldVisibleAudience">
      <div class="d-flex align-items-center">
        <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big" />
        <div class="d-flex flex-column ms-2">
          <span>Primary Phone Number</span>
          <span v-if="primary.primary_phone_number == null || primary.primary_phone_number == ''" class="text-small ms-2 text-secondary">None</span>
          <span v-else class="text-small ms-2 text-secondary">{{ primary.primary_phone_number }}</span>
        </div>
      </div>
      <div class="d-flex justify-content-end align-items-center">
        <!-- Audience icon logic -->
        <a class="me-2 text-dark cursor-pointer" @click="primaryFieldVisibleAudienceChange">
          <font-awesome-icon v-if="primary.primary_phone_number_audience == '0'" :icon="['fas', 'earth-americas']" />
          <font-awesome-icon v-if="primary.primary_phone_number_audience == '1'" :icon="['fas', 'users']" />
          <font-awesome-icon v-if="primary.primary_phone_number_audience == '2'" :icon="['fas', 'lock']" />
        </a>

        <!-- Corrected logic for pen and plus icons -->
        <a class="ms-4 text-dark cursor-pointer rounded-circle bg-light edit-btn" @click="primaryFieldVisibleChange">
          <!-- Show 'pen' icon when phone number is not empty (can edit) -->
          <font-awesome-icon v-if="primary.primary_phone_number == null || primary.primary_phone_number == ''" :icon="['fas', 'plus']" />
          <!-- Show 'plus' icon when phone number is empty (can add new number) -->
          <font-awesome-icon v-else :icon="['fas', 'pen']" />
        </a>
      </div>
    </li>
    <div class="mt-3 form-group" v-if="primaryFieldVisibleAudience">
       
          <h6 class="mt-3">Select Audience</h6>
          <select class="mt-2 form-control"  v-model="primary.primary_phone_number_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="primaryFieldVisibleAudienceChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updatePrimary">
              Save
            </button>
          </div>
    </div>
    <div class="mt-3 form-group" v-if="primaryFieldVisible">
          <input type="text" class="form-control" v-model="primary.primary_phone_number" placeholder="primary phone number">
          <h6 class="mt-3">Audience</h6>
          <select class="mt-2 form-control"  v-model="primary.primary_phone_number_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="primaryFieldVisibleChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updatePrimary">
              Save
            </button>
          </div>
    </div>
    <li class="d-flex justify-content-between mt-2" v-if="!secondaryFieldVisible && !secondaryFieldVisibleAudience">
      <div class="d-flex align-items-center">
        <font-awesome-icon :icon="['fas', 'phone']" class="text-secondary text-big" />
        <div class="d-flex flex-column ms-2">
          <span>Secondary Phone Number</span>
          <span v-if="secondary.secondary_phone_number == null || secondary.secondary_phone_number == ''" class="text-small ms-2 text-secondary">None</span>
          <span v-else class="text-small ms-2 text-secondary">{{ secondary.secondary_phone_number }}</span>
        </div>
      </div>
      <div class="d-flex justify-content-end align-items-center">
        <!-- Audience icon logic -->
        <a class="me-2 text-dark " @click="secondaryFieldVisibleAudienceChange">
          <font-awesome-icon v-if="secondary.secondary_phone_number_audience == '0'" :icon="['fas', 'earth-americas']" />
          <font-awesome-icon v-if="secondary.secondary_phone_number_audience == '1'" :icon="['fas', 'users']" />
          <font-awesome-icon v-if="secondary.secondary_phone_number_audience == '2'" :icon="['fas', 'lock']" />
        </a>

    <!-- Corrected logic for pen and plus icons -->
    <a class="ms-4 text-dark cursor-pointer rounded-circle bg-light edit-btn" @click="secondaryFieldVisibleChange">
      <!-- Show 'pen' icon when phone number is not empty (can edit) -->
      <font-awesome-icon v-if="secondary.secondary_phone_number == null || secondary.secondary_phone_number == ''" :icon="['fas', 'plus']" />
      <!-- Show 'plus' icon when phone number is empty (can add new number) -->
      <font-awesome-icon v-else :icon="['fas', 'pen']" />
    </a>
  </div>
    </li>
    <div class="mt-3 form-group" v-if="secondaryFieldVisible">
          <input type="text" class="form-control" v-model="secondary.secondary_phone_number" placeholder="Secondary phone number">
          <h6 class="mt-3">Audience</h6>
          <select class="mt-2 form-control"  v-model="secondary.secondary_phone_number_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="secondaryFieldVisibleChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateSecondary">
              Save
            </button>
          </div>
    </div>
    <div class="mt-3 form-group" v-if="secondaryFieldVisibleAudience">
          <h6 class="mt-3">Select Audience</h6>
          <select class="mt-2 form-control"  v-model="secondary.secondary_phone_number_audience">
            <option value="0">Public</option>
            <option value="1">Friends</option>
            <option value="2">Only Me</option>
          </select>
          <div class="d-flex justify-content-end mt-2">
            <button class="btn btn-secondary" @click="secondaryFieldVisibleAudienceChange">
              Cancel
            </button>
            <button class="btn btn-primary ms-2" @click="updateSecondary">
              Save
            </button>
          </div>
    </div>

    </ul>
  </div>
</template>
<script>
import axiosInstance from '@/axios';
import { onMounted, reactive, ref } from 'vue';
import { useStore } from 'vuex';
export default {
  name: "about_contact",
  setup(){
    const store = useStore();
    const gender = reactive({
        gender:"",
        gender_audience:"0",
    });
    const dob = reactive({
        date_of_birth:"",
        date_of_birth_audience:"0",
    });
    const relationship = reactive({
        relationship:"",
        relationship_audience:"0",
    });
    const primary = reactive({
        primary_phone_number:"",
        primary_phone_number_audience:"0",
    });
    const secondary = reactive({
        secondary_phone_number:"",
        secondary_phone_number_audience:"0",
    });

    const genderFieldVisible = ref(false);
    const genderFieldVisibleAudience = ref(false);
    const dateFieldVisible = ref(false);
    const dateFieldVisibleAudience = ref(false);
    const relationshipFieldVisible = ref(false);
    const relationshipFieldVisibleAudience = ref(false);
    const primaryFieldVisible = ref(false);
    const primaryFieldVisibleAudience = ref(false);
    const secondaryFieldVisible = ref(false);
    const secondaryFieldVisibleAudience = ref(false);
    onMounted(async()=>{
        await axiosInstance.get('basic-info').then(resp=>{
            gender.gender = resp.data[0].gender
            gender.gender_audience = resp.data[0].gender_audience
            dob.date_of_birth = resp.data[0].date_of_birth
            dob.date_of_birth_audience = resp.data[0].date_of_birth_audience
            relationship.relationship = resp.data[0].relationship
            relationship.relationship_audience = resp.data[0].relationship_audience
            primary.primary_phone_number = resp.data[0].primary_phone_number
            primary.primary_phone_number_audience = resp.data[0].primary_phone_number_audience
            secondary.secondary_phone_number = resp.data[0].secondary_phone_number
            secondary.secondary_phone_number_audience = resp.data[0].secondary_phone_number_audience
            store.commit('SET_PROFILE',resp.data[0])
        }).catch(()=>{
            console.error("Some error occured while fetching basic info.")
        });
    });
    //for showing and hiding gender field
    const genderFieldVisibleChange = ()=>{
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        genderFieldVisible.value = !genderFieldVisible.value
    }
    //for showing and hiding gender audience field
    const genderFieldVisibleAudienceChange = ()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        genderFieldVisibleAudience.value = !genderFieldVisibleAudience.value
    }
    //for updating gender
    const updateGender = async()=>{
        await axiosInstance.post("gender/update/",gender).then(()=>{
            genderFieldVisible.value =false;
            store.commit('UPDATE_GENDER',gender)
            genderFieldVisibleAudience.value = false;
        }).catch(()=>{
            console.log("Some error occured while updating gender")
        });
    }
    //for showing and hiding dob field 
    const dobFieldVisibleChange = ()=>{
      genderFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        dateFieldVisible.value = !dateFieldVisible.value
    }
    //for showing and hididng dob audience
    const dobFieldVisibleAudienceChange = ()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        dateFieldVisibleAudience.value = !dateFieldVisibleAudience.value
    }
    //for updating dob
    const updateDob = async()=>{
        await axiosInstance.post("dob/update/",dob).then(()=>{
            dateFieldVisible.value =false;
            store.commit('UPDATE_DOB',dob)
            dateFieldVisibleAudience.value = false;
        }).catch(()=>{
            console.log("Some error occured while updating dob")
        });
    }
      //for showing and hiding edit relationship
    const relationshipFieldVisibleChange = ()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        relationshipFieldVisible.value = !relationshipFieldVisible.value
    }
      //for showing and hiding change audience relationship
    const relationshipFieldAudienceVisibleChange = ()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        relationshipFieldVisibleAudience.value = !relationshipFieldVisibleAudience.value
    }
    //for updating relationship
    const updateRelationship = async()=>{
        await axiosInstance.post("relationship/update/",relationship).then(()=>{
            relationshipFieldVisible.value =false;
            store.commit('UPDATE_RELATIONSHIP',relationship)
        }).catch(()=>{
            console.log("Some error occured while updating relationship")
        });
    }
      //for showing and hiding edit of primary phone number
    const primaryFieldVisibleChange = ()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        primaryFieldVisible.value = !primaryFieldVisible.value
    }
      //for showing and hiding change audience of pirmary phone number
    const primaryFieldVisibleAudienceChange = ()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;

      secondaryFieldVisibleAudience.value = false;
        primaryFieldVisibleAudience.value = !primaryFieldVisibleAudience.value
    }
        //for updating primary phone number
    const updatePrimary = async()=>{
        await axiosInstance.post("primary/update/",primary).then(()=>{
            primaryFieldVisible.value =false;
            primaryFieldVisibleAudience.value = false;
            store.commit('UPDATE_PRIMARY',primary)
        }).catch(()=>{
            console.log("Some error occured while updating primary number")
        });
    }
    //for showing and hiding edit secondary phone number
    const secondaryFieldVisibleChange = ()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
   
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = false;
        secondaryFieldVisible.value = !secondaryFieldVisible.value
    }
    //for updating secondary phone number
    const updateSecondary = async()=>{
        await axiosInstance.post("secondary/update/",secondary).then(()=>{
            secondaryFieldVisible.value =false;
            secondaryFieldVisibleAudience.value = false;
            store.commit('UPDATE_SECONDARY',secondary)
        }).catch(()=>{
            console.log("Some error occured while updating secondary number")
        });
    }
    //for showing and hiding change audience of secondary phone number
    const secondaryFieldVisibleAudienceChange =()=>{
      genderFieldVisible.value = false;
      dateFieldVisible.value = false;
      relationshipFieldVisible.value = false;
      primaryFieldVisible.value = false;
      secondaryFieldVisible.value = false;
      genderFieldVisibleAudience.value = false;
      dateFieldVisibleAudience.value = false;
      relationshipFieldVisibleAudience.value = false;
      primaryFieldVisibleAudience.value = false;
      secondaryFieldVisibleAudience.value = !secondaryFieldVisibleAudience.value
    }
    return{gender,genderFieldVisible,genderFieldVisibleChange,updateGender,dateFieldVisible,dob,dobFieldVisibleChange,updateDob,relationship,relationshipFieldVisibleChange,relationshipFieldVisible,updateRelationship,primary,primaryFieldVisible,primaryFieldVisibleChange,updatePrimary,secondary,secondaryFieldVisible,secondaryFieldVisibleChange,updateSecondary,secondaryFieldVisibleAudience,secondaryFieldVisibleAudienceChange,primaryFieldVisibleAudience,primaryFieldVisibleAudienceChange,relationshipFieldAudienceVisibleChange,relationshipFieldVisibleAudience,dateFieldVisibleAudience,dobFieldVisibleAudienceChange,genderFieldVisibleAudience,genderFieldVisibleAudienceChange}
  }
};
</script>
