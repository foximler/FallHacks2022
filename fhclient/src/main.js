import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

import './assets/main.css'

const app = createApp(App)
import { createStore } from 'vuex'

// Create a new store instance.
const store = createStore({
  state () {
    return {
     formData: {
      dest:null,
      currLoc:null,
      transportMode: null,
      arrivalTime:null,
      delayTime:null,
     },
    }
  },
})

// Install the store instance as a plugin
app.use(store)

app.use(router)

app.mount('#app')
