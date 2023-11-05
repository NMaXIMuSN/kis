<template>
  <v-menu
ref="menu" v-model="menu" :close-on-content-click="false" :return-value.sync="item"
    transition="scale-transition" offset-y min-width="auto">
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
v-model="item" outlined readonly clearable :label="label" v-bind="attrs"
        v-on="on"></v-text-field>
    </template>
    <v-date-picker v-model="item" no-title scrollable>
      <v-spacer></v-spacer>
      <v-btn text color="primary" @click="menu = false">
        Cancel
      </v-btn>
      <v-btn text color="primary" @click="$refs.menu.save(item)">
        OK
      </v-btn>
    </v-date-picker>
  </v-menu>
</template>
<script>
export default {
  name: 'MDatePicker',
  props: {
    value: {
      type: String,
      default: '',
    },
    label: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      item: this.value,
      menu: false,
    }
  },
  watch: {
    value(val) {
      this.item = val
    },
    item(val) {
      this.$emit('input', val)
    },
  }
}
</script>
<style lang="scss"></style>