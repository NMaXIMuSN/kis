<template>
  <v-select
    v-bind="$attrs"
    v-model="item"
    :items="items"
    :clearable="clearable"
    outlined
  >
    <template
      v-for="(slot) in $scopedSlots"
      #[slot]="scopedSlots"
    >
      <slot
        :name="slot"
        v-bind="scopedSlots"
      />
    </template>
  </v-select>
</template>

<script>
export default {
  name: 'MSelect',
  props: {
    value: {
      type: [String, Number],
      default: null,
    },
    items: {
      type: Array,
      required: true,
    },
    clearable: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      item: this.value,
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

<style>

</style>