<template>
  <div class="New">
    <img class="New__image" :src=item.im />
    <div class="New__date">{{this.item.date}}</div>
    <div class="New__label">{{this.item.label}}</div>
    <div class="New__text">{{this.item.description}}</div>
  </div>

</template>

<script>
  export default {
    name: "NewsCard",
    props: {
      item: {}
    }

  }
</script>

<style scoped>
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
</style>
