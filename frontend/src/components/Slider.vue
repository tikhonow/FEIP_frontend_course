<template>
  <div class="Container Container--default">
    <div class="Slider">
      <div class="Slider__text">
        <div class="Slider__text__big">
          Проектируем<br /> и строим<br /> загородные дома
        </div>
        <div class="Slider__text__small">
          Строим дома «под ключ»: от этапа проектирования<br /> и до финишной отделки помещений
        </div>
      </div>

      <img class="Slider__image Slider__image--active" src="../assets/slider/image1.png"/>
      <img class="Slider__image" src="../assets/slider/image2.jpg"/>
      <img class="Slider__image" src="../assets/slider/image3.jpg"/>

      <div class="Slider__button Slider__button--left" @click="Slider(-1)">
        <img class="Slider__button__image" src="../assets/icons/arrow-left.svg" />
      </div>

      <div class="Slider__button Slider__button--right" @click="Slider(1)">
        <img class="Slider__button__image" src="../assets/icons/arrow-right.svg" />
      </div>

      <div class="Slider__dots">
        <div class="Slider__dots__dot Slider__dots__dot--active"></div>
        <div class="Slider__dots__dot"></div>
        <div class="Slider__dots__dot"></div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "SliderCo",
    data() {
      return {
        CurrentFrame: 0,
        Frames :document.getElementsByClassName("Slider__image"),
        Dots: document.getElementsByClassName("Slider__dots__dot"),
      }
    },
    mounted: function() {
      for (var i = 0; i < 3; i++) {
        this.Dots[i].addEventListener("click", function () {
          this.Change(this);
        })
      }

      setInterval(function () {
        this.Slider(1);
      }, 5000);
      console.log(124)
    },
    methods: {
      Slider: function(arg) {
        if (this.CurrentFrame + arg === -1) {
          this.ChangeFrame(2)
          return;
        }
        if (this.CurrentFrame + arg === 3) {
          this.ChangeFrame(0)
          return;
        }
        this.ChangeFrame(this.CurrentFrame + arg)
      },
      ChangeFrame: function(New) {
        this.Frames[this.CurrentFrame].classList.remove("Slider__image--active");
        this.Dots[this.CurrentFrame].classList.remove("Slider__dots__dot--active");

        this.Frames[New].classList.add("Slider__image--active");
        this.Dots[New].classList.add("Slider__dots__dot--active");

        this.Frames[New].classList.toggle("fade");

        this.CurrentFrame = New;
      },
      Change: function (event) {
        var pos = 0;
        for (var i = 0; i < 3; i++) {
          if (this.Dots[i] === event) {
            pos = i;
            break;
          }
        }
        this.ChangeFrame(pos);
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

.Slider {
  margin-top: 40px;
  margin-bottom: 160px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}
.Slider__text {
  position: absolute;
  z-index: 4;
  left: 10%;
  width: 30%;
}
.Slider__text__big {
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  font-size: 46px;
  color: #ffffff;
}
.Slider__text__small {
  font-family: "Open Sans", sans-serif;
  font-weight: 400;
  font-size: 16px;
  color: #ffffff;
}
.Slider__image {
  position: relative;
  z-index: 0;
  display: none;
  width: 100%;
  border-radius: 30px;
}
.Slider__image--active {
  display: block;
}
.Slider__button {
  width: 48px;
  height: 48px;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  z-index: 10;
  background-color: #03B766;
  border-radius: 10px;
}
.Slider__button__image {
  width: 12px;
  height: 12px;
}
.Slider__button--left {
  position: absolute;
  top: calc(50% - 24px);
  left: 16px;
}
.Slider__button--right {
  position: absolute;
  top: calc(50% - 24px);
  right: 16px;
}
.Slider__dots {
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: absolute;
  top: calc(100% - 40px);
}
.Slider__dots__dot {
  background-color: #ffffff;
  height: 12px;
  width: 12px;
  border-radius: 6px;
  margin: 8px;
}
.Slider__dots__dot:hover {
  cursor: pointer;
  background-color: #03B766;
}
.Slider__dots__dot--active {
  background-color: #03B766;
}

.fade {
  animation: fade 0.9s;
}

@keyframes fade {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/*# sourceMappingURL=slider.css.map */
</style>
