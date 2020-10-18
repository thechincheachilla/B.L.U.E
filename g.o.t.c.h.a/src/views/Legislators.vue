<template>
    <div id="legislators">
        <h1 style="font-weight:bold">Legislator Lookup</h1>
        <LegislatorSearch />
    </div>
</template>

<script>
import LegislatorSearch from "../components/LegislatorSearch.vue";
export default {
    name: "Legislator",
    components: {
        LegislatorSearch
    }
}
</script>

<style>
#legislators {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>