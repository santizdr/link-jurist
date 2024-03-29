<script setup>
    import axios from 'axios'
    import { ref } from 'vue'
    import router from '@/router'
    import { useAuthStore } from '@/stores/auth';
    import { useCasesStore } from '@/stores/cases';
    import { useDetailsStore } from '@/stores/details';

    const { props } = defineProps(['caso']);
    const authStore = useAuthStore();
    const caseStore = useCasesStore();
    const detailsStore = useDetailsStore();

    const tags = {
        1: "Derecho penal",
        2: "Derecho civil",
        3: "Derecho laboral",
        4: "Derecho mercantil",
        5: "Derecho administrativo",
        6: "Derecho internacional",
    }

    const alert = ref({
        message: "",
        class: "",
    });

    function closeAlert() {
        alert.value.message = "";
        alert.value.class = "";
    }
    
    function applyToCase(case_id, acc_id) {
      const me = authStore.account.id;
      const data = {
        "applicant": me,
        "case": case_id,
      }

      axios.post("/api/apply/", data)
        .then(response => {
            if(response.data.message === "applied") {
              alert.value.message = "Has aplicado para la asiganción del caso";
              alert.value.class = "span-success";
            } else if (response.data.message === "delete") {
              alert.value.message = "Has cancelado tu solicitud de asiganción al caso";
              alert.value.class = "span-success";
            } else {
              console.log("Error")
              alert.value.message = "Se ha producido un error";
              alert.value.class = "span-error";
            }

            if (router.currentRoute.value.path.match("/cases")) {
              caseStore.fetchCasesData(authStore.account.id);
            } else {
              detailsStore.fetchAccountData(authStore.account.id, detailsStore.account.id);
            }
        })
        .catch(error => {
            console.log("Error: ", error);
        })
        
    }
</script>

<template>
    <div class="card my-3">
      <div class="card-content">
        <div class="media">
          <div class="media-content">    
            <div v-if="alert.message !== ''" class="my-3">
              <article class="message">
                  <div class="message-header"  :class="alert.class">
                    <p>{{ alert.message }}</p>
                    <a @click="closeAlert()" class="delete" aria-label="delete"></a>
                  </div>
              </article>  
            </div>   
            <p class="title is-4">{{ caso.title }} - <RouterLink :to="'/account/' + caso.account" class="black-text has-text-weight-semibold">{{ caso.account_name }}</RouterLink></p>
            <p class="subtitle is-5 secondary-text-color is-capitalized">{{ caso.type === "OFFER" ? "Oferta"  : "Demanda" }}</p>
            <div>
              <span v-for="tag in caso.tags" class="tag is-medium mr-2" :class="'tag-' + tag">{{ tags[tag] }}</span>
            </div>
          </div>
        </div>
        <div class="content">
          <p>{{ caso.description }}</p>
          <p><span class="secondary-text-color">Fecha de publicación: </span><time :datetime="caso.post_date">{{ caso.post_date }}</time></p>
          <p><span class="secondary-text-color">Fecha de expiración: </span><time :datetime="caso.expiry_dDate">{{ caso.expiry_date }}</time></p>
          <div class="columns is-vcentered">
            <div class="column">
              <div v-if="caso.account !== authStore.account.id">
                <a v-if="!caso.is_applied" @click.prevent="applyToCase(caso.id)" class="button secondary-bg-color has-text-weight-semibold white-text navbar-button" style="width: 150px;">
                  <font-awesome-icon :icon="['fas', 'plus']" class="top-ranking-icon mr-2" />Aplicar
                </a>
                <a v-else @click.prevent="applyToCase(caso.id)" class="button main-bg-color has-text-weight-semibold white-text navbar-button" style="width: 150px;">
                  <font-awesome-icon :icon="['fas', 'minus']" class="top-ranking-icon mr-2" />Cancelar
                </a>
              </div>
              <div v-else>
                <button class="button disabled disabled-btn secondary-form-button">No puedes aplicar a tu caso</button>
              </div>
            </div>
            <div class="is-narrow">
              <div class="has-text-right case-file-stats mr-4">
                <span class="secondary-text-color mx-3">{{ caso.applications }} <font-awesome-icon class="mx-1"  :icon="['fas', 'arrow-right']" /></span>
              </div>
            </div>
           </div>
        </div>
      </div>
    </div>   
</template>
