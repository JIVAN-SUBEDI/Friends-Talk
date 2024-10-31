<template>
  <div class="container">
    <div class="row d-flex justify-content-center align-items-center">
      <div class="col-md-8 mt-5">
        <div class="bg-white p-5 rounded-3 shadow-sm border">
          <div>
            <p class="text-center text-success" style="font-size: 5.5rem">
              <font-awesome-icon :icon="['fas', 'envelope-circle-check']" />
            </p>
            <p class="text-center h5">Please check your email</p>
            <p class="text-muted text-center">
              We've sent a code to {{$route.params.email}}
            </p>
            <div class="d-flex justify-content-between pt-4 pb-2">
              <input
                v-for="(value, index) in otp"
                :key="index"
                :disabled="otpCurrentIndex !== index"
                v-model="otp[index]"
                class="otp-letter-input"
                type="text"
                maxlength="1"
                @input="onInput($event, index)"
                @keydown="onKeydown($event, index)"
                ref="otpInputs"
              />
            </div>
            <p class="text-muted text-center">
              Didn't get the code?
              <a class="text-success" @click="resendOtp()">Click to resend.</a>
            </p>

            <div class="row pt-5">
              <div class="col-6">
                <button class="btn btn-outline-secondary w-100" @click="cancelOtp()">Cancel</button>
              </div>
              <div class="col-6">
                <button
                @click="otpSubmit()"
                  class="btn btn-success w-100"
                  :disabled="otp[5] === ''"
                >
                  Verify
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, nextTick } from "vue";
import { useRoute,useRouter } from "vue-router";
import axios from "axios";
import { useToast } from "vue-toastification";


export default {
  name: "otp_page",
  setup() {
    const otp = ref(["", "", "", "", "", ""]);
    const otpCurrentIndex = ref(0);
    const otpInputs = ref([]);
    const route = useRoute();
    const router = useRouter();
    const toast = useToast();
    onMounted(() => {
      otpInputs.value = document.querySelectorAll(".otp-letter-input");
      nextTick(() => {
        otpInputs.value[otpCurrentIndex.value].focus(); // Focus the first input on page load
      });
    });

    const onInput = (e, index) => {
      const value = e.target.value;
      if (value.length === 1 && index < 5) {
        otp.value[index] = value;
        otpCurrentIndex.value = index + 1;

        // Shift focus after DOM updates
        nextTick(() => {
          otpInputs.value[otpCurrentIndex.value].focus();
        });
      }
    };

    const onKeydown = (e, index) => {
      if (e.key === "Backspace") {
        if (otp.value[index] === "") {
          if (index > 0) {
            otpCurrentIndex.value = index - 1;

            // Shift focus after DOM updates
            nextTick(() => {
              otpInputs.value[otpCurrentIndex.value].focus();
            });
          }
        } else {
          otp.value[index] = "";
        }
      }
    };
    const otpSubmit =()=>{
   
      const mainOtp = otp.value.join('');
      

      axios.get(`verify-otp/${route.params.email}/${mainOtp}`).then(resp=>{
        toast.info(resp.data.message,{
          timeout:5000
        }
        )
        const time = ref(5);
        const toastid =toast.success(`Redirecting to login in ${time.value} seconds...`,{timeout:5000})
       const myInterval =  setInterval(()=>{
          if(time.value === 0){
            router.push('/Login');
            clearInterval(myInterval);
          }
          toast.update(toastid,{content:`Redirecting to login in ${time.value} seconds...`})
          time.value--;
   
        
        },1000)
        
      }).catch(err=>{
        toast.error(err.response.data.message,{
          timeout:5000
        })
      })
    }
    const resendOtp = ()=>{
      axios.get(`forgot-password/${route.params.email}`).then(resp=>{
        toast.info(resp.data.message)
      }).catch(err=>{
        toast.error(err.response.data.message,{
          timeout:5000
        });
    });
  }
    const cancelOtp = ()=>{
      router.push('/login');
    }

    return { otp, otpCurrentIndex, onInput, onKeydown, otpInputs,otpSubmit,resendOtp,cancelOtp };
  },
};
</script>

<style scoped>
.otp-letter-input {
  width: 90px;
  height: 90px;
  border: 1px solid #198754;
  border-radius: 10px;
  color: #198754;
  font-size: 60px;
  text-align: center;
  font-weight: bold;
}
.btn {
  height: 50px;
}
a{
  cursor: pointer;
}
</style>
