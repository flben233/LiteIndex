<script>
  import {login} from "src/api/loginApi";
  import axios from "axios";

  export default {
    name: 'LoginPage',
    mounted() {
      console.log("Asdasjsdfoi")
    },
    data() {
      return {
        username: "",
        password: "",
        loading: false,
        error: false
      }
    },
    methods: {
      login() {
        this.loading = true;
        login(this.username, this.password).then((resp) => {
          // 这个不能删，具体用法见index.js
          localStorage.setItem("Authorization", resp.data.access_token);
          axios.defaults.headers.common["Authorization"] = resp.data.access_token;
          this.$router.push("/");
        }).catch((err) => {
          if (err.response.status === 401) {
            this.error = true;
          }
          this.loading = false;
        });
      }
    }
  }
</script>

<template>
  <div class="row" id="bg">
    <div class="col-lg-5 col-md-6 col-sm-9 col-xs-11">
        <div id="login-frame">
          <p id="login-text">登录</p>
          <q-input v-model="username" label="用户名" :error="error"/>
          <br/>
          <q-input v-model="password" label="密码" :error="error" type="password"/>
          <br/>
          <div style="display: flex; width: 100%; justify-content: flex-end">
            <q-btn
              color="primary"
              round
              icon="arrow_right_alt"
              :loading="loading"
              @click="login"
            />
          </div>
        </div>
    </div>
  </div>
</template>

<style scoped>
#bg {
  background: url("/wallpaper.png");
  height: 100vh;
  width: 100vw;
  display: flex;
  align-items: center;
  justify-content: center;
  background-size: cover;
}
#login-frame {
  background-color: rgba(255, 255, 255, 0.5);
  border-radius: 1rem;
  backdrop-filter: blur(20px);
  padding: 5%;
  opacity: 100%;
}
#login-text {
  font-size: 30px;
  font-weight: lighter;
}
</style>
