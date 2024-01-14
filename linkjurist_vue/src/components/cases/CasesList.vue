<script setup>
    import { useAuthStore } from '@/stores/auth';
    import CaseCard from '../cases/CaseCard.vue'

    const store = useAuthStore();

    const cases = [
      {
      "id": 1,
      "title": "Caso de Defensa Criminal",
      "description": "El cliente enfrenta cargos criminales y busca representación legal para su defensa en el tribunal. Se necesita experiencia en derecho penal y juicios criminales.",
      "type": "demanda",
      "postDate": "2024-01-15",
      "expiryDate": "2024-01-19",
      "postedBy": "Prudencio Sáez",
    },
    {
      "id": 2,
      "title": "Oferta de Servicios en Derecho de la Propiedad Intelectual",
      "description": "Despacho especializado en derecho de la propiedad intelectual ofrece servicios para la protección de patentes, marcas registradas y derechos de autor.",
      "type": "oferta",
      "postDate": "2024-01-16",
      "expiryDate": "2024-01-19",
      "postedBy": "S&P Asociados",
    },
    {
      "id": 3,
      "title": "Caso de Accidente de Tráfico",
      "description": "Se busca asesoramiento legal para un caso de accidente de tráfico. El cliente ha sufrido lesiones y busca una compensación justa. Experiencia en derecho de lesiones personales es esencial.",
      "type": "demanda",
      "postDate": "2024-01-17",
      "expiryDate": "2024-01-19",
      "postedBy": "Summa Legal",
    },
    {
      "id": 4,
      "title": "Oferta de Servicios en Derecho Inmobiliario",
      "description": "Despacho de abogados especializado en derecho inmobiliario ofrece asesoramiento para transacciones de bienes raíces, contratos de arrendamiento y litigios relacionados con propiedades.",
      "type": "oferta",
      "postDate": "2024-01-18",
      "expiryDate": "2024-01-19",
      "postedBy": "Lucio Anneo Séneca",
    },
    {
      "id": 5,
      "title": "Caso de Discriminación en el Trabajo",
      "description": "El cliente ha experimentado discriminación en el lugar de trabajo y busca representación legal para presentar una demanda por discriminación laboral.",
      "type": "demanda",
      "postDate": "2024-01-19",
      "expiryDate": "2024-01-19",
      "postedBy": "Diego Velázquez",
    },
    {
      "id": 6,
      "title": "Oferta de Servicios en Derecho Ambiental",
      "description": "Despacho especializado en derecho ambiental ofrece servicios para casos relacionados con regulaciones ambientales, cumplimiento y litigios ambientales.",
      "type": "oferta",
      "postDate": "2024-01-20",
      "expiryDate": "2024-01-19",
      "postedBy": "Caparros Abogados",
    },
    {
      "id": 7,
      "title": "Caso de Herencia y Testamento",
      "description": "Se necesita representación legal en un caso de herencia y testamento. Hay disputas entre los herederos sobre la distribución de los bienes.",
      "type": "demanda",
      "postDate": "2024-01-17",
      "expiryDate": "2024-01-19",
      "postedBy": "Vanguardia Legal",
    },
  ]
</script>


<template>
    <div class="box" style="overflow: auto; max-height: 720px;">

    <h1 class="title">Casos abiertos</h1>
    <h2 class="subtitle">Listado de oferta y demanda de servicios para todos los casos publicados por los usuarios en la plataforma. </h2>
    <hr>
    <CaseCard v-for="caso in cases" :key="caso.id" :caso="caso" />
  </div>
</template>
