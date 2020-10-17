<template>
  <div id="app">
    <img alt="GOTCHA_Logo" src="../assets/GOTCHA_Logo.png" style="width:37%; height:37%">
    <HelloWorld msg="Welcome to Project g.o.t.c.h.a"/>
  </div>
</template>

<script>
import BillsPage from '../views/Bills.vue'
import LegislatorsPage from '../views/Legislators.vue'

export default {
  name: 'HomePage',
  components: {
    BillsPage,
    LegislatorsPage
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
