<template>
  <v-dialog
    v-model="isOpen"
    width="550px"
  >
    <v-card>
      <v-card-title>
        Add User
      </v-card-title>


      <div class="v-card__text">
        <div class="login-card__row">
          <div>Email*</div>
          <v-text-field
            v-model="form.email"
            outlined
            :error-messages="error.includes('email') ? 'field is required' : undefined"
          />
        </div>
        <div class="login-card__row">
          <div>FIrst Name*</div>
          <v-text-field
            v-model="form.first_name"
            outlined
            :error-messages="error.includes('first_name') ? 'field is required' : undefined"
          />
        </div>
        <div class="login-card__row">
          <div>Last Name*</div>
          <v-text-field
            v-model="form.last_name"
            outlined
            :error-messages="error.includes('last_name') ? 'field is required' : undefined"
          />
        </div>
        <div class="login-card__row">
          <div>Office*</div>
          <v-select
            v-model="form.office"
            :items="officeList"
            attach
            clearable
            item-text="title"
            placeholder="Choose an office"
            :error-messages="error.includes('office') ? 'field is required' : undefined"
            item-value="id"
            outlined
          />
        </div>
        <div class="login-card__row">
          <div>Birthdate*</div>
          <v-text-field
              v-model="form.birthdate"
              outlined
              lang="eu"
              type="date"
              :error-messages="error.includes('birthdate') ? 'field is required' : undefined"
            />
        </div>
        <div class="login-card__row">
          <div>Password*</div>
          <v-text-field
            v-model="form.password"
            outlined
            type="password"
            :error-messages="error.includes('password') ? 'field is required' : undefined"
          />
        </div>
        <div class="flex">
          <v-btn
            color="primary"
            @click="save"
          >
            Save
          </v-btn>
          <v-spacer />
          <v-btn
            outlined
            color="red"
            @click="isOpen = false"
          >
            Cancel
          </v-btn>
        </div>
      </div>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  data() {
    return {
      isOpen: false,
      error: '',
      form: {
        email: '',
        first_name: '',
        last_name: '',
        office: '',
        birthdate: '',
        password: '',
      }
    }
  },
  computed: {
    officeList() {
      return this.$store.state.officeList.list
    },
    roleList() {
      return this.$store.state.officeList.roleList
    },
  },
  watch: {
    isOpen(newValue) {
      if (!newValue) {
        this.form = {
          email: '',
          first_name: '',
          last_name: '',
          office: '',
          birthdate: '',
          password: '',
        }
        this.error = ''
      }
    }
  },
  mounted() {
    this.$nuxt.$on('open-add-user', () => {
      this.isOpen = true
    })
  },
  methods: {
    async save() {
      await this.$axios.post('add_user', {
        role_id: 'User',
        ...this.form
      })
        .then(async () => {
          await this.$store.dispatch('users/fetchUsersList')
          this.isOpen = false
          this.error = ''
        })
        .catch(({response}) => {
          this.error = response.data.msg
        })
    },
  },
}
</script>

<style lang="scss" scoped>
.flex {
  display: flex;
}
</style>