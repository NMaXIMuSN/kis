<template>
  <div class="amenities">
    <v-container>
      <div class="amenities_booking">
        <v-text-field v-model="bookingReference_" counter="6" outlined label="Booking reference"/>
        <v-btn height="56" width="100" color="primary" @click="onLoadTickets">
          OK
        </v-btn>
      </div>
      <div v-if="ticketsList.length" class="amenities_select">
        <m-select v-model="selectTicket" label="Choose your flight" :items="ticketsListValidate" @input="onSelectTickets"/>
      </div>
      <div v-if="selectTicket">
        <amenities-piple-info :select-ticket="selectTicket" />
        <v-card class="mt-10">
          <v-card-title>
            Amenities
          </v-card-title>
          <v-card-text>
            <v-row>
              <v-col v-for="(item) in amenitiesList" :key="item.id" cols="6">
                <v-checkbox v-if="item.price" v-model="selectAmenitiesIds" :value="item.id" input-value="true" :disabled="!item.price" :label="`${item.service} (${item.price ? item.price : 'Free'})`"/>
                <v-checkbox v-else input-value="true" :disabled="!item.price" :label="`${item.service} (${item.price ? item.price : 'Free'})`"/>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
        <amenities-cost class="mt-10" :price="price" :purchase-amenities-cost="purchaseAmenitiesCost" />
        <v-btn :disabled="price === 0" class="mt-10" height="56" block color="primary" @click="onSave">Save And Confirm</v-btn>
      </div>
    </v-container>
  </div>
</template>

<script>
import AmenitiesCost from '../../components/Amenities/AmenitiesCost.vue';
import AmenitiesPipleInfo from '../../components/Amenities/AmenitiesPipleInfo.vue';
import MSelect from '../../components/MSelect.vue';
export default {
  comments: {
    MSelect,
  },
  components: { AmenitiesCost, AmenitiesPipleInfo },
  data() {
    return {
      bookingReference: 'CKIRMA',
      ticketsList: [],
      selectTicket: null,
      amenitiesList: [],
      selectAmenitiesIds: [],
      purchaseAmenitiesCost: 0,
    }
  },
  computed: {
    bookingReference_: {
      get() {
        return this.bookingReference;
      },
      set (v) {
        this.bookingReference = v.toUpperCase();
      }
    },
    selectAmenities() {
      return this.selectAmenitiesIds.map(el => this.amenitiesList.find((_el) => _el.id === el))
    },
    price() {
      return this.selectAmenities.reduce((sum, el) => sum + el.price, 0) - this.purchaseAmenitiesCost
    },
    ticketsListValidate() {
      return this.ticketsList.map(el => ({
        text: `${el.first_name} ${el.last_name}, ${el.schedule?.id}, ${el.schedule?.route.departure_airport.iata_code}-${el.schedule?.route.arrival_airport.iata_code}, ${el.schedule?.date}, ${el.schedule.time}`,
        value: el,
      }))
    }
  },
  async mounted() {
    try {
      const { data } = await this.$axios.get('/tickets/amenities')
      this.amenitiesList = data
    } catch (err) {
      console.error(err)
    }
  },
  methods: {
    async onSave() {
      try {
        const { data } = await this.$axios.post('/tickets/amenities/' + this.selectTicket.id, this.selectAmenitiesIds)
        this.selectAmenitiesIds = data.map(el => el.amenity)
        this.purchaseAmenitiesCost = data.reduce((sum, el) => sum + el.price, 0)
      } catch (error) {
        console.error(error)
      }
    },
    async onSelectTickets(v) {
      if (!v) {
        this.selectAmenitiesIds = []
        this.purchaseAmenitiesCost = 0

        return
      }

      const { data } = await this.$axios.get('/tickets/amenities/' + v.id)
      this.selectAmenitiesIds = data.map(el => el.amenity)
      this.purchaseAmenitiesCost = data.reduce((sum, el) => sum + el.price, 0)
    },
    async onLoadTickets() {
      try {  
        const { data } = await this.$axios.get(`/tickets/list?booking_reference=${this.bookingReference}`)
        
        this.ticketsList = data.filter((el) => {
          return true

          // const date = new Date(`${el.schedule.date} ${el.schedule.time}`)
          // date.setDate(date.getDate() - 1)
          // return Date.now() < date.getTime()
        })
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>

<style lang="scss">
.amenities {
  margin-top: 40px;
  &_booking {
    display: flex;
    gap: 20px;
  }
}
</style>