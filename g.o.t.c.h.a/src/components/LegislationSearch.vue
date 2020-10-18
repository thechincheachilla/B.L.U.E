<template>
    <div class="mt-4">
        <b-col>
            <div v-if="dataLoaded">
                <b-form-select
                    v-model="selected"
                    text="Legislation Selection"
                    block
                    class="m-2"
                    menu-class="w-100"
                    size="sm" 
                    split
                    :options="billDropdownItems"
                >
                </b-form-select>
                <b-button v-b-modal.info @click=search() variant="info" style="max-height:80%; margin-left: 30px">Search</b-button>
            </div>
            <div v-else class="text-center">
                <b-spinner variant="primary" label="Text Centered"></b-spinner>
            </div>
        </b-col>
        <b-modal id="info" :title="currentBill[0]">
            <b-row>
                <b-col style="text-align:left; font-weight:bold; color:#42b983">Full Name:</b-col>
            </b-row>
            <b-row>
                <b-col style="text-align:left; color:#2c3e50">{{currentBill[1]}}</b-col>
            </b-row>
            <b-row>
                <b-col style="text-align:left; font-weight:bold; color:#42b983" class="mt-3">Summary:</b-col>
            </b-row>
            <b-row>
                <b-col style="text-align:left; color:#2c3e50">{{currentBill[2]}}</b-col>
            </b-row>
        </b-modal>
    </div>
</template>

<script>
import axios from 'axios'; 

export default {
    name: "LegislationSearch",
    data() {
        return{
            selected: null,
            billDropdownItems: [],
            legislationData: {},
            legislation: {},
            currentBill: {},
            dataLoaded: false,
            showModal: false,
        }
    },
    created() {
        let path = 'http://localHost:5000/getBillInfos';
        axios.get(path)
            .then((res) => {
                this.legislationData = res.data;
                this.dataLoaded = true;
                //console.log(this.legislationData);
                //console.log(typeof(this.legislationData));
                Object.keys(this.legislationData).forEach(id => {
                    //console.log(this.legislationData[id][0])
                    let currBill = this.legislationData[id][0]
                    if (currBill.length >= 110) {
                        currBill = currBill.substr(0, 107);
                        currBill = currBill.trim();
                        currBill = currBill.concat("...");
                    }
                    this.billDropdownItems.push(
                        {value: this.legislationData[id][0], text: currBill});
                    this.legislation[currBill] = this.legislationData[id]
                    //console.log(this.legislation[this.legislationData[id][0]])
                });
                //console.log("Finished", this.billDropdownItems);
                //console.log("Legislator Dict:", this.legislation);
        })
        .catch((error) => {
            console.error(error);
            alert("Error loading data, please try again")
        });
    },
    methods: {
        search() {
            this.showModal = true;
            console.log(this.legislation)
            console.log(this.selected)
            try {
                this.currentBill = this.legislation[this.selected];
                console.log(this.currentBill)
            }
            catch (error) {
                this.currentBill = {};
                this.currentBill[0] = "Bill Not Found!";
                console.log(error)
            }
        },
    }
}
</script>

<style>

</style>