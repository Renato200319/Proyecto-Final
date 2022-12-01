<template>
  <div>
    <nav >
      <div>
        <a class="navbar-brand" >UTEC Shop</a> |
            <router-link to="/home">Home</router-link> |
            <router-link to="/registrar">Registrar</router-link> |
            <router-link to="/about">About</router-link>|
            <router-link to="/contact">Contact </router-link>
      </div>
    </nav>

    <img src="../assets/portada.png" width="1250" height="650" alt="portada" >
    <h2>Inicio de sesión</h2>
    <label>Usuario </label> 
    <input type="text" v-bind:value="nombre_usuario" v-on:input="verificar_nombre"><br>
    <br>
    <label>Contraseña </label>
    <input type="text" v-bind:value="contrasenha" v-on:input="verificar_contrasenha"><br>
    <br>
    <button type="button" class="btn btn-primary" v-on:click="casa">Login</button>
  </div>

    <p>¿No tiene una cuenta?</p>
    <a><router-link to="/registrar" type="button" class="btn btn-primary">Registrarse</router-link></a>

  <br><br><br>
  <footer-c></footer-c>

</template>

<script>

import FooterC from '@/components/FooterC.vue'
export default {
  components: { FooterC},
  name: "LoginView",
  data(){
    return{
      nombre_usuario: "",
      contrasenha: ""
    }
  },
  methods: {
    casa(){
      this.$store.dispatch("accion_act_usuario", this.nombre_usuario)
      this.$store.dispatch("accion_act_contra", this.contrasenha)
      this.$router.push('/home')
    },
    verificar_nombre(e){
      this.nombre_usuario = e.target.value
    },
    verificar_contrasenha(e){
      this.contrasenha = e.target.value
    },
    async verificar_usuario(){
      let v_usuario = {nombre_usuario: this.nombre_usuario, contrasenha: this.contrasenha}
      await fetch('http://127.0.0.1:5000/utecshop/login', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(v_usuario)
      }).then((resp)=> resp.json()).then((datos)=>{
        if(datos.nombre_usuario === this.nombre_usuario && datos.contrasenha === this.contrasenha)
          this.casa()
      })
    }
  }
}
</script>

<style scoped>
p{
  color:rgb(24, 24, 119)
}
a{
  color:rgb(249, 249, 249)
}
label{
  color:black
}
h2{
  color:black
}
nav{
  background-color: black;
}
</style>