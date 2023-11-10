<template>
  <div class="flight">
    <v-container>
      <flight-filter class="flight__filters" />
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
      <v-row class="mt-1">
        <v-col>
          <v-btn color="primary" block height="60px" @click="fileDialog = true">
            Import Changes
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <edit-flight-dialog
      v-model="dialog"
      :form-value="editForm"
      @updateShedule="onUpdateShedule"
    />

    <file-flight-dialog v-model="fileDialog" @updateShedule="onUpdateShedule" />
  </div>
</template>

<script>
import EditFlightDialog from '~/components/EditFlightDialog.vue'
import FileFlightDialog from '~/components/FileFlightDialog.vue'
export default {
  components: {
    EditFlightDialog,
    FileFlightDialog,
  },
  async asyncData({ store }) {
    await store.dispatch('flight/fetchAirportList')
    await store.dispatch('flight/fetchAirList', { ordering: '-data' })
  },

  data() {
    return {
      filters: {
        ordering: '-data',
        from: '',
        to: '',
        date: '',
        flightNumber: '',
      },
      headers: [
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
          text: 'Aircraft',
          value: 'aircraft.name',
        },
        {
          text: 'Economy price',
          value: 'economy_price',
        },
        {
          text: 'Business price',
          value: 'business_price',
        },
        {
          text: 'First class price',
          value: 'first_class_price',
        },
        {
          text: 'Actions',
          align: 'start',
          sortable: true,
          value: 'actions',
        },
      ],
      dialog: false,
      editForm: {
        to: '',
        from: '',
        economy_price: '',
        aircraft: '',
        time: '',
        date: '',
        id: null,
      },
      fileDialog: false,
    }
  },
  computed: {
    airList() {
      return this.$store.state.flight.AirList
    },
    airportList() {
      return this.$store.state.flight.airportList
    },
    airportListTo() {
      return this.airportList.filter((el) => el.id !== this.filters.from)
    },
  },
  methods: {
    canselAirList(id) {
      this.$store.dispatch('flight/canselAirList', id)
    },
    async onUpdateShedule() {
      await this.$store.dispatch('flight/fetchAirList', { ordering: '-data' })
    },
    editItem(item) {
      this.editForm = {
        to: item.route.arrival_airport.iata_code,
        from: item.route.departure_airport.iata_code,
        economy_price: item.economy_price,
        aircraft: item.aircraft.name,
        time: this.$dayjs(`2000-01-01 ${item.time}`).format('HH:mm'),
        date: item.date,
        id: item.id,
      }

      this.dialog = true
    },
    getClasses(item) {
      const classes = []

      if (!item.confirmed) {
        classes.push('red')
      }

      return classes.join(' ')
    },
  },
}
</script>

<style lang="scss" scoped>
.flight {
  margin-top: 40px;

  &__filters {
    margin-bottom: 20px;
  }

  &:deep() {
    .red {
      background: #ff6a55 !important;
      color: #fff !important;
      &:hover {
        background: #ff6a55 !important;
      }
    }
  }
}
</style>
