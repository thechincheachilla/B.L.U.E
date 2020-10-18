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
            legislatorData: {},
            dataLoaded: false,
            legislators: {},
            legislatorNames: []
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
                // let count = 0;
                // let cont = true;
                // while (cont && count < 100) {
                //     try {
                //         //console.log(this.legislatorData["\"" + count + "\""])
                //         this.legislators.push(this.legislatorData["\"" + count + "\""]);
                //         //console.log("\"" + count + "\"")
                //     }
                //     catch(error) {
                //         // Dropped off the end, iteration over
                //         cont = false;
                //     }
                //     count++; 
                // }
        })
        .catch((error) => {
            console.error(error);
        });
        console.log("Finished", this.legislatorNames);
        console.log("Legislator Dict:", this.legislators);
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