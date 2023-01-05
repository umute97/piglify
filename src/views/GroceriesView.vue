<template>
    <div id="groceries-container">
        <n-layout has-sider sider-placement="right">
            <n-layout-content>
                <li v-for="grocery in groceries" :key="grocery.id">
                    {{ grocery.name }} (x{{ grocery.qty }}): location: {{ grocery.location }}, {{ grocery.bought }}
                </li>
            </n-layout-content>
            <n-layout-sider bordered>
                Test
            </n-layout-sider>
        </n-layout>
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider } from 'naive-ui'
import { onMounted, ref, type Ref } from 'vue'
import { useUrlStore } from '@/stores/urls'
import axios from 'axios'

interface Grocery {
    id: number,
    date_added: string,
    name: string,
    qty: number,
    location: string | null,
    bought: boolean,
}

const urlStore = useUrlStore()
let groceries: Ref<Grocery[]> = ref([])

onMounted(async () => {
    await axios.get(`${urlStore.backendIP}/groceries?format=json`).then((response) => {
        groceries.value = response.data.results
    })
})

</script>

<style scoped>

</style>