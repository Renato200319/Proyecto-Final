<template>
    <nav>    
    <a></a><router-link to="/home">Home</router-link> |
    <router-link to="/contact">Contact</router-link> 
    </nav>
    <h1>About UTEC Shop</h1>
    <p> This is a website aimed to help students from UTEC to sell some products and purchase them as well</p>
    <img src="../assets/utecsinos.png" height="300" width="600">
</template>

<script>
export default{
    name:'AboutView'
}
</script>

<style scope>
nav{
    background-color:black
}
a{
    color:lavender
}
</style>