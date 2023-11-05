<template>
  <v-row :style="{ flexDirection: 'column !important', margin: '0px' }">
    <v-row>
      <v-col>
        From
      </v-col>
      <v-col>
        To
      </v-col>
      <v-col>
        Cabin Type
      </v-col>
      <v-col>
        Date
      </v-col>
      <v-col>
        Flight number
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        {{ from }}
      </v-col>
      <v-col>
        {{ to }}
      </v-col>
      <v-col>
        {{ cabinType }}
      </v-col>
      <v-col>
        {{ date }}
      </v-col>
      <v-col>
        {{ flightNumber }}
      </v-col>
    </v-row>
  </v-row>
</template>

<script>
export default {
  props: {
    to: {
      type: String,
      required: true,
    },
    from: {
      type: String,
      required: true,
    },
    cabinType: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
    flightNumber: {
      type: String,
      required: true,
    },
  }
}
</script>

<style></style>