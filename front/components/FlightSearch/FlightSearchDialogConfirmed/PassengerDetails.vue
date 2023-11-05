<template>
  <v-card>
    <v-card-title>
      Passenger Details
    </v-card-title>
    <v-form ref="form" v-model="valid" lazy-validate>
      <v-row style="margin: 0;">
        <v-col cols="4">
          <v-text-field v-model="form.firstName" label="firstName" outlined :rules="[(v) => !!v || 'is required']"/>
        </v-col>
        <v-col cols="4">
          <v-text-field v-model="form.lastName" label="lastName" :rules="[(v) => !!v || 'is required']" outlined/>
        </v-col>
          <v-col cols="4">
            <m-date-picker
              v-model="form.date"
              label="Birthdate"
              :rules="[(v) => !!v || 'is required']"
            />
        </v-col>
        <v-col cols="4">
          <v-text-field v-model="form.passportNumber" label="passportNumber" :rules="[(v) => !!v || 'is required']" outlined/>
        </v-col>
        <v-col cols="4">
          <m-select v-model="form.passportCountry" label="passportCountry" :rules="[(v) => !!v || 'is required']" :items="$store.state.countries.countries" :item-text="'name'" return-object/>
        </v-col>
        <v-col cols="4">
          <v-text-field v-model="form.phone" label="phone" :rules="[(v) => !!v || 'is required']" outlined type="phone"/>
        </v-col>
        <v-col cols="4">
        </v-col>
        <v-col cols="4">
        </v-col>
        
        <v-col cols="4">
          <v-btn color="primary" block height="57" @click="onAdd">Add</v-btn>
        </v-col>
      </v-row>
    </v-form>
  </v-card>
</template>

<script>
import MDatePicker from '../../MDatePicker.vue'
import MSelect from '../../MSelect.vue'

const defaultForm = {
  firstName: '',
  lastName: '',
  date: '',
  passportNumber: '',
  passportCountry: '',
  phone: '',
}
export default {
  components: { MDatePicker, MSelect },
  data() {
    return {
      form: {...defaultForm},
      valid: false,
    }
  },
  methods: {
    onAdd() {
      this.valid = this.$refs.form.validate()

      if (this.valid) {
        this.$emit('addPassenger', this.form)
        
        this.form = {...defaultForm}
        this.$refs.form.reset()
      }
    }
  }
}
</script>

<style>

</style>