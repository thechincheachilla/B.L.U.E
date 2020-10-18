<template>
    <div class="mt-4">
        <b-col>
        <b-input-group v-if="dataLoaded">
            <template v-slot:prepend>
                <b-form-select placeholder="Select:" v-model="selected" :options="searchType"></b-form-select>
            </template>
            <b-form-input v-model="input"></b-form-input>
            <template v-slot:append>
                <b-button v-b-modal.info @click=search() variant="info">Search</b-button>
            </template>
        </b-input-group>
        <b-spinner v-else>Loading...</b-spinner>
        </b-col>
        <b-modal id="info" :title="currentName">
            <div>
                <b-tabs content-class="mt-3" align="center">
                    <b-tab title="Info" active>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">Position:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['position']}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">Party:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['party']}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">State:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['state']}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">District:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['district']}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">Address:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['address']}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">Phone Number:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['phone']}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">Facebook:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['facebook']}}</b-col>
                        </b-row>
                        <b-row>
                            <b-col style="text-align:right; font-weight:bold; color:#42b983">Twitter:</b-col>
                            <b-col style="text-align:left; color:#2c3e50">{{currentLegislator['twitter']}}</b-col>
                        </b-row>
                    </b-tab>
                    <b-tab title="Sponsorships">
                        
                    </b-tab>
                </b-tabs>
            </div>
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
            input: "", 
            searchType: [
                {value: 'name', text: 'Full Name'},
            ],
            legislatorData: {},
            dataLoaded: false,
            legislatorNames: [],
            legislators: {}, 
            showModal: false,
            currentLegislator: {},
            currentName: "Legislator Not Found!"
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
            console.log(this.input, this.selected)
            try {
                this.currentLegislator = this.legislators[this.input];
                console.log(this.currentLegislator);
                this.currentName = this.currentLegislator['full_name'];
                if(this.currentLegislator['senate_class'] != null) {
                    this.currentLegislator['position'] = "Senator";
                    this.currentLegislator['district'] = "Not Applicable";
                } 
                else {
                    this.currentLegislator['position'] = "Representative";
                }
            }
            catch (error) {
                this.currentLegislator = {};
                this.currentName = "Legislator Not Found!";
                console.log(error)
            }
            console.log(this.currentLegislator)
        }
    }
}
</script>

<style>

</style>