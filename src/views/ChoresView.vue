<template>
    <div id="chores-container">
        <person-card v-for="person in people" :person="person" @toggle-chores-done="toggleChoresDone"/>
    </div>
    <span>{{ chores }}</span>
</template>

<script setup lang="ts">
import PersonCard from '@/components/PersonCard.vue'
import type { Person } from '@/components/PersonCard.vue'
import { defineComponent, onMounted, reactive, ref, type Ref } from 'vue';
import axios from 'axios';
import { useUrlStore } from '@/stores/urls';

interface Chore {
    id: number,
    name: string,
    desc: string,
    date_added: string
}
defineComponent({
    components: { PersonCard }
})

const urlStore = useUrlStore()

let people: Ref<Person[]> = ref([])
let chores = ref([])

onMounted(async () => {
    await axios.get(`${urlStore.backendIP}/users/`).then((response) => {
        people.value = response.data.results
    })
    await axios.get(`${urlStore.backendIP}/chores/`).then((response) => {
        chores.value = response.data.results
    })
})

function toggleChoresDone(done: boolean) {
    //TODO: toggle server state
    //TODO: get server state
    //TODO: set local state
}
</script>

<style scoped>
#chores-container {
    display: flex;
    gap: 1rem;
    padding: 1rem;
}

</style>