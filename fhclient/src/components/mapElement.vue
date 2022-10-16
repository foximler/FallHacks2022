<template>
    <img alt="Unable To Resolve Your Address" class="rounded mx-auto d-block" :src=getMapUrl v-if="getMapUrl !== null" style="max-height: calc(50vh); width: auto;"/>
</template>

<script>
import { mapState } from 'vuex'
export default {
  computed: {
    // a computed getter
    getMapUrl() {
      if (this.$store.state.formData.dest !== null && this.$store.state.formData.currLoc !== null){
        return `https://dev.virtualearth.net/REST/v1/Imagery/Map/CanvasLight/Routes?wp.0=${this.$store.state.formData.currLoc};66;A&wp.1=${this.$store.state.formData.dest};66;2&key=&mapSize=1200,900`
      }
      else {
        return null
      }
    }
  }
}
</script>