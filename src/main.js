import { createApp } from 'vue'
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faMessage,faBell,faMagnifyingGlass,faChevronDown,faArrowRightFromBracket,faComment,faGear,faUser,faImage,faFaceSmile,faPersonRunning,faXmark } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faMessage,faBell,faMagnifyingGlass,faChevronDown,faArrowRightFromBracket,faComment,faGear,faUser,faImage,faFaceSmile,faPersonRunning,faXmark)
const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
