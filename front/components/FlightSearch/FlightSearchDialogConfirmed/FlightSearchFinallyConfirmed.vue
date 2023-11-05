<template>
  <v-dialog v-model="dialog">
    <template #activator="{on, attrs}">
      <v-btn color="primary" height="57" block :disabled="$attrs.disabled" v-bind="attrs" v-on="on">
        <slot />
      </v-btn>
    </template>
    <v-card>
        <v-toolbar dark color="primary">
          Billing confirmation
        </v-toolbar>

        <v-card-text class="mt-5">
          Total amount: ${{ amount }}
        </v-card-text>

        <v-card-text class="mt-5">
          <div class="flex">
            <div>
              Paint using:
            </div>
            <div>
              <v-radio-group v-model="paint" row>
                <v-radio
                  v-for="(text, i) in paints"
                  :key="i"
                  :label="text"
                  :value="i"
                />
              </v-radio-group>
            </div>
          </div>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            outlined
            @click="dialog = false"
          >
            Close
          </v-btn>
          <v-btn
            color="primary"
            outlined
            @click="onAccept"
          >
            Issue tickets
          </v-btn>
        </v-card-actions>
      </v-card>
  </v-dialog>
</template>

<script>
export default {
  props: {
    amount: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {
      dialog: false,
      paint: 0,
    }
  },
  computed: {
    paints() {
      return [
        'Credit Card',
        'Cash',
        'Voucher',
      ]
    },
  },
  methods: {
    onAccept() {
      this.$emit('accept')
      this.dialog = false
    },
  },
}
</script>

<style>

</style>
