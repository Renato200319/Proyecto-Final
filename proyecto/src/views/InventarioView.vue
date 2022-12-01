<template>
  <nav>
  <router-link to="/home">Home</router-link> |
  <router-link to="/ventas">Ventas</router-link> |
  <router-link to="/about">About</router-link> |
  <router-link to="/contact">Contact</router-link>
  </nav>
  <br><br><br>
  <div>
    <img src="../assets/inventario.jpg" width="150" height="150">
    <table class="table table-borderless">
      <tr>
        <th>Numero de compra</th>
        <th>Codigo de producto</th>
        <th>Vendedor</th>
      </tr>
      <tr v-for="compra of compras" v-bind:key="compra"> 
        <td>{{compra.codigo_c}}</td>
        <td>{{compra.codigo_p}}</td>
        <td>{{compra.usuario_v}}</td>
      </tr>
    </table>
    
  </div>

</template>

<script>
export default {
  name: "InventarioView",
  data(){
    return{
      compras: []
    }
  },
  methods: {
    async obtener_compras(){
      let usuario_c = {usuario: this.$store.state.mi_usuario}
      await fetch('http://127.0.0.1:5000/utecshop/inventario', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(usuario_c)
      }).then((resp)=> resp.json()).then((datos)=> this.compras = datos)
    }
  },
  created(){
    this.obtener_compras()
  }
}
</script>

<style scoped>
nav{
  background-color: black;
}
a{
  color:lavender
}
table{
  font-size: large;
  position: "relative";
  background-color: rgb(255, 255, 255);
  text-decoration-color: aliceblue;

}
</style>