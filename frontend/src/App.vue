<template>
  <div class="container" id="app">
    <div>
      <h1>yearn Vault ROI Calculator</h1>
    </div>
    <div id="nav">
      <router-link to="/">ROI</router-link> |
      <router-link to="/faq">F.A.Q.</router-link>
    </div>
    <router-view/>
    <div>
      Like it? Appreciate it!<br />0xa181c52692c902Ea39DfB759eeBDD1807eDF033a
    </div>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #0065d0;
}

#nav a.router-link-exact-active {
  color: #2c3e50;
}
</style>
