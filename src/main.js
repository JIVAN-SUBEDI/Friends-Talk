import { createApp } from 'vue'
import App from './App.vue'
import router from './route'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import Toast from "vue-toastification";
import store from './store'
import './axios'
import messageModal from './components/partials/messageModal.vue'
// Import the CSS or use your own!
import "vue-toastification/dist/index.css";
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faMessage,faBell,faMagnifyingGlass,faChevronDown,faArrowRightFromBracket,faComment,faGear,faUser,faImage,faFaceSmile,faPersonRunning,faXmark,faThumbsUp,faShare,faMagnifyingGlassPlus,faMagnifyingGlassMinus,faChevronLeft,faChevronRight,faCopy,faUsers,faMaximize,faUserPlus,faCommentDots,faCamera,faPen,faSuitcase,faHome,faLocationDot,faTrash,faEarthAmerica,faLock,faGraduationCap,faHeart,faPhone,faPenToSquare,faVideo,faEnvelopeCircleCheck,faCirclePlus,faEllipsis,faCakeCandles,faPlus ,faUserXmark,faArrowLeft,faUserTag,} from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faMessage,faBell,faMagnifyingGlass,faChevronDown,faArrowRightFromBracket,faComment,faGear,faUser,faImage,faFaceSmile,faPersonRunning,faXmark,faThumbsUp,faShare,faMagnifyingGlassPlus,faMagnifyingGlassMinus,faChevronLeft,faChevronRight,faCopy,faUsers,faMaximize,faUserPlus,faCommentDots,faCamera,faPen,faSuitcase,faHome,faLocationDot,faTrash,faEarthAmerica,faLock,faGraduationCap,faHeart,faPhone,faPenToSquare,faVideo,faEnvelopeCircleCheck,faCirclePlus,faEllipsis,faCakeCandles,faPlus,faUserXmark,faArrowLeft,faUserTag,)
const app = createApp(App)
app.use(router);
app.component('font-awesome-icon', FontAwesomeIcon);
app.component(messageModal);
app.use(Toast);
app.use(store);
app.mount('#app');
