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
        <v-col>
          <m-select
            v-model="filters.ordering"
            :items="sortingItems"
            label="Sort By"
            item-text="name"
            :clearable="false"
            item-value="value"
          />
        </v-col>
        <v-col
          cols="4"
        >
          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :return-value.sync="filters.date"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="filters.date"
                outlined
                readonly
                clearable
                label="Outbound"
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-date-picker
              v-model="filters.date"
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn
                text
                color="primary"
                @click="menu = false"
              >
                Cancel
              </v-btn>
              <v-btn
                text
                color="primary"
                @click="$refs.menu.save(filters.date)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>
        </v-col>
        <v-col
          cols="4"
        >
          <v-text-field
            v-model="filters.flightNumber"
            outlined
            label="Flight Number"
            clearable
          />
        </v-col>
        <v-col
          cols="4"
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
import MSelect from './MSelect.vue'
export default {
  components: { MSelect },
  data(){
    return{
      menu: false,
      filters: {
        ordering: '-date',
        from: '',
        to: '',
        date: '',
        flightNumber: '',
      },
      sortingItems: [
        {
          name: 'date up',
          value: 'date',
        },
        {
          name: 'date down',
          value: '-date',
        },
        {
          name: 'time up',
          value: 'time',
        },
        {
          name: 'time down',
          value: '-time',
        },
        {
          name: 'economy price up',
          value: 'economy_price',
        },
        {
          name: 'economy price down',
          value: '-economy_price',
        },
        {
          name: 'confirmed up',
          value: 'confirmed',
        },
        {
          name: 'confirmed down',
          value: '-confirmed',
        },
      ]
    }
  },
  computed: {
    airportList() {
      return this.$store.state.flight.airportList
    },
    airportListTo() {
      return this.airportList.filter(el => el.id !== this.filters.from)
    },
  },
  methods: {
    accept() {
      this.$store.commit('flight/setFilters', this.filters)

      this.$store.dispatch('flight/fetchAirList')
    }
  }
}
</script>

<style>

</style>