<template>
  <v-row>
    <v-col>
      Selected Amenities: <b>{{price}}$</b>
    </v-col>
    <v-col>
      Duties and Taxis: <b>{{ dutiesAndTaxis }}$</b>
    </v-col>
    <v-col>
      Total payable: <b>{{ allPrice}}$</b>
    </v-col>
  </v-row>
</template>

<script>
export default {
  props: {
    price: {
      type: Number,
      default: 0,
    },
    purchaseAmenitiesCost: {
      type: Number,
      default: 0,
    }
  },
  computed: {
    dutiesAndTaxis() {
      return (this.price * 0.05).toFixed(2)
    },
    allPrice() {
      return (Number(this.dutiesAndTaxis) + this.price).toFixed(2)
    }
  },
}
</script>

<style>

</style>