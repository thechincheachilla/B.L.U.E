<template>
    <div id="legislation">
        <h1 style="font-weight:bold">Legislation Lookup</h1>
        <LegislationSearch />
    </div>
</template>

<script>
import LegislationSearch from "../components/LegislationSearch.vue";
export default {
    name: "Legislation",
    components: {
        LegislationSearch
    }
}
</script>

<style>
#legislation {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>