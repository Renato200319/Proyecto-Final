<template>
  <div>
    <nav>
      <a>
      <router-link to="/registrar_producto">Registrar producto</router-link> |
      <router-link to="/home">Home</router-link>
    </a>
    </nav>
    <h1>Esta es la página de ventas</h1>
    <table>
      <tr>
        <th>Codigo</th>
        <th>Nombre</th>
        <th>Precio</th>
        <th>Marca</th>
        <th>Categoria</th>>
      </tr>
      <tr v-for="producto of productos" v-bind:key="producto">
        <td>{{producto.codigo}}</td>
        <td>{{producto.nombre}}</td>
        <td>{{producto.precio}}</td>
        <td>{{producto.marca}}</td>
        <td>{{producto.tipo}}</td>
      </tr>
    </table>
  </div>

</template>

<script>
export default {
  name: "VentasView",
  data(){
    return{
      productos: []
    }
  },
  methods: {
    async obtener_productos(){
      let usuario_p = {usuario: this.$store.state.mi_usuario}
      await fetch('http://127.0.0.1:5000/utecshop/vender', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(usuario_p)
      }).then((resp)=> resp.json()).then((datos)=> this.productos = datos)
    }
  },
  created(){
    this.obtener_productos()
  }
}
</script>

<style scoped>
table{
  padding-left: 575px;
}
nav{
  background-color:black
}
a{
  color:lavender
}
</style>
