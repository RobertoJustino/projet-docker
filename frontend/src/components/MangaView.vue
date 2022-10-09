<script>
import axios from 'axios'

export default {
  beforeCreate() {
    document.querySelector('body').setAttribute('style', 'background:#FFFBE9')
  },
  beforeUnmount() {
    document.querySelector('body').setAttribute('style', '')
  },
  /*data() {
    return {
      list: [this.$store.dispatch("loadAnimes")],
      post: {
        id:"",
      }
    };
  },*/
  data() {
    return {
      currentManga: null,
      currentMangaGenres: null,
      commentBox: '',
    }
  },
  mounted() {
    /* 		this.id = this.$route.params.id;
        this.$store.dispatch('loadAnime', { id: this.$route.params.id })
        console.log(this.$store.dispatch('loadAnime', { id: this.$route.params.id })) */
    axios
      .get('http://localhost:5000/api/mangas/' + this.$route.params.id)
      .then((response) => {
        this.currentManga = response.data;
        console.log(this.currentManga)
      })
    axios
      .get('http://localhost:5000/api/mangas/' + this.$route.params.id + '/genres')
      .then((response) => {
        this.currentMangaGenres = response.data;
        console.log(this.currentMangaGenres)
      })
  },
  computed: {
    anime() {
      return this.$store.state.anime;
    }
  },
  methods: {
    postComment: function()
        {
            axios.post('/api/recipes/'+this.recipe.id+'/comment', {
                    api_token: this.user.api_token,
                    body: this.commentBox
                })
                .then((response) => {
                    this.comments.unshift(response.data);
                    this.commentBox = '';
                })
                .catch((error) => {
                    console.log(error);
                })
        }
  },
}
</script>

<template>
  <div>
    <div>
      <ul>
        <li><a class="active" href="../">Accueil</a></li>
        <li><a href="/manga">Mangas</a></li>
        <li><a href="/login">Connexion</a></li>
        <li><a href="/profile">Profil</a></li>
      </ul>
    </div>
    <div>
      <h1 v-if="currentManga">{{ currentManga[0].title }}</h1>
      <div class="card">
        <img v-if="currentManga" :src="currentManga[0].img_src" alt="Photo d'illustration du manga.">
        <h4>
          Année de parution
        </h4>
        <p v-if="currentManga">
          {{ currentManga[0].year }}
        </p>
        <h4>
          Synopsis
        </h4>
        <p v-if="currentManga">
          {{ currentManga[0].description }}
        </p>
        <h4>
          Auteur | Réalisateur
        </h4>
        <p v-if="currentManga">
          {{ currentManga[0].author }}
        </p>
        <h4>
          Genre
        </h4>
        <div v-if="currentMangaGenres">
          <div v-for="genre in currentMangaGenres" :key="genre.name">
            <p v-if="genre">
              {{ genre.name }}
            </p>

          </div>
        </div>
      </div>
    </div>
  <div>
  <p>
  Ajouter un commentaire
  </p>
  <textarea></textarea>
  <p>Ajouter une note (sur 5)</p>
  <input>
  </div>
    <!-- Comment section, list all comment for this manga -->
    <div v-if="currentManga">
      <div v-for="review in currentManga.review" :key="review">
        <div class="container-com">
          <div class="auteur">
          Auteur
          </div>
          <div class="note">
            {{ review.note }} / 5
          </div>
          <div class="date-com">
            11/06/2022
          </div>
          <div class="commentaire">
          {{ review.review }}
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<style scoped>
body {
  font-family: 'Helvetica Neue', sans-serif;
}

img {
  box-shadow: rgba(17, 17, 26, 0.1) 0px 1px 0px, rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 48px;

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

h1 {
  color: #AD8B73;
  font-family: 'Helvetica Neue', sans-serif;
  font-size: 50px;
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

.container-com {
  background-color: #E3CAA5;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  ;
  grid-template-rows: 0.2fr 1.3fr;
  gap: 0px 0px;
  grid-template-areas:
    "auteur note date-com"
    "commentaire commentaire commentaire";
  justify-content: start;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  margin-top: 100px;
  margin-left: 100px;
  margin-right: 100px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

.auteur {
  grid-area: auteur;
  text-align: left;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}

.note {
  grid-area: note;
  text-align: center;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}

.date-com {
  grid-area: date-com;
  text-align: right;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}

.commentaire {
  grid-area: commentaire;
  text-align: left;
  box-shadow: rgba(99, 99, 99, 0.2) 0px 2px 8px 0px;
}

</style>
