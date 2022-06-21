<template>
  <header>
    <div class="Container Container--default">
      <div class="Header">
        <img class="Header__logo" src="../assets/logo_dark.png"/>

        <ul class="List List--row">
          <li class="List__item" v-for="nav in navlinks" :key="nav.name"><a class="Link Link--grey"> {{ nav.name }}</a></li>
        </ul>

        <div class="IconLink IconLink--rm Spacer--left">
          <img class="IconLink__icon" src="../assets/icons/telephone.svg"/>
          <a class="IconLink__link IconLink__link--tertiary" href="tel:@ViewBag.Phone">89145712434</a>
        </div>

        <div
            @click="showModal"
            class="Button Button--secondary">
          Оставить заявку
        </div>
      </div>
    </div>
  </header>

</template>

<script>
  export default {
    name: "HeaderComponent",
    data() {
      return {
        navlinks: [
            { name: 'Реализованные проекты' },
            { name: 'Новости' },
            { name: 'Контакты' },
        ],
        isModalVisible: false,
      }
    },
    methods: {
      showModal() {
        this.isModalVisible = true;
      },
      closeModal() {
        this.isModalVisible = false;
      }
    },
  }
</script>

<style scoped>
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

.List {
  display: flex;
  padding-left: 0;
}
.List--row {
  flex-direction: row;
  justify-content: start;
  align-items: center;
}
.List--row .List__item:not(:last-child) {
  margin-right: 24px;
}
.List--col {
  flex-direction: column;
  justify-content: start;
  align-items: start;
}
.List--col .List__item:not(:last-child) {
  margin-bottom: 24px;
}
.List--lm120 {
  margin-left: 120px;
}
.List__item {
  list-style-type: none;
}

.Link {
  font-family: "Open Sans", sans-serif;
  font-weight: 400;
  font-size: 16px;
}
.Link--white {
  color: #ffffff;
}
.Link--special {
  color: #ffffff;
  opacity: 0.6;
  font-size: 14px;
}
.Link--grey {
  color: #666666;
}
.Link:active, .Link:focus, .Link:hover {
  cursor: pointer;
  color: #000000;
}

.IconLink {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: start;
}
.IconLink__icon {
  width: 16px;
  height: 16px;
  margin-right: 8px;
}
.IconLink__link {
  font-family: "Montserrat", sans-serif;
  font-weight: 400;
  font-size: 14px;
}
.IconLink__link--white {
  color: #ffffff;
}
.IconLink__link--tertiary {
  color: #254741;
}
.IconLink__link:active, .IconLink__link:focus, .IconLink__link:hover {
  cursor: pointer;
}
.IconLink--rm {
  margin-right: 24px;
}

.Spacer--left {
  margin-left: auto;
}
.Spacer--right {
  margin-right: auto;
}

.Button {
  height: 50px;
  width: 200px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
  font-size: 14px;
  color: #ffffff;
}
.Button--news {
  background-color: transparent;
  border-color: #03B766;
  color: #03B766;
  border: solid 1px;
}
.Button--secondary {
  background-color: #03B766;
}

.Header {
  padding-top: 24px;
  padding-bottom: 24px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: start;
}
.Header__logo {
  width: 160px;
  height: auto;
  margin-right: 80px;
}
</style>
