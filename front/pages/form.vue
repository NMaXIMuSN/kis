<template>
  <div class="form-page">
    <v-container>
      <h1>Feedback Form</h1>

      <v-card>
        <v-card-actions>
          <v-form class="form-page__form" @submit.prevent="onSubmit">
            <v-row>
              <v-col cols="4">
                <m-select
                  v-model="form.going_from"
                  :items="airportList"
                  label="Going From"
                  :clearable="false"
                  item-text="name"
                  item-value="id"
                ></m-select>
              </v-col>

              <v-col cols="4">
                <m-select
                  v-model="form.going_to"
                  :items="airportListTo"
                  label="Going To"
                  :clearable="false"
                  item-text="name"
                  item-value="id"
                ></m-select>
              </v-col>

              <v-col cols="4">
                <v-text-field
                  v-model="form.age"
                  label="Age"
                  type="number"
                  outlined
                />
              </v-col>

              <v-col cols="4">
                <m-select
                  v-model="form.gender"
                  :items="genderList"
                  label="Gender"
                  :clearable="false"
                ></m-select>
              </v-col>

              <v-col cols="4">
                <m-select
                  v-model="form.cabin_type"
                  :items="cabinTypeList"
                  label="Cabin Type"
                  :clearable="false"
                ></m-select>
              </v-col>
            </v-row>

            <div v-for="(q, i) in form.questions" :key="i">
              <div class="text-h6">{{ q.title }}</div>
              <v-radio-group v-model="q.value" row>
                <v-radio
                  v-for="ans in answersList"
                  :key="ans.id"
                  :label="ans.title"
                  :value="ans.id"
                />
              </v-radio-group>
            </div>

            <v-btn height="56" block color="primary" type="submit">
              submit
            </v-btn>
          </v-form>
        </v-card-actions>
      </v-card>
    </v-container>
  </div>
</template>

<script>
import MSelect from '~/components/MSelect.vue'

export default {
  components: {
    MSelect,
  },
  async asyncData({ store }) {
    await store.dispatch('flight/fetchAirportList')
    await store.dispatch('flight/fetchAirList', { ordering: '-data' })
  },
  data() {
    return {
      form: {
        going_to: '',
        going_from: '',
        gender: '',
        cabin_type: '',
        age: '',
        questions: null,
      },

      genderList: ['Male', 'Female'],
      cabinTypeList: ['Economy', 'Business', 'First Class'],

      answersList: null,
    }
  },
  computed: {
    airportList() {
      return this.$store.state.flight.airportList
    },
    airportListTo() {
      return this.airportList.filter((el) => el.id !== this.form.going_from)
    },
  },
  mounted() {
    this.$axios.get('/survey/questions/').then(({ data }) => {
      this.form.questions = data.map((e) => ({ ...e, value: 0 }))
    })
    this.$axios.get('/survey/answers/').then(({ data }) => {
      this.answersList = data
    })
  },
  methods: {
    onSubmit() {
      this.$axios
        .post('/survey/create-answer/', {
          user: {
            going_to: this.form.going_to,
            going_from: this.form.going_from,
            gender: this.form.gender,
            cabin_type: this.form.cabin_type,
            age: +this.form.age,
          },
          answers: this.form.questions.map((e) => ({
            question: e.id,
            survey_answer: e.value,
          })),
        })
        .then(() => {
          this.form = {
            going_to: '',
            going_from: '',
            gender: '',
            cabin_type: '',
            age: '',
            questions: this.form.questions.map((e) => {
              e.value = 0
              return e
            }),
          }
        })
    },
  },
}
</script>

<style lang="scss" scoped>
.form-page {
  &__form {
    padding-top: 10px;
  }
}
</style>
