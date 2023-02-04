<template>
    <div class="chores-wrapper">
        <person-card v-for="person in people" :person="person" @toggle-chores-done="toggleChoresDone" />
    </div>
</template>

<script setup lang="ts">
import PersonCard from '@/components/PersonCard.vue'
import type { Person } from '@/components/PersonCard.vue'
import { NIcon } from 'naive-ui';
import { Check } from '@vicons/fa';
import { computed, defineComponent, onMounted, reactive, ref, type Ref } from 'vue';
import axios from 'axios';
import { useUrlStore } from '@/stores/urls';

export interface Chore {
    id: number,
    name: string,
    desc: string,
    date_added: string
}
defineComponent({
    components: { PersonCard, NIcon, Check }
})

const urlStore = useUrlStore()

let people: Ref<Person[]> = ref([])
let chores = ref([])

onMounted(async () => {
    await Promise.all([
        axios.get(`${urlStore.backendIP}/users/`).then((response) => {
            people.value = response.data.results
            people.value.forEach((element) => console.log(element.profile_pic))
        }),
        axios.get(`${urlStore.backendIP}/chores/`).then((response) => {
            chores.value = response.data.results
        })
    ]).catch((err) => console.log(err))
})

async function toggleChoresDone(person: Person) {
    let done: boolean, done_date: string | null
    if (!person.done) {
        done = true
        done_date = new Date(Date.now()).toISOString()
    } else {
        done = false
        done_date = null
    }
    const postData = { done, done_date }
    await axios.patch(`${urlStore.backendIP}/users/${person.id}/`, postData).then((response) => {
        const objIndex = people.value.findIndex(element => element.id == person.id)
        people.value[objIndex].done = response.data.done
        people.value[objIndex].done_date = response.data.done_date
    })
}

const allChoresDone = computed(() => {
    return people.value.every(element => element.done)
})
</script>

<style scoped>
.chores-wrapper {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    gap: 1rem;
}

@media only screen and (min-width: 768px) {
    .chores-wrapper {
        flex-direction: row;
        gap: 2rem;
        margin: 0 2em;
    }
}
</style>
