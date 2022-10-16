<script setup>
import mapComp from '../components/mapElement.vue'
</script>

<template> <div class="p-5" style="width:100vw !important;">     <main class="main">
        <div class="container center">
            <h1 class="heading location">Time of Arrival</h1> 
            <input class="input desired-arrival" type="time" placeholder="e.g. 12:45pm" v-model="$store.state.formData.arrivalTime">             
        </div>
        <div class="container center">
            <h1 class="heading location">Minutes Needed To Get Ready</h1> 
            <input class="input desired-arrival" type="number" placeholder="30" v-model="$store.state.formData.delayTime">             
        </div>
    </main>

    <div class="justify-content-center d-flex m-4">
<div style="padding:10px;">
  <router-link to="/map">
<button type="button" class="btn btn-secondary btn-lg">Back</button></router-link>
</div>
<div style="padding:10px;">
<router-link to="/submit">
<button type="button" class="btn btn-light btn-lg" @click="">Continue</button>
</router-link>
</div>
</div> 
  </div>
</template>
<style scoped>

.clock {
    position: absolute;
    width: 300px;
    height: 300px;
    border: 20px solid #b06a26;
    border-radius: 50%;
    left: 42%;
    margin-top: 70px;
    top: 300;
    background: #fefbf2;
    box-shadow: inset 0px 0px 10px black;
}

.clock::before {
    position: absolute;
    content: '';
    height: 130px;
    width: 10px;
    background: black;
    top: 50%;
    left: calc(50% - 5px);
    border-radius: 5px;
    animation: spin 6s linear infinite;
    transform-origin: top;
}

.clock::after {
    position: absolute;
    content: '';
    height: 100px;
    width: 10px;
    background: black;
    top: 50%;
    left: calc(50% - 5px);
    border-radius: 5px;
    animation: spin 72s linear infinite;
    transform-origin: top;
    
}

@keyframes spin {
    0% {
        transform: rotate(-180deg)
    }
    100% {
        transform: rotate(180deg)
    }
}

body::before {
    content: '';
    position: absolute;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #b06a26;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    z-index: 1;

}

body::after {
    content: '';
    position: absolute;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: black;
    left: 50%;
    top: calc(50% - 145px);
    z-index: 2;
    transform: translateX(-50%);
    box-shadow: 140px 145px 0 0 black, -140px 145px 0 0 black, 0 280px 0 0 black;
}
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
}</style>
