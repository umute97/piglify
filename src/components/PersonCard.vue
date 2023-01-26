<template>
    <n-card :title="person.full_name">
        <template #cover>
            <img :src="person.profile_pic" alt="A cool person." />
        </template>
        <template #action>
            <n-button type="error" @click="toggleDone">
                <template #icon>
                    <n-icon v-if="person.done" :component="ThumbsUpRegular" />
                    <n-icon v-else :component="ThumbsDownRegular" />
                </template>
                Done
            </n-button>
        </template>
    </n-card>
</template>

<script setup lang="ts">
import { defineComponent } from 'vue';
import { NCard, NButton, NIcon } from 'naive-ui';
import { ThumbsUpRegular, ThumbsDownRegular } from '@vicons/fa';

export interface Person {
    id: number,
    full_name: string,
    first: string,
    last: string,
    profile_pic?: string,
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
    emit('toggleChoresDone', props.person.done)
}
</script>

<style scoped>

</style>