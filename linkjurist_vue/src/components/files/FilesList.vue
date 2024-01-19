<script setup>
  import { useAuthStore } from '@/stores/auth';
  import FileCard from '../files/FileCard.vue'

  const store = useAuthStore();

  const files =  [
    {
      "id": 101,
      "name": "Demanda de Divorcio",
      "description": "Demanda presentada por Juan Pérez solicitando el divorcio de María González.",
      "downloads": 542
    },
    {
      "id": 2,
      "name": "Escrito de Alegaciones",
      "description": "Alegaciones presentadas por la defensa en el caso 'Estado vs. Rodríguez'.",
      "downloads": 312
    },
    {
      "id": 3,
      "name": "Recurso de Amparo",
      "description": "Recurso de amparo interpuesto por Ana Martínez ante el Tribunal Constitucional.",
      "downloads": 789
    },
    {
      "id": 4,
      "name": "Escrito de Defensa Penal",
      "description": "Defensa penal de Roberto Jiménez en el caso 'Estado vs. Jiménez'.",
      "downloads": 231
    },
    {
      "id": 5,
      "name": "Sentencia de Custodia",
      "description": "Sentencia dictada por el juez García en el caso de custodia de los hijos de Laura Torres.",
      "downloads": 623
    },
    {
      "id": 6,
      "name": "Reclamación de Daños",
      "description": "Reclamación de daños y perjuicios presentada por Carlos Fernández contra la compañía XYZ.",
      "downloads": 431
    },
    {
      "id": 7,
      "name": "Testamento",
      "description": "Testamento de Isabel Ramírez, otorgado ante notario el 15 de marzo de 2023.",
      "downloads": 874
    },
    {
      "id": 8,
      "name": "Recurso Administrativo",
      "description": "Recurso administrativo presentado por la empresa ABC contra la resolución del organismo regulador.",
      "downloads": 312
    },
    {
      "id": 9,
      "name": "Contrato de Arrendamiento",
      "description": "Contrato de arrendamiento entre Juan López (arrendador) y Marta Sánchez (arrendataria) para la propiedad ubicada en Calle Principal.",
      "downloads": 542
    }
  ]
</script>


<template>
    <div class="box scrollable-div">
    <h1 class="title">Escritos</h1>
    <h2 class="subtitle">Listado de escritos subidos por usuarios de <span class="secondary-text-color">LinkJurist</span>. </h2>
    <hr>
    <FileCard v-for="file in files" :key="file.id" :file="file" />
  </div>
</template>
