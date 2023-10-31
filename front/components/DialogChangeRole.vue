<template>
  <v-dialog
    v-model="isOpen"
    width="550px"
  >
  <v-card>
    <v-card-title>
      Edit role
    </v-card-title>
    <v-card-text class="">
      <div>
        <div>
          Email address
        </div>
        <v-text-field
          v-model="form.email"
          outlined
        />
      </div>
      <div>
        <div>
          Name
        </div>
        <v-text-field
          v-model="form.first_name"
          outlined
        />
      </div>
      <div>
        <div>
          Last_name
        </div>
        <v-text-field 
          v-model="form.last_name"
          outlined
        />
      </div>
      <div>
        <div>
          Office
        </div>
        <v-select
            v-model="form.office_id"
            :items="officeList"
            item-text="title"
            placeholder="Choose an office"
            item-value="id"
            outlined
          />
      </div>

      <div>
        <div>
          Role
        </div>
        <v-radio-group v-model="form.role_id">
          <v-radio
            v-for="n in roles"
            :key="n.id"
            :label="n.title"
            :value="n.id"
          />
        </v-radio-group>
      </div>
      <div>
        <v-btn
          color="primary"
          @click="accept"
        >
          Accept
        </v-btn>
      </div>
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
    }
  },
  computed: {
    officeList() {
      return this.$store.state.officeList.list
    },
    roles() {
      return this.$store.state.officeList.role
    }
  },
  watch: {
    value(val) {
      this.isOpen = val
    },
    formValue(val) {
      this.form = {
        role_id: this.roles.find(el => el.title === val.role__title)?.id || '',
        email: val.email || '',
        first_name: val.first_name || '',
        last_name: val.last_name || '',
        office_id: val.office || '',
        id: val.id || '',
      }
    },
    isOpen(val) {
      this.$emit('input', val)
      if (!val) {
        this.form = {
          email: '',
          first_name: '',
          last_name: '',
          office: '',
          role__title: 'User',
        }
      }
    },
  },
  methods: {
    async accept() {
      await this.$axios.post('edit_role', this.form)
        .then(async ({data}) => {
          await this.$store.dispatch('users/fetchUsersList')

          this.isOpen = false
        })
        .catch(({response}) => {
        })
    },
  }
}
</script>
