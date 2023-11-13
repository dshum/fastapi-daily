import {createApp} from 'vue'
import './style.css'
import router from './router/index.js'
import App from './App.vue'

import {library} from '@fortawesome/fontawesome-svg-core'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import {faPenToSquare, faPencil, faBookmark as fasBookmark} from '@fortawesome/free-solid-svg-icons'
import {faFolderOpen, faBookmark} from '@fortawesome/free-regular-svg-icons'

library.add(faPenToSquare, faPencil, faFolderOpen, fasBookmark, faBookmark)

createApp(App)
  .component('font-awesome-icon', FontAwesomeIcon)
  .use(router)
  .mount('#app')
