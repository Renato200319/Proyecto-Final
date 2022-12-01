<template>
  <div class="compras">
    <nav>
      <a><router-link to="/home">Home</router-link></a>
    </nav>
    <h1>Página de compras</h1>
    <img src="../assets/compras.gif" width="400" height="200">
    <br><br><br><br>
    <table>
      <tr v-for="producto of productos" v-bind:key="producto">
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <a>Codigo: <td  v-if="producto.nombre_usuario !== $store.state.mi_usuario">{{producto.codigo}}</td></a> <br>
            <a>Usuario: <td  v-if="producto.nombre_usuario !== $store.state.mi_usuario">{{producto.usuario_nombre}}</td></a><br>
            <a>Nombre: <td  v-if="producto.nombre_usuario !== $store.state.mi_usuario">{{producto.nombre}}</td></a> <br>
            <a>Precio: <td  v-if="producto.nombre_usuario !== $store.state.mi_usuario">{{producto.precio}}</td></a><br>
            <a>Marca: <td  v-if="producto.nombre_usuario !== $store.state.mi_usuario">{{producto.marca}}</td></a> <br>
            <a>Tipo: <td  v-if="producto.nombre_usuario !== $store.state.mi_usuario">{{producto.tipo}}</td></a><br>
            <button class="btn btn-success" v-on:click="comprar(producto.codigo)">Comprar</button>
          </div>
        </div>
  
        <td></td>
      </tr>
    </table>
  </div>
  <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
  <footer-c></footer-c>
  

</template>

<script>
import FooterC from '@/components/FooterC.vue'
export default {
  components: {FooterC},
  name: "ComprasView",
  data(){
    return{
      productos: []
    }
  },
  methods: {
    async obtener_productos(){
      let usuario_p = {usuario: this.$store.state.mi_usuario}
      await fetch('http://127.0.0.1:5000/utecshop/comprar', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(usuario_p)
      }).then((resp)=> resp.json()).then((datos)=> this.productos = datos)
    },
    async comprar(codigo_c, codigo_p, usuario_v){
      let n_compra = {codigo_compra: codigo_c, codigo_producto: codigo_p,
        usuario_comprador: this.$store.state.mi_usuario, usuario_vendedor: usuario_v}
      await fetch('http://127.0.0.1:5000/utecshop/registrar_compra', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(n_compra)
      }).then(()=>alert("producto comprado"))
    }
  },
  created(){
    this.obtener_productos()
  }
}
</script>

<style scoped>
nav{
  background-color:black
}
a{
  color:lavender
}
h1{
  color:rgb(18, 18, 18)
}

</style>