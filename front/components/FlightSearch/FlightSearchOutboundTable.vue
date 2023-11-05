<template lang="">
  <div class="tableOutbound">
    <v-row>
        <v-col cols="6" align-self="center">
          {{!isReturn ? "Outbound" : "Return"}} flight details:
        </v-col>
        <v-col cols="6">
          <v-checkbox v-model="item" label="Display three days before and after"/>
        </v-col>
      </v-row>
      <v-data-table
        :headers="headers"
        :items="airList"
        :item-class="getClasses"
        :options="{
          itemsPerPage: 5,
        }"
        class="tableOutbound"
        @click:row="$emit('click:row', $event)"
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
import { getPriceKey } from '@/utils/getPriceKey'
export default {
  props: {
    airList: {
      type: Array,
      default: () => [],
    },
    selected: {
      type: Object,
      default: null,
    },
    isReturn: Boolean,
    value: {
      type: Boolean,
      default: false,
    }
  },
  data() {
    return {
    }
  },
  computed: {
    item: {
      get() {
        return this.value
      },
      set(v) {
        this.$emit('input', v)
      }
    },
    cabinType() {
      return this.$store.state.flightSearch?.filters?.cabinType || ''
    },  
    headers() {
      return[
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
          value: getPriceKey(this.cabinType),
        },
        {
          text: 'Number of stops',
          value: `stops`,
        },
      ]
    },
  },
  async mounted() {
    await this.$store.dispatch('countries/fetchCountries')
  },
  methods: {
    getClasses(item) {
      const classes = []
      
      if (item.id === this.selected?.id) {
        classes.push('green')
      }

      return classes.join(' ')
    }
  },
}
</script>
<style lang="scss">
.tableOutbound {
  &:deep {
    .green {
      background: #4adb3a !important;
      color: #fff !important;
      &:hover {
        background: #4adb3a !important;
      }
    }
  }
}
</style>