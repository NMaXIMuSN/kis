<template>
  <div style="margin-top: 40px;">
    <v-container>
      <v-card v-if="stats">
        <v-card-title style="justify-content: center;">
          <img src="../static/logo/logoX2.png" >
        </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="6">
              <v-card>
                <v-card-title>
                  Flight
                </v-card-title>
                <v-card-text>
                  <div>
                    Number confirmed: {{ stats.confirmed }}
                  </div>
                  <div>
                    Number canceled: {{ stats.notConfirmed }}
                  </div>
                  <div>
                    Average daily flight time: {{ stats.average.toFixed(0) }}min
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="6">
              <v-card>
                <v-card-title>
                  Top Customers
                </v-card-title>
                <v-card-text>
                  <ol>
                    <li v-for="(item, key) in stats.top_three_values" :key="key">
                      {{ item[0].split('/')[1] }} ({{ item[1] }} Tickets)
                    </li>
                  </ol>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="6">
              <v-card>
                <v-card-title>
                  Number of passengers flight
                </v-card-title>
                <v-card-text>
                  <div>
                    Busiest day: {{ stats.max.date }} with {{ stats.max.count }} flight
                  </div>
                  <div>
                    Most quiet day: {{ stats.min.date }} with {{ stats.min.count }} flight
                  </div>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="6">
              <v-card>
                <v-card-title>
                  Top AMONIC Airlines office(Revenue)
                </v-card-title>
                <v-card-text>
                  <ol>
                    <li v-for="(item, key) in stats.top_three_office" :key="key">
                      {{ officeList.find(el => el.id === item[0]).title }}
                    </li>
                  </ol>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card>
                <v-card-title>
                  Revenue from ticket sales
                </v-card-title>
                <v-card-text>
                  <v-row row>
                    <v-col>
                      Yesterday: {{ stats.ticketsSave.yesterday }}$
                    </v-col>

                    <v-col>
                      Two days ago: {{ stats.ticketsSave.tooDays }}$
                    </v-col>

                    <v-col>
                      Three days ago: {{ stats.ticketsSave.threeDays }}$
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
            </v-col>
            <v-col cols="12">
              <v-card>
                <v-card-title>
                  Weekly report of percentage of empty seats
                </v-card-title>
                <v-card-text>
                  <v-row row>
                    <v-col>
                      This week: {{ stats.emptySeats.this.countTicket ? (stats.emptySeats.this.countTicket / stats.emptySeats.this.allSeats * 100).toFixed(0) : 100}} %
                    </v-col>

                    <v-col>
                      Last week: {{ stats.emptySeats.last.countTicket ? (stats.emptySeats.last.countTicket / stats.emptySeats.last.allSeats * 100).toFixed(0) : 100}} %
                    </v-col>

                    <v-col>
                      Two last week: {{ stats.emptySeats.too.countTicket ? ((stats.emptySeats.too.countTicket / stats.emptySeats.too.allSeats) * 100).toFixed(0) : 100 }} %
                    </v-col>
                  </v-row>
                </v-card-text>
              </v-card>
            </v-col>
          </v-row>
        </v-card-text>
      </v-card>
      <div v-else>
        loading...
      </div>
    </v-container>
  </div>
</template>

<script>
export default {
  async asyncData({ store }) {
    await store.dispatch('officeList/fetchList')
  },
  data() {
    return {
      stats: null,
    }
  },
  computed: {
    officeList() {
      return this.$store.state.officeList.list
    },
  },
  async mounted() {
    const { data } = await this.$axios.get('/stats/flight')
    this.stats = data
  }
}
</script>

<style>

</style>