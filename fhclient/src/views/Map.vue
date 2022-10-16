<script setup>
import mapComp from '../components/mapElement.vue'
</script>

<template> <div class="p-5"> <h1 style=" text-align: center; color:white;
padding-bottom: 0.2em">A Quick Look At Your Route</h1> <h4 style="
text-align: center; padding-bottom: 1em">Does this look right?</h4>
<mapComp />
<div class="justify-content-center d-flex m-4">
<div style="padding:10px;">
  <router-link to="/">
<button type="button" class="btn btn-secondary btn-lg">Back</button></router-link>
</div>
<div style="padding:10px;">
<router-link to="/arrivalTime">
<button type="button" class="btn btn-light btn-lg" @click="">Continue</button>
</router-link>
</div>
</div> </div> </template>
