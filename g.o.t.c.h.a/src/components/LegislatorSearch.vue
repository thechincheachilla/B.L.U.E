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
        <div v-else class="text-center">
            <b-spinner variant="primary" label="Text Centered"></b-spinner>
        </div>
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
                        <div v-if="modalDataLoaded">
                            <h4 style="text-align:center; font-weight:bold; color:#42b983">Sponsorships:</h4>
                            <h6 style="text-align:center" v-for="bill in currentLegislator['bills']" :key="bill">{{ bill }}</h6>
                        </div>
                        <div v-else class="text-center">
                            <b-spinner variant="primary" label="Text Centered"></b-spinner>
                        </div>
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
            legToBills: {}, 
            dataLoaded: false,
            modalDataLoaded: false, 
            legislatorNames: [],
            legislators: {}, 
            showModal: false,
            currentLegislator: {},
            currentName: "Legislator Not Found!"
        }
    },
    created() {
        let path = 'http://localHost:5000/getLegislators';
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
            alert("Error loading data, please try again")
        });
        //console.log("Finished", this.legislatorNames);
        //console.log("Legislator Dict:", this.legislators);
    },
    methods: {
        search() {
            this.showModal = true; 
            try {
                this.currentLegislator = this.legislators[this.input];
                //console.log(this.currentLegislator);
                this.currentName = this.currentLegislator['full_name'];
                if(this.currentLegislator['senate_class'] != null) {
                    this.currentLegislator['position'] = "Senator";
                    this.currentLegislator['district'] = "Not Applicable";
                } 
                else {
                    this.currentLegislator['position'] = "Representative";
                }
                let path = 'http://localHost:5000/getBills';
                axios.get(path)
                    .then((res) => {
                    this.legToBills = res.data;
                    this.modalDataLoaded = true;
                    //console.log(this.legToBills)
                    //console.log(this.legislatorData);
                    //console.log(typeof(this.legislatorData));
                    //console.log(this.legislatorData["0"])
                    this.currentLegislator['bills'] = this.legToBills[this.currentLegislator['full_name']];
                    //console.log(this.legToBills[this.currentLegislator['full_name']]);
                    //console.log(this.currentLegislator['bills']);
                    if (this.currentLegislator['bills'] == undefined) {
                        this.currentLegislator['bills'] = ["This legislator has not worked on any of the last 100 bills."]
                    }
                })
                .catch((error) => {
                    console.error(error);
                    alert("Error loading data, please try again")
                });
            }
            catch (error) {
                this.currentLegislator = {};
                this.currentName = "Legislator Not Found!";
                console.log(error)
            }
        }
    }
}
</script>

<style>

</style>