<template>
  <div class="search">
    <v-container>
      <flight-search-filter v-model="filters"/>
      <flight-search-outbound-table v-model="AfterBeforeTo" :air-list="airList" :selected="selectTo" @click:row="onClickRowOutbound"/>
      <flight-search-outbound-table v-if="filters.isReturn"  v-model="AfterBeforeFrom" :air-list="airListReturn" :selected="selectFrom" is-return @click:row="onClickRowReturn"/>
      <flight-search-confirm v-if="showConfirm" @click="onConfirmed"/>
      <flight-search-dialog-confirmed v-if="showConfirm" v-model="isOpen" :outbound="selectTo" :return-flight="selectFrom" :cabin-type="filters.cabinType"/>
    </v-container>
  </div>
</template>

<script>
import FlightSearchConfirm from '../../components/FlightSearch/FlightSearchConfirm.vue'
import FlightSearchFilter from '../../components/FlightSearch/FlightSearchFilter.vue'
import FlightSearchOutboundTable from '../../components/FlightSearch/FlightSearchOutboundTable.vue'
import FlightSearchDialogConfirmed from '~/components/FlightSearch/FlightSearchDialogConfirmed/FlightSearchDialogConfirmed.vue'

const defaultFilters = {
  to: '',
  from: '',
  date: null,
  return: '',
  cabinType: 'Economy',
  isReturn: false,
}

export default {
  components: {
    FlightSearchFilter,
    FlightSearchOutboundTable,
    FlightSearchConfirm,
    FlightSearchDialogConfirmed
},
  async asyncData({
    store,
  }) {
    store.commit('flightSearch/setAirListTo', [])
    store.commit('flightSearch/setAirListReturn', [])
    store.commit('flightSearch/setFilters', {...defaultFilters})

    await store.dispatch('flight/fetchAirportList')

  },
  data: () => ({
    filters: {...defaultFilters},
    selectTo: null,
    selectFrom: null,
    isOpen: false,
  }),
  computed: {
    showConfirm() {
      return this.filters.isReturn ? this.selectTo && this.selectFrom : this.selectTo
    },
    AfterBeforeTo: {
      get() {
        return this.$store.state.flightSearch.AfterBeforeTo
      },
      async set(v) {
        this.$store.commit('flightSearch/setAfterBeforeTo', v)
        await this.$store.dispatch('flightSearch/fetchAirListTo')
      }
    },
    AfterBeforeFrom: {
      get() {
        return this.$store.state.flightSearch.AfterBeforeFrom
      },
      async set(v) {
        this.$store.commit('flightSearch/setAfterBeforeFrom', v)
        await this.$store.dispatch('flightSearch/fetchAirListReturn')
      }
    },
    airList() {
      return this.$store.state.flightSearch.AirListTo
    },
    airListReturn() {
      return this.$store.state.flightSearch.AirListReturn
    },
  },
  watch: {
    filters(val) {
      this.$store.commit('flightSearch/setFilters', this.filters)

      this.$store.dispatch('flightSearch/fetchAirList')
    },
  },
  methods: {
    onClickRowOutbound(e) {
      if (this.selectTo?.id === e.id) {
        this.selectTo = null

        return
      }

      this.selectTo = e
    },
    onClickRowReturn(e) {
      if (this.selectFrom?.id === e.id) {
        this.selectFrom = null
        return
      }
      this.selectFrom = e
    },
    onConfirmed() {
      this.isOpen = true
    }
  }
}
</script>

<style lang="scss" scoped>
.search {
  margin-top: 40px;
}
</style>