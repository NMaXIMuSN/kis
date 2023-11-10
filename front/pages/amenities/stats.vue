<template>
  <div style="margin-top: 40px;">
    <v-container>
      <v-card>
        <v-card-text>
          <v-row>
            <v-col>
              <v-text-field v-model="flight_number" outlined label="Flight number"/>
            </v-col>
            <v-col>
              <m-date-picker v-model="date" label="Date"/>
            </v-col>
            <v-col>
              <v-btn block color="primary" height="56" @click="onSearch">
                OK
              </v-btn>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
      <v-data-table :headers="headers" :items="stats || []">
        <template
          #item.cabin_type="{index}"
        >
          {{ index === 0 ? "Economy" : index === 1 ? 'Business' : "First Class"}}
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
import MDatePicker from '../../components/MDatePicker.vue'
export default {
  components: { MDatePicker },
  data() {
    return {
      flight_number: '',
      date: '',
      stats: null,
      amenities: []
    }
  },
  computed: {
    headers() {
      return [
        {
          text: 'cabin Type',
          value: 'cabin_type',
        },
        ...this.amenities.map(el => ({
          text: el.service,
          value: el.service,
        }))
      ]
    }
  },
  async mounted() {
    const { data } = await this.$axios.get('tickets/amenities')
    this.amenities = data
  },
  methods: {
    async onSearch() {
      try {
        const { data } = await this.$axios.get('/tickets/amenities/stats', {
          params: {
            flight_number: this.flight_number || null,
            date: this.date || null,
          }
        })
        this.stats = Object.values(data);
      } catch (error) {
        console.error(error)
      }
    },
  }
}
</script>

<style>

</style>