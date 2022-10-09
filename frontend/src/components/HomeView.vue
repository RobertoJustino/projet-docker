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
        },
        goToAbout() {
            this.$router.push('/about');
        }
    },
}
</script>

<template>
    <div class="titleBox">
        <h1 class="mainTitle">GoodOtaku.</h1>
    </div>
    <div>
        <button class="button-18" role="button" @click="goToLogin()">Connexion</button>
        <button class="button-18" role="button" @click="goToMangas()">Mangas</button>

        <button class="button-18" role="button" @click="goToAbout()">About</button>
    </div>
</template>

<style scoped>
.mainTitle {
    color: black;
    font-family: 'Helvetica Neue', sans-serif;
    font-size: 200px;
    font-weight: bold;
    letter-spacing: -1px;
    line-height: 1;
    text-align: center;
}

/* CSS */
.button-18 {
    align-items: center;
    background-color: #E3CAA5;
    border: 0;
    box-sizing: border-box;
    color: black;
    cursor: pointer;
    display: inline-flex;
    font-family: -apple-system, system-ui, system-ui, "Segoe UI", Roboto, "Helvetica Neue", "Fira Sans", Ubuntu, Oxygen, "Oxygen Sans", Cantarell, "Droid Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Lucida Grande", Helvetica, Arial, sans-serif;
    font-size: 16px;
    font-weight: 600;
    justify-content: center;
    line-height: 20px;
    max-width: 480px;
    min-height: 40px;
    min-width: 0px;
    overflow: hidden;
    padding: 0px;
    padding-left: 20px;
    padding-right: 20px;
    text-align: center;
    touch-action: manipulation;
    transition: background-color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s, box-shadow 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s, color 0.167s cubic-bezier(0.4, 0, 0.2, 1) 0s;
    user-select: none;
    -webkit-user-select: none;
    vertical-align: middle;
    margin-left: 50px;
    margin-right: 50px;
    margin-top: 50px;
    
  box-shadow: rgba(0, 0, 0, 0.25) 0px 54px 55px, rgba(0, 0, 0, 0.12) 0px -12px 30px, rgba(0, 0, 0, 0.12) 0px 4px 6px, rgba(0, 0, 0, 0.17) 0px 12px 13px, rgba(0, 0, 0, 0.09) 0px -3px 5px;
}

.button-18:hover,
.button-18:focus {
    background-color: #FFFBE9;
    color: black;
}

.button-18:active {
    background: #09223b;
    color: rgb(255, 255, 255, .7);
}

.button-18:disabled {
    cursor: not-allowed;
    background: rgba(0, 0, 0, .08);
    color: rgba(0, 0, 0, .3);
}


</style>
