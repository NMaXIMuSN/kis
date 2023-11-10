<template>
  <div v-if="selectTicket">
    <v-row>
      <v-col>
        Full Name: <b>{{ selectTicket.first_name }} {{ selectTicket.last_name }}</b>
      </v-col>
      <v-col>
        Passport number: <b>{{ selectTicket.passport_number }}</b>
      </v-col>
      <v-col>
        Cabin class: <b>{{ selectTicket.cabin_type.name }}</b> 
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  props: {
    selectTicket: {
      type: Object,
      default: null,
    }
  }
}
</script>

<style>

</style>