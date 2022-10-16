
<template>
<div class="main w-100 p-3" style="width:100vw !important;">
        <div class="container center">
            <h1 class="location current">Your Location</h1>
            <input class="input current" type="text" placeholder="e.g. 15250 Pender St." v-model=curr>
            <div  v-if="g_suggestion_curr != null" @click="setToRec('curr')"><a style="text-align: center;"><h4>Suggested: <u>{{g_suggestion_curr.name? g_suggestion_curr.name : g_suggestion_curr.address.formattedAddress}}</u></h4></a></div>
            <h1 class="location destination">Destination</h1>
            <input class="input destination" type="text" placeholder="e.g. Rogers Arena" v-model=dest>
            <div  v-if="g_suggestion_dest != null" @click="setToRec('dest')"><a style="text-align: center;"><h4>Suggested: <u>{{g_suggestion_dest.name? g_suggestion_dest.name : g_suggestion_dest.address.formattedAddress}}</u></h4></a></div>
        </div>
    </div>
    <div class="buttons container row">
        <router-link to="/map"> <div class="continue justify-content-center d-flex m-4">
            <button class="btn btn btn-light btn-lg ">Continue</button> 
      </div>
    </router-link>
    </div> 
</template>
<script>
import { mapState } from 'vuex'
import { io } from "socket.io-client";
const socket = io("localhost:3000");
export default {
  data () {
    return {
      dest:'Edmonton International Airport',
      curr:'University of Calgary',
      transportMode: null,
      arrivalTime:null,
     formattedData:{
      dest:null,
     },
     returnData:{
      travelTime:null,
      alarmTime:null,
     },
     g_suggestion_curr: null,
     g_suggestion_dest: null,
    }
  },
  methods:{
    setToRec(address){
      switch(address) {
        case 'curr':
          this.curr = this.g_suggestion_curr.address.formattedAddress
          break;
        case 'dest':
          this.dest = this.g_suggestion_dest.address.formattedAddress
          break;
        }
    }
  },
  beforeMount(){
     socket.emit("cancelAlarm",{});
  },
  watch: {
    dest:{
      deep:true,
      immediate:true,
  async handler(newFormData) {
      var requestOptions = {
    method: "get",
    mode: "cors",
          cache: "default",
    headers: {"Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*","Access-Control-Allow-Headers":"Origin, X-Requested-With:Content-Type, Accept" },
  }
  this.g_suggestion_dest = null
  this.$store.state.formData.dest = newFormData;
  let res = await fetch(`http://dev.virtualearth.net/REST/v1/Autosuggest?query=${this.dest},1&userLocation=49.277283,%20-122.916498,5&includeEntityTypes=Address,Place&countryFilter=CA&key=`,  {mode: 'cors'})
    const data = await res.json();
    if (data.resourceSets[0]['resources'][0]['value'].length > 0){
       this.g_suggestion_dest = data.resourceSets[0]['resources'][0]['value'][0]
    }
   
} },
curr:{
      deep:true,
      immediate:true,
      async handler(newFormData){
  this.g_suggestion_curr = null;
  this.$store.state.formData.currLoc = newFormData;
  let res = await fetch(`http://dev.virtualearth.net/REST/v1/Autosuggest?query=${this.curr},1&userLocation=49.277283,%20-122.916498,5&includeEntityTypes=Address,Place&countryFilter=CA&key=`,  {mode: 'cors'})
    const data = await res.json();

    if (data.resourceSets[0]['resources'][0]['value'].length > 0){
       this.g_suggestion_curr = data.resourceSets[0]['resources'][0]['value'][0]
    }
},
  },
}
}
</script>
<style scoped>
*, *::before, *::after {
    margin: 0;
    box-sizing: border-box;
}
:root {
    --primary-color-light: #F1E9E9;
    --primary-color-dark: #555555;
    --ff-primary: 'Arial', sans-serif;
}
body{
    background-color: var(--primary-color-dark);
    color: white;
}
p, h1, h2 {
    font-family: var(--ff-primary);
    color: white;
    text-align: center;
}
h1{    
    text-transform: uppercase;
}
img {
    max-width: 100%;
}
.nav {
    justify-content: center;
    height: 10vh;
    width: 100vw;
    background-color: var(--primary-color-light);
}

.center {
    margin: 0 auto;
}

.location{
    margin-top: 2ch;
}
.container {
    display: flex;    
    flex-direction: column;
    max-width: 60%;
    margin: 0 auto;
}
.row {
    display: flex;
    flex-direction: row;
}
.input {
    margin-top: 1rem;
    border: none;
    padding: .75rem;
    border-radius: 12px;
}

.btn{

    padding: .7rem 1.2rem;
    width: 1;
    border: none;
    border-radius: 5px;
}

</style>