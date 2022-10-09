import { createStore } from "vuex";

// Appel du plugin axios
const axios = require("axios");

// Création de la baseURL de l'API
const instance = axios.create({
  baseURL: "http://localhost:5000/api",
});

export default createStore({
  state: {
    mangaInfos: {
      titles: "",
      id: "",
      posterimage: "",
      averageRating: "",
      status: "",
      createdAt: "",
    },
    mangas: [],
    manga: [],
  },
  getters: {},
  mutations: {
    mangaInfos(state, mangaInfos) {
      state.mangaInfos = mangaInfos;
    },
    LOAD_MANGAS(state, manga) {
      state.mangas = manga;
    },
    LOAD_MANGA: function (state, manga) {
      state.manga = manga;
    },
  },
  actions: {
    loadMangas: ({ commit }) => {
      console.debug("loadMangas");
      instance
        .get("/mangas")
        .then((response) => response.data)
        .then((mangas) => {
          commit("LOAD_MANGAS", mangas.data);
        })
        .catch(function (error) {
          return error;
        });
    },
    loadManga: ({ commit }, manga) => {
      console.debug("loadManga");
      instance
        .get("/mangas/" + manga.id)
        .then(function (response) {
          commit("LOAD_MANGA", response.data);
        })
        .catch(function (error) {
          return error;
        });
    },
  },
  modules: {},
});
