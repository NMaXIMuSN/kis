<template>
  <v-dialog
    v-model="isOpen"
    persistent
  >
    <v-card>
      <v-card-title>
        No logout detected
      </v-card-title>
      <v-card-text>
        No logout detected for your last login on {{ $dayjs(time).format('DD/MM/YYYY HH:mm') }}
      </v-card-text>
      <v-card-text>
        Reason: 
        <v-textarea
          v-model="reason"
          auto-grow
          rows="4"
          outlined
          :error-messages="errors.reason"
          name="input-7-4"
        />
      </v-card-text>
      <v-card-text>
        <v-radio-group
          v-model="type"
          :error-messages="errors.type"
        >
          <v-radio
            v-for="item in typeErrors"
            :key="item.value"
            :label="item.lable"
            :value="item.value"
          />
        </v-radio-group>
      </v-card-text>
      <v-card-text>
        <v-btn
          outlined
          color="primary"
          @click="sendReport"
        >
          Confirm
        </v-btn>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    time: {
      type: String,
      required: true,
    },
    userLogId: {
      type: Number,
      default: undefined,
    },
    value: Boolean,
  },
  data() {
    return {
      isOpen: this.value,
      reason: '',
      type: '',
      errors: {
        reason: '',
        type: ''
      },
      typeErrors: [
        {
          lable: 'Software crash',
          value: 'software_crash',
        },
        {
          lable: 'System crash',
          value: 'system_crash ',
        },
      ]
    }
  },
  watch:{
    isOpen(val) {
      this.$emit('input', val)
    },
    value(val) {
      this.isOpen = val
    }
  },
  methods: {
    sendReport() {
      this.$axios.post('/send_report', {
        description: this.reason,
        reason: this.type,
        userlog: this.userLogId
      })
        .then(() => {
          this.errors = {
            reason: '',
            type: ''
          }
          this.$emit('confirm')
        })
        .catch(({response}) => {
          if (!this.reason) {
            this.errors.reason = response.data.description
          }
          if (!this.type) {
            this.errors.type = response.data.reason
          }
        })
    }
  }
}
</script>

<style>

</style>