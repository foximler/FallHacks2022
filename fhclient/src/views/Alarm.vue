<script setup>
import mapComp from '../components/mapElement.vue'
</script>
<template>
  <div>
    <div class="continue justify-content-center d-flex m-4">
<h1> Rise And Shine, Time To Leave</h1>
<audio autoplay loop>
        <source src="audio/alarm.wav" type="audio/wav" />
    </audio>
</div>
<mapComp />
<router-link to="/" class="m-5">
  <div class="continue justify-content-center d-flex m-4">
<button type="button" class="btn btn-danger p-5"><h2>Mute</h2></button>
</div>
</router-link>
</div>
</template>
