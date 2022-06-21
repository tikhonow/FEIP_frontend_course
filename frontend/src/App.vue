<template>
  <HeaderComponent/>
  <slider-co/>
  <about-co/>
  <projects-co/>
  <news-co/>
  <footer-co/>
</template>

<script>

import HeaderComponent from "@/components/Header";
import FooterCo from "@/components/footer";
import SliderCo from "@/components/Slider";
import AboutCo from "@/components/About";
import ProjectsCo from "@/components/Projects";
import NewsCo from "@/components/News";
export default {
  name: 'App',
  components: {
    NewsCo,
    ProjectsCo,
    AboutCo,
    SliderCo,
    FooterCo,
    HeaderComponent
  }
}
</script>

<style>


.Container {
  padding-left: 150px;
  padding-right: 150px;
  position: relative;
}
.Container--default {
  background-color: #ffffff;
}
.Container--primary {
  background-color: #F5F7F3;
}
.Container--tertiary {
  background-color: #254741;
}
body, html {
  padding: 0;
  margin: 0;
}

a {
  text-decoration: none;
}
</style>
