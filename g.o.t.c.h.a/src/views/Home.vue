<template>
  <div>
    <div id="home">
      <h1 class="mb-4" style="font-weight:bold; font-size:50px">Project</h1>
      <img alt="GOTCHA_Logo" src="../assets/GOTCHA_Logo.png" style="width:35%; height:35%" />
      <h1 class="mt-4 mb-4" style="font-weight:bold;">No time to read the latest bills? We gotcha!</h1>
      <b-container>
        <div class="mt-3">
          <b-card-group deck class="mb-3">
            <b-card 
              header="Lookup Legislators" 
              class="text-center"
            >
              <b-card-text>
                What have our legislators been up to? How does their voting record look? How can we contact them?
                Use this search to find out!
              </b-card-text>
              <b-button variant="info" to="/legislators">Search</b-button>
            </b-card>
            <b-card 
              header="Lookup Legislation" 
              class="text-center"
            >
              <b-card-text>
                Want to find out what Congress has been up to? What bills are currently on the floor?
                Click here to find out! 
              </b-card-text>
              <b-button variant="info" to="/legislation">Search</b-button>
            </b-card>

          </b-card-group>
        </div>
      </b-container>
    </div>
  </div>
</template>

<script>

export default {
  name: "Home",
  data() {
    return {
    }
  },
  methods: {
  }
}
</script>

<style>
#home {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
