<template>
  <div class="login-card">
    <div class="login-card__img-wrap">
      <img src="/logo/logoX2.png" />
    </div>
    <div class="login-card__title">Login</div>
    <div
      v-if="countError > 0"
      class="login-card__error"
    >
      <div>
        {{ errorMesage }}
      </div>
      <div v-if="countError < 3">
        Try: {{ 3 - countError }}
      </div>
      <div v-else>
        Too many attempts. Wait {{ secontWait }} seconds to continue
      </div>
    </div>
    <div class="login-card__row">
      <div>Username</div>
      <v-text-field v-model="form.email" :disabled="disable" outlined />
    </div>
    <div class="login-card__row">
      <div>Password</div>
      <v-text-field
        v-model="form.password"
        :disabled="disable"
        outlined
        type="password"
      />
    </div>
    <v-row
      class="actions"
    >
      <v-col
        cols="3"
      >
       <v-btn
         color="primary"
          :disabled="disable"
          @click="login"
        >
          Lodin
        </v-btn>
      </v-col> 
      <v-col
        cols="3"
      >
        <a
          href="https://www.google.ru"
        >
          <v-btn
            color="red"
          >
            Exit
          </v-btn>
        </a>
      </v-col> 
    </v-row>
   
    
    <dialog-error
      v-model="isOpenError"
      :time="timeLastLogin"
      :user-log-id="user_log_id"
      @confirm="nextPage"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        email: '',
        password: '',
      },
      errorMesage: '',
      countError: 0,
      disable: false,
      secontWait: 10,
      isOpenError: false,
      timeLastLogin: '',
      user_log_id: null,
    }
  },
  watch: {
    countError(newValue) {
      if (newValue === 3) {
        this.disable = true
        
        const timer = setInterval(() => {
          this.secontWait--
        }, 1000);

        setTimeout(() => {
          this.disable = false
          this.errorMesage = ''
          this.countError = 0
          this.secontWait = 10
          clearInterval(timer)
        }, 10000)
      }
    },
  },
  methods: {
    login() {
        this.$auth.loginWith('local', { data: this.form })
          .then(async () => {
            await this.$axios.get('is_graceful_logout')
              .then(({data}) => {
                if (!data.is_graceful_logout) {
                  this.user_log_id = data.user_log_id
                  this.isOpenError = true
                  this.timeLastLogin = data.last_login
                }
                else {
                  this.nextPage()
                }
              })
          })
          .catch(({response}) => {
            this.errorMesage = response.data.msg
            this.countError++
          })
      },
    nextPage() {
      if (this.$auth.user.is_admin) {
        this.$router.push('/admin')
      }
      else {
        this.$router.push('/')
      }
    },
    logout() {
      this.$auth.logout()
    },
  },
}
</script>

<style lang="scss" scoped>
.login-card {
  max-width: 600px;
  padding: 24px;
  border-radius: 12px;
  background: $white;
  display: flex;
  flex-direction: column;
  align-items: center;

  &__img {
    &-wrap {
      max-width: 350px;
      padding: 0 25px;
      margin-bottom: 24px;
    }
  }

  &__title {
    font-size: 24px;
    line-height: 120%;
    font-weight: 700;
    margin-bottom: 24px;
  }

  &__error {
    color: #FF6A55;
    font-size: 14px;
    line-height: 140%;
    margin-bottom: 12px;
  }

  &__row {
    width: 100%;
  }

  .actions {
    width: 100%;
    justify-content: space-between;
  }
}
</style>
