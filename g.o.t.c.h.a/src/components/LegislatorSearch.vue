<template>
    <div class="mt-4">
        <b-col>
        <b-input-group>
            <template v-slot:prepend>
                <b-dropdown :text="legType" variant="success">
                    <b-dropdown-item @click=updateLegHouse()>Representative</b-dropdown-item>
                    <b-dropdown-item @click=updateLegSenate()>Senator</b-dropdown-item>
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
import axios from 'axios'; 

export default {
    name: "LegislatorSearch",
    data() {
        return{
            legType: "Legislator Type:",
            legislatorData: {}
        }
    },
    created: {
        // getLegislators() {
        //     const path = 'http://localHost:5000/getLegislators';
        //     axios.get(path)
        //         .then((res) => {
        //             this.legislatorData = res.data;
        //             console.log(this.legislatorData);
        //     })
        //     .catch((error) => {
        //         console.error(error);
        //     });
        // },
    },
    methods: {
        updateLegHouse() {
            this.legType = "Representative";
        },
        updateLegSenate() {
            this.legType = "Senator";
        }
    }
}
</script>

<style>

</style>