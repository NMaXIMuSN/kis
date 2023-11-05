<template>
  <v-card>
    <v-card-actions>
      <v-row>
        <v-col
          cols="4"
        >
          <m-select
            v-model="filters.from"
            :items="airportList"
            clearable
            label="From"
            item-text="name"
            item-value="iata_code"
          />
        </v-col>
        <v-col
          cols="4"
        >
          <m-select
            v-model="filters.to"
            :items="airportListTo"
            label="To"
            clearable
            item-text="name"
            item-value="iata_code"
          />
        </v-col>
        <v-col
          cols="4"
        >
          <m-select
            v-model="filters.cabinType"
            :items="cabinTypes"
            label="Cabin type"
            item-text="name"
            item-value="name"
          />
        </v-col>
        <v-col
          cols="4"
        >
          <v-radio-group v-model="filters.isReturn" row>
            <v-radio
              :label="`One Way`"
              :value="false"
            />
            <v-radio
              :label="`Return`"
              :value="true"
            />
          </v-radio-group>
        </v-col>
        <v-col
          cols="4"
        >
          <m-date-picker v-model="filters.date" label="Outbound" />
        </v-col>
        <v-col
          cols="4"
        >
          <m-date-picker v-model="filters.return" label="Return" />
        </v-col>
        <v-col
          cols="12"
        >
          <v-btn
            color="primary"
            block
            style="height: 56px"
            @click="accept"
          >
            Accept
          </v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>
<script>
import MDatePicker from '../MDatePicker.vue'
export default {
  components: { MDatePicker },
  props: {
    value: {
      type: Object,
      default: null,
    }
  },
  data() {
    return {
    filters: {...this.value} || {
      to: '',
      from: '',
      date: '',
      return: '',
      cabinType: '1',
      isReturn: false,
    },
    typeTicket: 'oneWay',
    cabinTypes: [
      {
        name: 'Economy',
        value: '1',
      },
      {
        name: 'Business',
        value: '2',
      },
      {
        name: 'Class',
        value: '3',
      },
    ],
    }
  },
  computed: {
    airportList() {
      return this.$store.state.flight.airportList
    },
    airportListTo() {
      return this.airportList.filter(el => el.iata_code !== this.filters.from)
    },
  },
  watch: {
    value(val) {
      this.filters = {...val}
    },
  },
  methods: {
    accept() {
        this.$emit('input', this.filters)
    }
  }
}
</script>
<style lang="">
  
</style>