<template>
  <v-data-table
    :headers="headers"
    v-bind="$attrs"
    v-on="$listeners"
  >
    <template v-slot:item.actions="{ index }">
      <v-icon
        :color="'black'"
        small
        @click="deletePassenger(index)"
      >
        mdi-close-box-outline
      </v-icon>
    </template>
  </v-data-table>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        {
          text: 'firstName',
          value: 'firstName',
        },
        {
          text: 'lastName',
          value: 'lastName',
        },
        {
          text: 'date',
          value: 'date',
        },
        {
          text: 'passportNumber',
          value: 'passportNumber',
        },
        {
          text: 'passportCountry',
          value: 'passportCountry.name',
        },
        {
          text: 'phone',
          value: 'phone',
        },
        {
          text: 'Actions',
          align: 'start',
          sortable: true,
          value: 'actions',
        }
      ]
    }
  },
  methods: {
    deletePassenger(index) {
      this.$emit('deletePassenger', index)
      console.log(index)
    }
  }
}
</script>

<style>

</style>