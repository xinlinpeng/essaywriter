<template>
  <div class="img_box">
  <!-- <div id="app"> -->
    <!-- <img src="./assets/logo.png">-->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
/* #app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
.img_box{
	width: 100%;height: 115%;
	background-image: url(assets/background.jpg);
	background-size: cover; /* 使图片平铺满整个浏览器（从宽和高的最大需求方面来满足，会使某些部分无法显示在区域中） */
	position: absolute; /* 不可缺少 */
	z-index: -1;
	background-repeat: no-repeat;
	/* overflow: hidden; */
	/* overflow: auto; */
}
</style>
