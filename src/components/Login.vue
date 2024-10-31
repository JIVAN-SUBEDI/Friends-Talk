<template>
  <div>
  <div class="bg-light d-flex justify-content-center align-items-center height">
    <div class="">
      <div class="card border-0 w-60">
        <div class="card-body">
          <div class="row">
            <div class="col">
              <h4 class="mt-3">Friends Talk</h4>
              <p class="text-secondary">Welcome Back,</p>
              <p class="text-secondary">
                We're glad to see you again! Log in to connect with your
                friends, share your moments, and explore what's happening around
                the world. Your community is just a click away!
              </p>
              <div class="d-flex justify-content-center">
                <button
                  class="btn btn-success mt-3"
                  data-bs-toggle="modal"
                  data-bs-target="#signup"
                >
                  Create new account
                </button>
              </div>
            </div>
            <div class="col">
              <h4 class="text-center mt-3">Login</h4>
              <div class="alert alert-info" v-if="resend.show"><a href="#" @click="resend"> Resend Verification Link</a></div>
              <div class="mt-3">
                <div class="form-group">
                  <label for="">Email Address</label>
                  <input
                    type="email"
                    class="form-control mt-2"
                    placeholder="Email Address"
                    v-model="login_details.email"
                    />
                    <span class="text-danger">{{ login_error.email }}</span>
                  </div>
                  <div class="form-group mt-3 mb-3">
                    <label for="">Password</label>
                    <input
                    type="password"
                    class="form-control mt-2"
                    placeholder="Password"
                    v-model="login_details.password"
                    />
                    <span class="text-danger">{{ login_error.password }}</span>
                </div>

                <a href="#" class="text-decoration-none" data-bs-toggle="modal" data-bs-target="#forgot">Forgot Password?</a>
                <div class="mt-4 d-flex">
                  <button class="btn btn-primary btn-custom" @click="login()">Login</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="signup"
    tabindex="-1"
    aria-labelledby="signupLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="signupLabel">Signup</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row form-group">
            <div class="col-md-6">
              <label for="">First name</label>
              <input
                type="text"
                placeholder="First name"
                class="form-control" v-model="signup_details.first_name"
              />
              <span class="text-danger">{{ signup_error.first_name }}</span>
            </div>
            <div class="col-md-6">
              <label for="">Last name</label>
              <input type="text" placeholder="Last name" class="form-control" v-model="signup_details.last_name"/>
              <span class="text-danger">{{ signup_error.last_name }}</span>
            </div>
          </div>
          <div class="form-group mt-2">
            <label for="">Email Address</label>
            <input
              type="email"
              class="form-control"
              placeholder="someone@example.com"
              v-model="signup_details.email"
            />
            <span class="text-danger">{{ signup_error.email }}</span>
          </div>
          <div class="form-group mt-2">
            <label for="">Password</label>
            <input
              type="password"
              class="form-control"
              placeholder="password"
              v-model="signup_details.password"
            />
            <span class="text-danger">{{ signup_error.password }}</span>
          </div>
          <div class="form-group mt-2">
            <label for="">Date of birth</label>
            <input
              type="date"
              class="form-control"
              placeholder="Date of birth"
              v-model="signup_details.date_of_birth"
            />
            <span class="text-danger">{{ signup_error.date_of_birth }}</span>
          </div>
          <label for="" class="mt-2">Gender</label>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gender"
              id="male"
              value="male"
              checked
              v-model="signup_details.gender"
            />
            <label class="form-check-label" for="male"> Male </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gender"
              id="female"
              value="female"
              v-model="signup_details.gender"
            />
            <label class="form-check-label" for="female"> Female </label>
          </div>
          <div class="form-check">
            <input
              class="form-check-input"
              type="radio"
              name="gender"
              id="Others"
              value="others"
              v-model="signup_details.gender"
            />
            <label class="form-check-label" for="Others"> Others </label>
       
          </div>
          <div class="d-flex justify-content-center">
            <button class="btn btn-success" @click="signup">Signup</button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="modal fade"
    id="forgot"
    tabindex="-1"
    aria-labelledby="signupLabel"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h1 class="modal-title fs-5" id="signupLabel">Forgot Password?</h1>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">

          <div class="form-group mt-2">
            <label for="">Email Address</label>
            <input
              type="email"
              class="form-control"
              placeholder="someone@example.com"
              v-model="forgot.email"
            />
          
          </div>
    
          <div class="d-flex justify-content-center mt-3">
            <button class="btn btn-success" @click="forgot_password">Forgot Password</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import { onMounted, reactive,ref } from "vue";
