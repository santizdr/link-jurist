<script setup>
    import AccountHeader from '../account/AccountHeader.vue'
    import AccountTabs from '../account/AccountTabs.vue'

    import { useAuthStore } from '@/stores/auth';
    const store = useAuthStore();

    const account = {
      "id": 1,
      "name": "Prudencio Sáez y Asociados",
      "accImg": "https://bulma.io/images/placeholders/256x256.png",
      "slogan": "Soluciones innovadoras para desafíos legales",
      "description": "Prudencio Sáez y Asociados es un despacho integrado por profesionales con máxima experiencia como Fiscales, Abogados del Estado, Magistrados, Docentes Universitarios o Representantes Sindicales de alto nivel, que te aportan la tranquilidad y seguridad de disponer del mejor equipo, competitivo y muy preparado para conseguir tus objetivos y cubrir tus necesidades. Prudencio Sáez y Asociados dispone de asistencia jurídica on line, a través de videollamadas y videoconferencia (Skype, Zoom, Whatsapp,..) y teléfono, así como otros métodos de comunicación. Para más información visitanos en persona. ", 
      "address": "C/ Gastor nº 7",
      "cp": "41007",
      "locality": "Sevilla",
      "country": "España",
      "web": "www.example.com",
      "email": "mail@psya.com",
      "phone": "954575450",
      "nif": "29548963V",
    }
</script>


<template>
    <section class="section mt-4">
    <div v-if="store.authenticated" class="columns is-centered">
      <div class="column is-three-quarters-desktop">
          <div class="box">
            <AccountHeader :account="account" />
            <AccountTabs :account="account" />
        </div>
      </div>
  </div>
  </section>
</template>
