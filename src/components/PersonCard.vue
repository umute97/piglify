<template>
    <n-card :title="person.full_name" hoverable>
        <template #cover>
            <img loading="lazy" :src="person.profile_pic" :alt="`Cover image of ${ person.full_name }`" />

        </template>

        <div class="chore">
            <n-collapse arrow-placement="right">
                <n-collapse-item>
                    <template #header>
                        <span class="chore-title">{{ person.chore[0].name }}</span>
                    </template>
                    <div v-html="person.chore[0].desc"></div>
                </n-collapse-item>
            </n-collapse>
            <div class="next-up">
                <label>Next up</label>
                <span>{{ person.next_chore[0].name }}</span>
            </div>
        </div>

        <template #action>
            <div class="card-action" v-if="person.done">
                <n-button type="success" @click="toggleDone" class="card-action-thumb">
                    <template #icon>
                        <n-icon :component="ThumbsUpRegular" />
                    </template>
                </n-button>
                <span>Chore was done on {{ person.done_date }}</span>
            </div>
            <div class="card-action" v-else>
                <n-button type="error" @click="toggleDone" class="card-action-thumb">
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
import { NCard, NButton, NIcon, NCollapse, NCollapseItem } from 'naive-ui';
import type { Chore } from '@/views/ChoresView.vue'
import { ThumbsUpRegular, ThumbsDownRegular } from '@vicons/fa';

export interface Person {
    id: number,
    full_name: string,
    initial_chore: number,
    chore: Chore[],
    next_chore: Chore[],
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

.next-up {
    position: relative;
    border: 2px purple solid; 
    border-radius: 0.5rem;
    padding: 1.5rem 1rem 0.5rem 1rem;
    margin-top: 1rem;
    font-size: 1.1rem;
}

.next-up>label {
    position: absolute;
    border-radius: 0.5rem;
    padding: 0 0.5rem;
    top: -0.5rem;
    left: -1rem;
    background: var(--primary-color-400);
}

.chore-title {
    font-size: 1.5rem;
    font-weight: bold;
}

@media only screen and (max-width: 768px) {
    .card-action-thumb {
        flex-grow: 1;
    }
}
</style>