import { useToast } from "vue-toastification";
import axios from "axios";
import { useRouter } from "vue-router";
import { Modal } from "bootstrap";
import { useStore } from "vuex";

export default {
  name: "login_page",
  setup() {
    const toast = useToast();
    const router = useRouter();
    const forgotModal = ref();
    const store = useStore();
    const resend = reactive({
      show :false,
      email:""
    });
    const login_details = reactive({
      email:"",
      password:"",
    })
    const login_error = reactive({
      email:"",
      password:"",
    })
    const signup_details = reactive({
      first_name:"",
      last_name:"",
      date_of_birth:"",
      gender:"male",
      email:"",
      password:""

    });
    const signup_error = reactive({
      first_name:"",
      last_name:"",
      date_of_birth:"",
      gender:"male",
      email:"",
      password:""

    });
    const forgot = reactive({
      email:""
    })
    onMounted(()=>{
      forgotModal.value = new Modal(document.getElementById("forgot"));
    })
    const signup = async()=>{
      signup_error.first_name = "",
      signup_error.last_name = "",
      signup_error.gender = "",
      signup_error.date_of_birth = "",
      signup_error.email = "",
      signup_error.password = "",
      await axios.post("http://localhost:8000/api/register/",signup_details).then(resp=>{
        toast.success(resp.data.message, {
        timeout: 5000
      });
      }).catch(error=>{
        const errors = error.response.data.field_errors
        if(errors){
          if(errors.first_name){
            signup_error.first_name = errors.first_name[0]
          }
          if(errors.last_name){
            signup_error.last_name = errors.last_name[0]
          }
          if(errors.gender){
            signup_error.gender = errors.gender[0]
          }
          if(errors.email){
            signup_error.email = errors.email[0]
          }
          if(errors.password){
            signup_error.password = errors.password[0]
          }
          if(errors.date_of_birth){
            signup_error.date_of_birth = errors.date_of_birth[0]
          }
        }
      })
    }
    const forgot_password = async()=>{
      await axios.get("forgot-password/"+forgot.email).then(()=>{
        forgotModal.value.hide();
        router.push(`/otp-verify/${forgot.email}`);
      }).catch(err=>{
        toast.error(err.response.data.message,{
          timeout:5000
        })
      })
    }
    const login = async()=>{
      login_error.email = ''
      login_error.password = ''
      await axios.post('login/',login_details).then(resp=>{
        console.log(resp)
        const access_token = resp.data.token.access;
        const refresh_token = resp.data.token.refresh;
          store.dispatch('login',{access_token,refresh_token})
        router.push('/');
      }).catch(err=>{
        if (err.response.data.field_errors){
          const field_errors = err.response.data.field_errors;
          if(field_errors.email){
            login_error.email = field_errors.email[0]
            
          }
          if(field_errors.password){  
            login_error.password = field_errors.password[0]
          }
          
        }
        if(err.response.data.non_field_errors){
          toast.error(err.response.data.non_field_errors,{
            timeout:5000
          });
          if(err.response.status === 403){
            resend.show = true;
            resend.email = err.response.data.non_field_errors.email 
          }
         
        }
      })
    }
    return { toast,signup,signup_error,signup_details,forgot,forgot_password,login,login_details,login_error,resend };
  },
};
</script>
<style scoped>
.height {
  height: 100vh;
}
.w-60 {
  width: 55vw;
}
.btn-custom {
  width: 100%;
}
</style>
