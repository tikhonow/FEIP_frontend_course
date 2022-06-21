<template>
  <footer>
    <div class="Container Container--tertiary">
      <div class="Footer">
        <img class="Footer__logo" src="../assets/logo_light.png"/>

        <ul class="List List--col List--lm120">
          <li class="List__item" v-for="link in links" :key="link.message"><a class="Link Link--white"> {{ link.name }}</a></li>
        </ul>

        <ul class="List List--col List--lm120">
          <li class="List__item IconLink">
            <img class="IconLink__icon" src="../assets/icons/telephone.svg" />
            <a class="IconLink__link IconLink__link--white" href="tel:@ViewBag.Phone">+7 (900)900-90-90</a>
          </li>
          <li class="List__item IconLink">
            <img class="IconLink__icon" src="../assets/icons/email-white.svg" />
            <a class="IconLink__link IconLink__link--white" href="mailto:@ViewBag.Mail">info@gmail.com</a>
          </li>
          <li class="List__item IconLink">
            <img class="IconLink__icon" src="../assets/icons/location-marker-white.svg" />
            <a class="IconLink__link IconLink__link--white">г.Владивосток  <br> ул.Выселковая  49, стр3 </a>
          </li>
        </ul>

        <div class="Button Button--secondary Spacer--left">
          Оставить заявку
        </div>

        <ul id="special" class="List List--row">
          <li class="List__item">
            <a class="Link Link--special">© Загдом, 2021</a>
          </li>
          <li class="List__item">
            <a class="Link Link--special">Политика конфиденциальности</a>
          </li>
          <li class="List__item">
            <a class="Link Link--special">Пользовательское соглашение</a>
          </li>
        </ul>

      </div>
    </div>
  </footer>
</template>

<script>
  export default {
    name: "FooterCo",
    data() {
      return {
        links: [
          { name: 'Реализованные проекты' },
          { name: 'Новости' },
          { name: 'Контакты' },
        ]
      }
    }
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

.Footer {
  padding-top: 24px;
  padding-bottom: 24px;
  display: flex;
  flex-direction: row;
  align-items: start;
  justify-content: start;
  flex-wrap: wrap;
}
.Footer__logo {
  width: 160px;
  height: auto;
  margin-right: 30px;
}
.Footer #special .List__item:not(:last-child) {
  margin-right: 130px;
}

/*# sourceMappingURL=footer.css.map */

</style>
