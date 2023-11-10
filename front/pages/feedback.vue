<template>
  <div>
    <v-switch
      v-model="isGeneral"
      :label="isGeneral ? 'General' : 'Expand'"
    ></v-switch>

    <template v-if="isGeneral">
      <v-data-table
        v-if="general"
        :headers="general.headers"
        :items="general.data"
      ></v-data-table>
    </template>

    <template v-else>
      <v-data-table
        v-if="expand"
        :headers="expand.headers"
        :items="expand.data"
        :items-per-page="-1"
      ></v-data-table>
    </template>
  </div>
</template>

<script>
export default {
  async asyncData({ store }) {
    await store.dispatch('flight/fetchAirportList')
  },
  data() {
    return {
      data: null,
      isGeneral: true,
      answersList: null,
      questions: null,
    }
  },

  computed: {
    airportList() {
      return this.$store.state.flight.airportList
    },

    users() {
      if (!this.data) return

      const set = new Set()

      return this.data
        .map((e) => {
          if (set.has(e.user_info.id)) return null

          set.add(e.user_info.id)
          return e.user_info
        })
        .filter((e) => e)
    },

    expand() {
      if (!this.answersList || !this.questions) return

      const data = this.questions
        .map((q) => {
          return [
            { answer: q.title },
            ...this.answersList.map((a) => {
              return {
                answer: a.title,
                ...this.countByAnswer(a.id, q.id),
              }
            }),
          ]
        })
        .flat()

      return {
        data,
        headers: Object.keys(data[1]).map((e) => ({ text: e, value: e })),
      }
    },

    general() {
      if (!this.users) return

      const data = this.countRow(this.users)

      return {
        data: [data],
        headers: Object.keys(data).map((e) => ({ text: e, value: e })),
      }
    },
  },

  mounted() {
    this.$axios.get('/survey/answers-list/').then(({ data }) => {
      this.data = data
    })
    this.$axios.get('/survey/answers/').then(({ data }) => {
      this.answersList = data
    })
    this.$axios.get('/survey/questions/').then(({ data }) => {
      this.questions = data
    })
  },

  methods: {
    countRow(users) {
      const obj = {
        gender: {
          male: 0,
          female: 0,
        },
        age: {
          '18-24': 0,
          '24-39': 0,
          '40-59': 0,
          '60+': 0,
        },
        cabin_type: {
          economy: 0,
          'first class': 0,
          business: 0,
        },
        going_to: {},
      }

      this.airportList.forEach((e) => {
        obj.going_to[e.iata_code] = 0
      })

      users.forEach((u) => {
        const key = Object.keys(obj.age).find((e) => {
          if (e === '60+' && u.age >= 60) return true

          const [left, right] = e.split('-').map((e) => +e)
          if (u.age >= left && u.age <= right) {
            return true
          }

          return false
        })
        if (key) {
          obj.age[key]++
        }

        if (u.gender) {
          obj.gender[u.gender.toLowerCase()]++
        }

        if (u.cabin_type) {
          obj.cabin_type[u.cabin_type.toLowerCase()]++
        }

        if (u.going_to) {
          obj.going_to[this.findIataCodeById(u.going_to)]++
        }
      })

      const data = {
        ...obj.gender,
        ...obj.age,
        ...obj.cabin_type,
        ...obj.going_to,
      }

      return data
    },

    findIataCodeById(id) {
      return this.airportList.find((e) => e.id === id).iata_code
    },

    countByAnswer(ansId, qId) {
      const users = this.data.filter(
        (e) => e.question.id === qId && e.survey_answer.id === ansId
      )

      return {
        total: users.length,
        ...this.countRow(users.map((u) => u.user_info)),
      }
    },
  },
}
</script>

<style lang="scss" scoped></style>
