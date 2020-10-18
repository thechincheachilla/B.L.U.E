<template>
    <div class="mt-4">
        <b-col>
        <b-input-group>
            <template v-slot:prepend>
                <b-dropdown :text="billType" variant="success">
                    <b-dropdown-item @click=updateBillSenate()>Senate Bill</b-dropdown-item>
                    <b-dropdown-item @click=updateBillHouse()>House Bill</b-dropdown-item>
                </b-dropdown>
            </template>
            <b-form-input></b-form-input>
            <template v-slot:append>
                <b-button @click=search() variant="info">Search</b-button>
            </template>
        </b-input-group>
        </b-col>
    </div>
</template>

<script>
export default {
    name: "LegislationSearch",
    data() {
        return{
            billType: "Bill Type:"
        }
    },
    methods: {
        search() {
            
        },
        updateBillHouse() {
            this.billType = "House Bill"
        },
        updateBillSenate() {
            this.billType = "Senate Bill"
        }
    }
}
</script>

<style>

</style>