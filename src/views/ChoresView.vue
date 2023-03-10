<template>
    <div class="chores-wrapper">
        <div class="chore-announcer">
            <h1>New chores every Wednesday!</h1>
        </div>
        <div class="people-wrapper">
            <person-card v-for="person in people" :person="person" @toggle-chores-done="toggleChoresDone" />
        </div>
    </div>
</template>

<script setup lang="ts">
import PersonCard from '@/components/PersonCard.vue'
import type { Person } from '@/components/PersonCard.vue'
import { NIcon, useMessage } from 'naive-ui';
import { Check } from '@vicons/fa';
import { computed, defineComponent, onMounted, ref, type Ref } from 'vue';
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
const message = useMessage()

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
    ]).catch(() => {
        message.error("Couldn't load chores. Sounds like a server error...")
    })
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
    }).catch(() => {
        message.error("Oh snap, that didn't work! Please try again later.")
    })
}

const allChoresDone = computed(() => {
    return people.value.every(element => element.done)
})
</script>

<style scoped>
.people-wrapper {
    display: flex;
    flex-direction: column;
    padding: 1rem;
    gap: 1rem;
}

.chore-announcer {
    margin-top: 1rem;
    margin-right: 1rem;
    margin-left: 1rem;
    overflow: hidden;
    text-align: center;
    border: 1px solid var(--primary-color-300);
}


@media only screen and (min-width: 768px) {
    .people-wrapper {
        flex-direction: row;
        gap: 2rem;
        margin: 0 2rem;
    }
    .chores-wrapper {
        display: grid;
        place-items: center;
    }
    .chore-announcer {
        padding: 0 3rem;
    }
}
</style>
