<!-- eslint-disable vue/valid-v-slot -->
<template>
  <div class="page">
    <v-container>
      <div>
        <span> Office: </span>
        <span>
          <v-select
            v-model="currenOffice"
            :items="officeList"
            clearable
            item-text="title"
            placeholder="Choose an office"
            item-value="id"
            outlined
          />
        </span>
      </div>
      <div>
        <v-data-table
          :headers="headers"
          :item-class="getClass"
          :items="users"
        >
          <template #item.office="{ item }">
            {{ getListName(item) }}
          </template>
          <template v-slot:item.office="{ item }">
            <template v-if="item.office">
              {{ item.office && item.office.title ? item.office.title : '-' }}
            </template>
          </template>
          <template v-slot:item.actions="{ item }">
            <v-icon
              :color="!item.is_active ? 'white' : 'black'"
              small
              class="mr-2"
              @click="editItem(item)"
            >
              mdi-pencil
            </v-icon>
            <v-icon
              :color="!item.is_active ? 'white' : 'black'"
              small
              @click="swapActive(item)"
            >
              {{ item.is_active ? 'mdi-account-outline' : 'mdi-account-off-outline' }}
            </v-icon>
          </template>
        </v-data-table>
      </div>
      <dialog-change-role
        v-model="dialog"
        :form-value="editedItem"
      />
    </v-container>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  middleware: 'onlyFromAdmin',
  async asyncData({ store }) {
    await Promise.all([
      store.dispatch('officeList/fetchList'),
      store.dispatch('officeList/fetchRole'),
      store.dispatch('users/fetchUsersList'),
    ])
  },
  data() {
    return {
      currenOffice: {},
      headers: [
        {
          text: 'Name',
          align: 'start',
          sortable: false,
          value: 'first_name',
        },
        {
          text: 'Last name',
          align: 'start',
          sortable: false,
          value: 'last_name',
        },
        {
          text: 'Age',
          align: 'start',
          sortable: true,
          value: 'age',
        },
        {
          text: 'User Role',
          align: 'start',
          sortable: true,
          value: 'role__title',
        },
        {
          text: 'Email Addres',
          align: 'start',
          sortable: false,
          value: 'email',
        },
        {
          text: 'Office',
          align: 'start',
          sortable: true,
          value: 'office',
        },
        {
          text: 'Actions',
          align: 'start',
          sortable: true,
          value: 'actions',
        }
      ],
      editedItem: {},
      dialog: false,
      editedIndex: null,
    }
  },

  computed: {
    officeList() {
      return this.$store.state.officeList.list
    },
    users() {
      return this.$store.state.users.usersList
    },
  },
  watch: {
    currenOffice(newValue) {
      this.$store.dispatch('users/fetchUsersList', newValue)
    }
  },
  methods: {
    async swapActive(item) {
      await this.$axios.post('toggle_activity', {
        id: item.id
      })
        .then(() => {
          this.$store.dispatch('users/fetchUsersList')
        })
    },
    editItem (item) {
      this.editedIndex = item.id
      this.editedItem = Object.assign({}, item)
      this.dialog = true
    },
    getListName(item) {
      const list = this.officeList.find((el) => el.id === item.office)
      if (list) {
        return list.title
      }
      return '-'
    },
    getClass(item) {
      const classes = ['row-table']

      if (!item.is_active) {
        classes.push('row-table-no-active')
      }
      else if (item.role && item.role.title === 'Administrator') {
        classes.push('row-table-administrator')
      }

      return classes.join(' ')
    }
  },
}
</script>

<style lang="scss" scoped>
.page {
  padding-top: 20px;
}

:deep() {
  .row-table {
    transition: all .3s ease;
    &-no-active {
      background: #FF6A55 !important;
      color: #fff;
      &:hover {
        background: #FF6A55 !important;
      }
    }

    &-administrator {
      background: #4adb3a;

      &:hover {
        background: #4adb3a !important;
      }
    }
  }
}
</style>
