<template>
  <div>
    <nav>
      <a><router-link to="/home">Home</router-link></a>
    </nav>
    <h1>¿Qué productos vas a vender?</h1>
    <h3>Registra tus productos</h3>
  <img src="../assets/productos.png" width="200" height="200">
  <br><br><br>
    <label>Codigo</label>
    <input type="text" v-bind:value="codigo" v-on:input="registrar_codigo"><br>
    <br>
    <label>Nombre</label>
    <input type="text" v-bind:value="nombre" v-on:input="registrar_nombre"><br>
    <br>
    <label>Precio</label>
    <input type="text" v-bind:value="precio" v-on:input="registrar_precio"><br>
    <br>
    <label>Marca</label>
    <input type="text" v-bind:value="marca" v-on:input="registrar_marca"><br>
    <br>
    <label>Categoria</label>
    <input type="text" v-bind:value="tipo" v-on:input="registrar_tipo"><br>
    <br>
    <button v-on:click="productos">Registrar producto</button>
  </div>
</template>

<script>
export default {
  name: "RegistrarProductoView",
  data(){
    return {
      codigo: "",
      usuario_nombre: this.$store.state.mi_usuario,
      nombre: "",
      precio: "",
      tipo: "",
      marca: ""
    }
    // aquí se guarda el usuario con el que se está logeado actualmente para registrar sus productos
  },
  methods: {
    productos(){
      this.$router.push('/ventas')
    },
    registrar_codigo(e){
      this.codigo = e.target.value
    },
    registrar_nombre(e){
      this.nombre = e.target.value
    },
    registrar_precio(e){
      this.precio = e.target.value
    },
    registrar_marca(e){
      this.marca = e.target.value
    },
    registrar_tipo(e){
      this.tipo = e.target.value
    },
    async registrar_producto(){
      let n_producto = {codigo: this.codigo, usuario: this.usuario_nombre, nombre: this.nombre,
        precio: this.precio, marca: this.marca, categoria: this.tipo}
      await fetch('http://127.0.0.1:5000/utecshop/registrar_producto', {
        method: 'POST',
        headers: {
          'Content-type': 'application/json'
        },
        body: JSON.stringify(n_producto)
      }).then(this.productos)
  }
  // se supone que los datos del input y el valor del usuario se tienen que guardar en la base de datos mediante
  // flask usando un fetch
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
</style>