<script setup>
    import AccountTeamCard from '../account/AccountTeamCard.vue'
    import FileUpload from '../account/FileUpload.vue'
    import AccountFileCard from '../account/AccountFileCard.vue'
    import AccountCaseCard from '../account/AccountCaseCard.vue'

    import { useUserStore } from '@/stores/user';

    const { props } = defineProps(['account', 'activeTab', 'cases']);

    const store = useUserStore();

    const accCases = [
    {
      "id": 1,
      "title": "Oferta de Servicios en Derecho de la Propiedad Intelectual",
      "description": "Despacho especializado en derecho de la propiedad intelectual ofrece servicios para la protección de patentes, marcas registradas y derechos de autor.",
      "type": "oferta",
      "postDate": "2024-01-16",
      "expiryDate": "2024-01-19",
      "postedBy": "Prudencio Sáez",
      "applications": 456,
      "visualizations": 778,
    },
    {
        "id": 2,
        "title": "Caso Civil: Divorcio por Mutuo Acuerdo",
        "description": "Proceso de divorcio amistoso entre Juan Pérez y María González. Acuerdo de custodia de hijos y división de bienes.",
        "type": "oferta",
        "postDate": "2024-01-17",
        "expiryDate": "2024-01-23",
        "postedBy": "Prudencio Sáez",
        "applications": 201,
        "visualizations": 478,
    },
    {
        "id": 3,
        "title": "Caso Laboral: Despido Injustificado",
        "description": "Demandante reclama despido injustificado contra la empresa XYZ. Se busca una compensación justa por la terminación del empleo.",
        "type": "oferta",
        "postDate": "2024-01-19",
        "expiryDate": "2024-01-28",
        "postedBy": "Prudencio Sáez",
        "applications": 114,
        "visualizations": 202,
    },
    {
        "id": 4,
        "title": "Caso de Familia: Custodia de Menores",
        "description": "Disputa legal por la custodia de menores entre los padres Laura Gómez y Carlos Rodríguez. La audiencia está programada para el próximo mes.",
        "type": "oferta",
        "postDate": "2024-01-20",
        "expiryDate": "2024-01-31",
        "postedBy": "Prudencio Sáez",
        "applications": 46,
        "visualizations": 127,
    }
  ]

  const accFiles = [
    {
        "id": "1",
        "name": "Modelo demanda de divorcio",
        "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!",
        "downloads": 521,
    },
    {
        "id": "2",
        "name": "Modelo caso despido injustificado",
        "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!",
        "downloads": 208,
    },
    {
        "id": "3",
        "name": "Modelo demanda laboral",
        "description": "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Quae soluta dolor maxime adipisci at quos quis quas corrupti voluptatum? Maxime nesciunt quos natus est eligendi quia repellat distinctio odit accusamus!",
        "downloads": 140,
    },
  ]

</script>

<template>
    <div id="tab-content">
        <div v-if="activeTab === 'info-tab'">
            <h1 class="title is-3">Resumen</h1>
            <div class="columns">
                <div class="column is-half">
                    <h2 class="subtitle is-4">Contacto</h2>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Web: </span>{{ account.web }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Email : </span>{{ account.email }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Teléfono : </span>{{ account.phone }}</p>
                </div>
                <div class="column is-half">
                    <h2 class="subtitle is-4">Dirección</h2>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Calle: </span>{{ account.address }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Código postal : </span>{{ account.cp }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">Provincia : </span>{{ account.locality }}</p>
                    <p class="is-size-5 my-1"><span class="secondary-text-color">País : </span>{{ account.country }}</p>
                </div>
            </div>
            <hr>
            <h1 class="title is-3">Sobre nosotros</h1>
            <div class="column is-full">
                <p class="is-size-5 my-1">{{ account.description }}</p>
            </div>
        </div>
        <div v-if="activeTab === 'team-tab'">
            <h1 class="title is-3">Nuestro equipo</h1>
            <AccountTeamCard v-for="user in store.team" :user="user" />
        </div>
        <div v-if="activeTab === 'case-tab'">
            <h1 class="title is-3">Nuestros casos</h1>
            <AccountCaseCard v-for="caso in accCases" :key="caso.id" :caso="caso" /> 
        </div>
        <div v-if="activeTab === 'file-tab'">
            <FileUpload />
            <hr>
            <div class="mx-3">
                <h1 class="title is-3">Nuestros escritos</h1>
                <div class="scrollable-div">
                    <AccountFileCard v-for="file in accFiles" :key="file.id" :file="file" />
                </div>
            </div>
        </div>
    </div>
</template>