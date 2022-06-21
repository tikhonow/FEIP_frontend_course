<template>
  <div class="Container Container--default">
    <div class="News">
      <div class="News__label">
        Новости
      </div>

      <div class="Button Button--news Spacer--left">
        Все новости
      </div>

      <div class="News__container">
        <NewsCard  v-for="i in item" :key="i.id" :item="i"/>
      </div>
    </div>
  </div>
</template>

<script>
  import NewsCard from "@/components/NewsCard";
  export default {
    name: "NewsCo",
    components: {NewsCard},
    data() {
      return {
        item: [{
          image:'C:\\Users\\Tikhonov_r\\WebstormProjects\\feip_front\\src\\assets\\news\\n1.png',
          date: '20 авг 2021',
          label: 'Почему Гуд Вилл строит лучшие дома?',
          description: 'Почему Гуд Вилл строит лучшие дома?'
        },{
          image:'',
          date: '20 авг 2021',
          label: 'Почему Гуд Вилл строит лучшие дома?',
          description: 'Почему Гуд Вилл строит лучшие дома?'
        },{
          image:'',
          date: '20 авг 2021',
          label: 'Почему Гуд Вилл строит лучшие дома?',
          description: 'Почему Гуд Вилл строит лучшие дома?'
        }]
      }
    }
  }
</script>

<style scoped>
/* standart colors */
/* color scheme */
/* fonts */
/* padding */
/* size */
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

.News {
  padding-top: 80px;
  padding-bottom: 80px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.News__label {
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  font-size: 38px;
  color: #000000;
  margin-bottom: 32px;
}
.News__container {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}

.New {
  width: 20%;
  display: flex;
  flex-direction: column;
  align-items: stretch;
  justify-content: start;
}
.New__image {
  width: 100%;
  border-top-left-radius: 20px;
  border-top-left-radius: 20px;
}
.New__date {
  font-family: "Montserrat", sans-serif;
  font-weight: 400;
  font-size: 14px;
  color: #000000;
  margin-top: 16px;
  margin-bottom: 16px;
}
.New__label {
  font-family: "Montserrat", sans-serif;
  font-weight: 500;
  font-size: 20px;
  color: #000000;
}
.New__text {
  font-family: "Open Sans", sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #666666;
  margin-top: 8px;
}

/*# sourceMappingURL=news.css.map */
</style>
