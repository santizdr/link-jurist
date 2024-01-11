<script setup>
    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();
</script>


<template>
    <div class="signup-page">
        <section class="section mt-6">
            <div class="columns is-centered">
                <div class="column is-three-fifths-desktop">
                    <form class="box">
                        <h1 class="title">Registro</h1>
                        <h2 class="subtitle mt-3">Crea tu cuenta en <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span> y empieza a disfrutar sus beneficios</h2>
                        <div class="field">
                            <label class="label">Nombre</label>
                            <div class="control">
                                <input class="input" type="text">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Correo electrónico</label>
                            <div class="control">
                                <input class="input" type="email">
                            </div>
                        </div>

                        <div class="field">
                            <label class="label">Contraseña</label>
                            <div class="control">
                                <input class="input" type="email">
                            </div>
                        </div> 
                        <div class="field">
                            <label class="label">Repetir contraseña</label>
                            <div class="control">
                                <input class="input" type="email">
                            </div>
                        </div>
                        <div class="field is-grouped is-grouped-right mt-1">
                            <!-- <div class="control">
                                <button class="button is-rounded secondary-form-button">Confirmar</button>
                            </div> -->

                            <div class="control">
                                <a v-on:click="store.changeAuthenticatedVal()" class="button is-rounded secondary-form-button">Confirmar</a>
                            </div>
                            <div class="control">
                                <button class="button is-rounded main-form-button">Cancelar</button>
                            </div>
                        </div>
                        <p class="mt-3">Ya tienes cuenta de <span class="secondary-text-color has-text-weight-semibold">Link Jurist</span>? Inicia sesión haciendo click <RouterLink to="login">aquí</RouterLink></p>
                    </form>
                </div>
            </div>
        </section>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SignUp',
    data() {
        return {
            username: '',
            password: '',
            password: '',
            errors: [],
        }
    },

}
</script>