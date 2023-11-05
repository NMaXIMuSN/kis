<template lang="">
  <div>
    <v-row>
        <v-col cols="6" align-self="center">
          Return flight details:
        </v-col>
        <v-col cols="6">
          <v-checkbox label="Display three days before and after"/>
        </v-col>
      </v-row>
      <v-data-table
        :headers="headers"
        :items="airList"
        :item-class="getClasses"
      >
       <template v-slot:item.actions="{ item }">
          <v-icon
            :color="!item.confirmed ? 'white' : 'black'"
            small
            class="mr-2"
            @click="editItem(item)"
          >
            mdi-pencil
          </v-icon>
          <v-icon
            :color="!item.confirmed ? 'white' : 'black'"
            small
            @click="canselAirList(item.id)"
          >
            mdi-close-box-outline
          </v-icon>
        </template>
      </v-data-table>
  </div>
</template>
<script>
export default {
  props: {
    airList: {
      type: Array,
      default: () => [],
    }
  },
  computed: {
    headers: () => ([
        {
          text: 'Date',
          value: 'date',
        },
        {
          text: 'Time',
          value: 'time',
        },
        {
          text: 'From',
          value: 'route.departure_airport.iata_code',
        },
        {
          text: 'To',
          value: 'route.arrival_airport.iata_code',
        },
        {
          text: 'Flight number',
          value: 'flight_number',
        },
        {
          text: 'Price',
          value: `_price`,
        },
        {
          text: 'Number of stops',
          value: `stops`,
        },
        // {
        //   text: 'First class price',
        //   value: 'first_class_price',
        // },
      ]),
  },
}
</script>
<style lang="">
  
</style>