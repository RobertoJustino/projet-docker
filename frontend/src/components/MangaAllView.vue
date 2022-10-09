<script>
import moment from 'moment'
import axios from 'axios'


export default {

  beforeCreate() {
    document.querySelector('body').setAttribute('style', 'background:#FFFBE9')
  },
  beforeUnmount() {
    document.querySelector('body').setAttribute('style', '')
  },
  data() {
    return {
      mangaList: null,
    }
  },
  mounted() {
    /*    this.$store.dispatch('loadmangas')
       console.log(this.$store.dispatch('loadmangas')); */

    axios
      .get('http://localhost:5000/api/mangas')
      .then((response) => {
        this.mangaList = response.data;
        console.log(this.mangaList)
      })
  },
  computed: {
    mangas() {
      return this.$store.state.mangas;
    }
  },
  methods: {
    mangaId(id) {
      this.$router.push("/manga/" + id);
      console.log(this.$route);
    }
  },
  homeRoute(){
    this.$router.push();
    console.log(this.$route);
  },
  formatDate(value) {
    if (value) {
      return moment(value).format('YYYYMMDD');
    }
  },
}
</script>

<template>
  <div>
    <ul>
      <li><a class="active" href="../">Accueil</a></li>
      <li><a href="/anime">Animes</a></li>
      <li><a href="/manga">Mangas</a></li>
      <li><a href="/login">Connexion</a></li>
      <li><a href="/profile">Profil</a></li>
      <li class="titlePage">Liste des Mangas</li>
    </ul>
  </div>
  <div>
    <div class="card" v-for="manga in mangaList" :key="manga.id" @click="mangaId(manga.id)">
      <h2 v-if="manga">
        {{ manga.title }}
      </h2>
      <img v-if="manga" :src="manga.img_src" alt="Photo d'illustration du manga.">
      <h4 v-if="manga">
        Année de parution
      </h4>
      <p v-if="manga">
        {{ manga.year }}
      </p>
      <h4>
        Synopsis
      </h4>
      <p v-if="manga" class="twohundred-chars">
        {{ manga.description }}
      </p>
      <h4>
        Auteur | Réalisateur
      </h4>
      <p v-if="manga">
        {{ manga.author }}
      </p>
    </div>


  </div>
</template>

<style scoped>
body {
  font-family: 'Helvetica Neue', sans-serif;
}
.twohundred-chars {
  width: 100ch auto;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.card {
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
  /* this adds the "card" effect */
  padding: 16px;
  text-align: center;
  background-color: #E3CAA5;
  margin-top: 100px;
  margin-left: 100px;
  margin-right: 100px;
  border-radius: 0px;
  border: 1px black;
}

img {
  box-shadow: rgba(17, 17, 26, 0.1) 0px 1px 0px, rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 48px;

}

h1 {
  color: #AD8B73;
    font-family: 'Helvetica Neue', sans-serif;
  font-size: 200px;
  font-weight: bold;
  letter-spacing: -1px;
  line-height: 1;
  margin-left: 0px;
}

ul {
  list-style-type: none;
  position: fixed;
  width: 100%;
  top: 0;
  margin: 0;
  padding: 0px;
  overflow: hidden;
  background-color: #E3CAA5;
}

li {
  float: left;
  border-right: 1px solid #FFFBE9;
}

li a {
  display: block;
  color: black;
  font-size: 20px;
  text-align: center;
  padding: 10px 20px;
  text-decoration: none;
  font-family: 'Helvetica Neue', sans-serif;
}

.active {
  background-color: #AD8B73;
  color: black;
}

li a:hover {
  background-color: #FFFBE9;
  color: black;
}

.titlePage {
  font-weight: bold;
  display: block;
  color: black;
  font-size: 20px;
  text-align: center;
  padding: 10px 20px;
  text-decoration: none;
  font-family: 'Helvetica Neue', sans-serif;
}
</style>





