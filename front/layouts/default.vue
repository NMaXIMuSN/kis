<template>
  <v-app>
    <v-app-bar
      v-if="isAuth"
      elevation="0"
      app
    >
      <template>
        <div
          v-if="$route.path === '/admin'"
          class="header__text"
          @click="$nuxt.$emit('open-add-user')"
        >
          Add User
        </div>
        <div
          v-else
          class="header__text"
          @click="$router.push('/admin')"
        >
          Users
        </div>
      </template>
      <div
        class="header__text"
        @click="$router.push('/flight')"
      >
        Flight
      </div>
      <div
        class="header__text header__text-exit"
        @click="logout"
      >
        Exit
      </div>
    </v-app-bar>
    <v-main>
      <Nuxt />
    </v-main>
    <dialog-add-user />
  </v-app>
</template>

<script>
export default {
  name: 'DefaultLayout',
  data() {
    return {
    }
  },
  computed: {
    isAuth() {
      return this.$auth.loggedIn
    },
  },
  methods: {
    logout() {
      this.$auth.logout()
    }
  }
}
</script>

<style lang="scss" scoped>
:deep() {
  .v-toolbar__content {
    gap: 20px
  }
}

.logo--wrpa {
  height: 36px;
}

.exit {
  color: $white;
}

.header__text {
  cursor: pointer;
  position: relative;

  &-exit {
    color: red;

    &::after {
     background-color: red !important; 
    }
  }

  &::after {
    content: "";
    position: absolute;
    bottom: 0px;
    width: 10px;
    height: 1px;
    left: 0;
    background-color: #000;
  }
}
</style>