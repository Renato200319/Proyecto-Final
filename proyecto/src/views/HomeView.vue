<template>
  <div class="home">
    <nav>
    <router-link to="/compras">
      <a>Comprar</a></router-link> |
    <router-link to="/ventas">Vender</router-link> |
    <router-link to="/inventario">Inventario</router-link> <br> |
    <router-link to="/">Logout</router-link>
    </nav>

    <h1>"Bienvenido a UTEC Shop"</h1>
    <br>
    <div v-for="usuario of usuarios" v-bind:key="usuario">
      <h2 v-if="usuario.nombre_usuario === $store.state.mi_usuario">Usuario: {{usuario.nombre_usuario}}</h2>
      <h2 v-if="usuario.contrasenha === $store.state.mi_contrasenha">Contraseña: {{usuario.contrasenha}}</h2>
  </div>
  <br>
  <img src="../assets/shop.jpg" width="1500">
  <br>
  </div>
  <h3>Valido para Perú. Recibe tu primer pedido totalmente gratis!</h3>


  <footer-c msg=""></footer-c>
</template>

<script>
import FooterC from '@/components/FooterC.vue'
export default {
  components: {FooterC},
  name: 'HomeView',
  data(){
    return{
      usuarios: []
    }
  },
  methods: {
    async obtener_usuarios(){
      await fetch('http://127.0.0.1:5000/utecshop/usuarios')
          .then((resp) => resp.json()).then((datos) => this.usuarios = datos)
    }
  },
  created(){
    this.obtener_usuarios()
  }
}
</script>

<style scoped>
nav{
  background-color:black;

}
a{
  color:lavender;

}
h3{
  color:brown
}
</style>
