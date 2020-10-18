<template>
    <div class="nav">
        <b-navbar>
            <b-navbar-nav class="pages">
                <b-nav-item href="#">home</b-nav-item>
                <b-nav-item href="#">bills</b-nav-item>
                <b-nav-item href="#">house</b-nav-item>
                <b-nav-item href="#">senate</b-nav-item>
            </b-navbar-nav>
            <b-navbar-nav class="ml-auto">
                <b-nav-form>
                    <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
                    <b-button size="sm" class="my-2 my-sm-0" type="submit">Search</b-button>
                </b-nav-form>
            <b-nav-item-dropdown right>
            </b-navbar-nav>
        </b-navbar>
    </div>
</template>

<script>
export default {
  name: 'NavBar',
  componenets: {
      
  }
}
</script>

<style>
.nav {
    background-color:turquoise;
    display: flex;
    justify-content: flex-start;
}

</style>
