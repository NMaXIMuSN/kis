<template>
<div class="login-page">
  <login-card />
</div>
</template>

<script>
export default {
  name: 'LoginPage',
  middleware: ['auth'],
  auth: 'guest',
  mounted() {
  }
}
</script>

<style lang="scss" scoped>
.login-page {
  height: 100vh;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background: $bg;
}

</style>
