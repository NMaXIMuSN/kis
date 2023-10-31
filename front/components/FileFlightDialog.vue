<template>
  <v-dialog
    v-model="isOpen"
    max-width="600px"
  >
    <v-card>
      <v-card-title>
        apply Schedules Changes
      </v-card-title>

      <v-card-text>
        <v-row>
          <v-col
            cols="8"
          >
            <v-file-input
              v-model="file"
              outlined
              :error-messages="errorText"
              height="60px"
            />
          </v-col>
          <v-col
            cols="4"
          >
            <v-btn
              height="60px"
              block
              class="primary"
              @click="uploadFile"
            >
              Import
            </v-btn>
          </v-col>
        </v-row>
        <v-row v-if="Object.keys(result).length">
          <v-col cols="12">
            Resilt
          </v-col>
          <v-col cols="6">
            Copies count: <strong>{{result.copies_count}}</strong>
          </v-col>
          <v-col cols="6">
            Сreated count: <strong>{{result.created_count}}</strong>
          </v-col>
          <v-col cols="6">
            Invalid record count: <strong>{{result.invalid_record_count}}</strong>
          </v-col>
          <v-col cols="6">
            Updates count: <strong>{{result.updates_count}}</strong>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    value: Boolean,
  },
  data() {
    return {
      isOpen: this.value,
      file: null,
      result: {},
      errorText: '',
    }
  },
  watch: {
    isOpen(val) {
      this.$emit('input', val)
    },
    value(val) {
      this.isOpen = val
    }
  },
  methods: {
    uploadFile() {
      if (this.file) {
        const formData = new FormData()

        formData.append('file', this.file)
        this.$axios.post(`/flight.upload_file/${this.file.name}`, formData)
          .then(({data}) => {
            this.result = data
            this.$emit('updateShedule')
          })
          .catch(() => {
            this.errorText = 'The wrong file is selected'
            this.result = {}
          })
      }
      else {
        this.errorText = 'Select a file'
      }
    },
    fileError() {

    }
  },
}
</script>

<style>

</style>