<template>
    <div class="mt-4">
        <b-col>
        <b-input-group>
            <template v-slot:prepend>
                <b-form-select placeholder="Select:" v-model="selected" :options="searchType"></b-form-select>
            </template>
            <b-form-input></b-form-input>
            <template v-slot:append>
                <b-button @click=search() variant="info">Search</b-button>
            </template>
        </b-input-group>
        </b-col>
        <b-modal v-if="showModal">
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios'; 

export default {
    name: "LegislatorSearch",
    data() {
        return{
            selected: null, 
            searchType: [
                {value: 'name', text: 'Full Name'},
            ],
            legislatorData: {},
            dataLoaded: false,
            legislatorNames: [],
            legislators: {}, 
            showModal: false
        }
    },
    created() {
        const path = 'http://localHost:5000/getLegislators';
        axios.get(path)
            .then((res) => {
                this.legislatorData = res.data;
                this.dataLoaded = true;
                //console.log(this.legislatorData);
                //console.log(typeof(this.legislatorData));
                //console.log(this.legislatorData["0"])
                Object.keys(this.legislatorData).forEach(id => {
                    this.legislatorNames.push(this.legislatorData[id]['full_name']);
                    this.legislators[this.legislatorData[id]['full_name']] = this.legislatorData[id]
                })
        })
        .catch((error) => {
            console.error(error);
        });
        //console.log("Finished", this.legislatorNames);
        //console.log("Legislator Dict:", this.legislators);
    },
    methods: {
        search() {
            this.showModal = true; 
        }
    }
}
</script>

<style>

</style>