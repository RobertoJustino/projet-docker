<script>

export default {
    beforeCreate() {
        document.querySelector('body').setAttribute('style', 'background: #FFFBE9')
    },
    beforeUnmount() {
        document.querySelector('body').setAttribute('style', '')
    },
    data() {
        return {
            anime: null,

        }
    },
    mounted() {
    },
    computed: {
    },
    methods: {

        goToMangas() {
            this.$router.push('/manga');
        },
        goToLogin() {
            this.$router.push('/login');
        }
    },
}
</script>

<template>
    <div>
        <ul>
            <li><a class="active" href="../">Accueil</a></li>
            <li><a href="/manga">Mangas</a></li>
            <li><a href="/profile">Profil</a></li>

            <li><a href="/login">Connexion</a></li>
            <li class="titlePage">Inscription</li>

        </ul>
    </div>

    <div>
        <div class="titleBox">
            <h1 class="mainTitle">Inscription.</h1>
            <div>
                <p>
                    Saisissez un nom d'utilisateur
                </p>
                <input type="">
            </div>
            <div>
                <p>
                    Saisissez un mot de passe
                </p>
                <input type="password">
            </div>
            <div>
                <p>
                    Confirmez votre mot de passe
                </p>
                <input type="password">
            </div>
            <br>
            <div>
                <a href="/register">Pas encore inscrit?</a>
            </div>
        </div>
    </div>

</template>

<style scoped>
.mainTitle {
    color: black;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 100px;
    font-weight: bold;
    letter-spacing: -1px;
    line-height: 1;
    text-align: center;
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
