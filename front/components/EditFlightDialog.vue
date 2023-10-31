<template>
  <v-dialog
    v-model="isOpen"
    max-width="600px"
  >
    <v-card>
      <v-card-title>
        Schedules Edit
      </v-card-title>
      <v-card-text>
        <v-row>
          <v-col>
            To <strong>{{ form.to }}</strong>
          </v-col>
          <v-col>
            From <strong>{{ form.from }}</strong>
          </v-col>
          <v-col>
            Aircraft <strong>{{ form.aircraft }}</strong>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              :return-value.sync="form.date"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="form.date"
                  outlined
                  readonly
                  clearable
                  label="Date"
                  v-bind="attrs"
                  v-on="on"
                />
              </template>
              <v-date-picker
                v-model="form.date"
                no-title
                scrollable
              >
                <v-spacer></v-spacer>
                <v-btn
                  text
                  color="primary"
                  @click="menu = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                  text
                  color="primary"
                  @click="$refs.menu.save(form.date)"
                >
                  OK
                </v-btn>
              </v-date-picker>
            </v-menu>
          </v-col>
          <v-col>
            <v-menu
              ref="menu2"
              v-model="menu2"
              :close-on-content-click="false"
              :return-value.sync="form.time"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="form.time"
                  outlined
                  readonly
                  clearable
                  label="Time"
                  v-bind="attrs"
                  v-on="on"
                />
              </template>
              <v-time-picker
                v-if="menu2"
                v-model="form.time"
                format="24hr"
                @click:minute="$refs.menu2.save(form.time)"
              ></v-time-picker>
            </v-menu>
          </v-col>
          <v-col>
            <v-text-field
              v-model="form.economy_price"
              outlined
              label="Economy price"
              append-icon="mdi-currency-usd"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col></v-col>
          <v-col>
            <v-btn
              color="primary"
              block
              @click="accept"
            >
              Update
            </v-btn>
          </v-col>
          <v-col>
            <v-btn
              color="red"
              block
              @click="isOpen = false"
            >
              Cancel
            </v-btn>
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
    formValue: {
      type: Object,
      required: true,
    },
  },
  data() {
    return{
      isOpen: false,
      form: this.formValue,
      menu: false,
      menu2: false,
    }
  },
  computed: {
  },
  watch: {
    value(val) {
      this.isOpen = val
    },
    formValue(val) {
      this.form = {
        to: val.to || '',
        from: val.from || '',
        economy_price: val.economy_price || '',
        aircraft: val.aircraft || '',
        time: val.time || '',
        date: val.date || '',
      }
    },
    isOpen(val) {
      this.$emit('input', val)
      if (!val) {
        this.form = {}
      }
    },
  },
  methods: {
    async accept() {
      try {
        await this.$axios.patch(`flight.schedule_edit/${this.formValue.id}`, {
          date: this.form.date,
          economy_price: this.form.economy_price,
          time: this.form.time,
        })
        this.$emit('updateShedule')
        this.isOpen = !this.isOpen
        
      } catch (error) {
        console.log(error)  
      }
    },
  }
}
</script>

<style>

</style>