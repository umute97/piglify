<template>
    <n-card>
        <template #cover>
            <img :src="profilePic" alt="A cool person." />
        </template>
    </n-card>
</template>

<script setup lang="ts">
import { defineComponent } from 'vue';
import { NCard } from 'naive-ui';

defineComponent({
    components: { NCard, }
})

defineProps(['profilePic'])
</script>

<style scoped>

</style>