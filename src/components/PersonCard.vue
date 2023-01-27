<template>
    <n-card :title="person.full_name">
        <template #cover>
            <img :src="person.profile_pic" alt="A cool person." />
        </template>

        <div class="chore">
            <div class="chore-title">{{ person.chore[0].name }}</div>
            <div>{{ person.chore[0].desc }}</div>
        </div>

        <template #action>
            <div class="card-action" v-if="person.done">
                <n-button type="success" @click="toggleDone">
                    <template #icon>
                        <n-icon :component="ThumbsUpRegular" />
                    </template>
                </n-button>
                <span>Chore was done on {{ person.done_date }}</span>
            </div>
            <div class="card-action" v-else>
                <n-button type="error" @click="toggleDone">
                    <template #icon>
                        <n-icon :component="ThumbsDownRegular" />
                    </template>
                </n-button>
                <span>Chore not done yet!</span>
            </div>
        </template>
    </n-card>
</template>

<script setup lang="ts">
import { defineComponent } from 'vue';
import { NCard, NButton, NIcon } from 'naive-ui';
import type { Chore } from '@/views/ChoresView.vue'
import { ThumbsUpRegular, ThumbsDownRegular } from '@vicons/fa';

export interface Person {
    id: number,
    full_name: string,
    initial_chore: number,
    chore: Chore[],
    first: string,
    last: string,
    profile_pic?: string,
    done_date: string,
    done: boolean
}

defineComponent({
    components: { NCard, NButton, NIcon, ThumbsDownRegular, ThumbsUpRegular }
})

const emit = defineEmits(['toggleChoresDone'])
const props = defineProps<{
    person: Person
}>()

function toggleDone() {
    emit('toggleChoresDone', props.person)
}

</script>

<style scoped>
.card-action {
    display: flex;
    gap: 1rem;
    padding: 0 1rem;
    align-items: center;
    justify-content: space-between;
}

.chore {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.chore-title {
    font-size: 1.5em;
    font-weight: bold;
}
</style>