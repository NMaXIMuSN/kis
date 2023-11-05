<template>
  <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
    <v-card>
      <v-toolbar dark color="primary">
        <v-toolbar-title>Booking confirmation</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon dark @click="dialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
      <v-row>
        <v-col cols="12">
          <v-card v-if="outbound">
            <v-card-title>
              Outbound flight details
            </v-card-title>
            <v-card-actions style="padding: 20px;">
              <flight-details
:to="outbound?.route?.arrival_airport?.iata_code"
                :from="outbound?.route?.departure_airport?.iata_code" :cabin-type="cabinType" :date="outbound?.date"
                :flight-number="outbound?.flight_number" />
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="12">
          <v-card v-if="returnFlight">
            <v-card-title>
              Return flight details
            </v-card-title>
            <v-card-actions style="padding: 20px;">
              <flight-details
:to="returnFlight?.route?.arrival_airport?.iata_code"
                :from="returnFlight?.route?.departure_airport?.iata_code" :cabin-type="cabinType"
                :date="returnFlight?.date" :flight-number="returnFlight?.flight_number" />
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col cols="12">
          <passenger-details @addPassenger="onAddPassenger" />
        </v-col>
        <v-col cols="12">
          <passenger-table :items="passengers" @deletePassenger="onDeletePassenger" />
        </v-col>
        <v-col cols="12">
          <flight-search-finally-confirmed :disabled="!passengers.length" :amount="totalAmount" @accept="onSave">
              Confirm Booking
          </flight-search-finally-confirmed>
        </v-col>
      </v-row>
    </v-card>
  </v-dialog>
</template>

<script>
import FlightDetails from './FlightDetails.vue'
import FlightSearchFinallyConfirmed from './FlightSearchFinallyConfirmed.vue'
import PassengerDetails from './PassengerDetails.vue'
import PassengerTable from './PassengerTable.vue'
import { getPriceKey } from '~/utils/getPriceKey'
export default {
  components: { FlightDetails, PassengerDetails, PassengerTable, FlightSearchFinallyConfirmed },
  props: {
    value: Boolean,
    outbound: {
      type: Object,
      default: null,
    },
    returnFlight: {
      type: Object,
      default: null,
    },
    cabinType: {
      type: String,
      default: 'null',
    }
  },
  data() {
    return {
      passengers: [],
    }
  },
  computed: {
    dialog: {
      get() {
        return this.value
      },
      set(value) {
        this.$emit('input', value)
      }
    },
    totalAmount() {
      const tickets = [this.outbound]

      if (this.returnFlight) {
        tickets.push(this.returnFlight)
      }


      return tickets.reduce((acc, schedule) => {
        return acc + schedule[getPriceKey(this.cabinType)]
      }, 0) * this.passengers.length
    },
  },
  methods: {
    onAddPassenger(passenger) {
      this.passengers.push({...passenger, user: this.$auth.user.id, booking_reference: 1, confirmed: 1})
    },
    onDeletePassenger(index) {
      this.passengers = this.passengers.filter((el, _index) => _index !== index)
    },
    async onSave() {
      try {
        const data = this.passengers.map((el) => ({
          first_name: el.firstName,
          last_name: el.lastName,
          passport_number: el.passportNumber,
          user: el.user,
          schedule: this.outbound.id,
          cabin_type: 1,
          phone: el.phone,
          passport_country: el.passportCountry.id,
          booking_reference: el.booking_reference,
          confirmed: el.confirmed
        }))

        if (this.returnFlight) {
          data.push(...this.passengers.map((el) => ({
          first_name: el.firstName,
          last_name: el.lastName,
          passport_number: el.passportNumber,
          user: el.user,
          schedule: this.returnFlight.id,
          cabin_type: 1,
          phone: el.phone,
          passport_country: el.passportCountry.id,
          booking_reference: el.booking_reference,
          confirmed: el.confirmed
        })))
        }

        await this.$axios.post('/tickets/add', data)
        this.dialog = false
      } catch (error) {
        console.log(error)
      }
    }
  }
}
</script>

<style></style>