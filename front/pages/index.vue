<template>
  <div>
    <v-container>
      <div class="hello">
        {{ $auth.user.msg }}
      </div>
      <div class="time">
        Time spent on system: {{ formatTime }}
      </div>
      <div class="crashes">
        Number of crashes: {{ items.reduce((count, el) => {
          if (el.reason) return count + 1
          return count
        }, 0) }}
      </div>
      <v-data-table
        :headers="headers"
        :item-class="getClass"
        :items="items"
      >
        <template
          #item.crash_report="{item}"
        >
          <template v-if="item.crash_report">
            {{ item.crash_report.reason }}
          </template>
        </template>
      </v-data-table>
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  middleware: ['auth'],
  auth: 'guest',
  async asyncData({store, $auth}) {
    await store.dispatch('userAuth/fetchAuthList')
    await $auth.fetchUser()
  },
  data() {
    return {
      time: 0,
      headers: [
        {
          text: 'Login time',
          value: 'login_date',
        },
        {
          text: 'Logout time',
          value: 'logout_date',
        },
        {
          text: 'Time spent on system',
          value: 'time_spent',
        },
        {
          text: 'Unsuccessful logout reason',
          value: 'crash_report',
        },
      ],
    }
  },
  computed: {
    items() {
      return this.$store.state.userAuth.authList
    },
    formatTime() {
      const date = this.$dayjs.duration(this.time)
      const hour = Math.floor(date.asHours())
      const minute = date.minutes() < 10
        ? '0' + date.minutes()
        : date.minutes()
      const second = date.seconds() < 10 
        ? '0' + date.seconds()
        : date.seconds()

      return `${hour}:${minute}:${second}`
    }
  },

  mounted() {
    this.time = this.$auth.user.total_time_in_system * 1000
    setInterval(() => {
      this.time+=1000
    }, 1000)
  },
  methods: {
    getClass(item) {
      const classes = []

      if (item.crash_report) {
        classes.push('table-error')
      }

      return classes.join(' ')
    },
  },
}
</script>

<style lang="scss" scoped>
.hello {
  margin-top: 20px;
  font-size: 24px;
  line-height: 140%;
  font-weight: 700;
}
.time {
  margin-bottom: 12px;
}
.crashes {
  margin-bottom: 12px;
}
::v-deep() {
  .table-error{
    background: #FF6A55;
    color: #fff;
    &:hover {
      background: #FF6A55 !important;
    }
  }
    }
</style>