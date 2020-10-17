<template>
    <div>
        <b-navbar>
        <b-navbar-brand href="#">Home</b-navbar-brand>
        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-navbar-nav>
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
}
</script>

<style>

</style>