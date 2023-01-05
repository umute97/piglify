<template>
    <div id="groceries-container">
        <n-layout has-sider sider-placement="right">
            <n-layout-content>
                <n-data-table remote ref="table" :columns="columns" :data="groceries" :loading="loading"
                    :pagination="pagination" @update:sorter="handleSorterChange" @update:filters="handleFiltersChange"
                    @update:page="handlePageChange" />
            </n-layout-content>
            <n-layout-sider bordered>
                Test
            </n-layout-sider>
        </n-layout>
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider, NDataTable } from 'naive-ui'
import { defineComponent, onMounted, ref, type Ref } from 'vue'
import { useUrlStore } from '@/stores/urls'
import axios from 'axios'
import type { TableColumn } from 'naive-ui/es/data-table/src/interface';

defineComponent({
    components: {
        NLayout, NLayoutContent, NLayoutSider,
        NDataTable,
    }
})

interface Grocery {
    id: number,
    date_added: string,
    name: string,
    qty: number,
    location: string | null,
    bought: boolean,
    contact: string,
}

const columns: TableColumn[] = [
    {
        title: "Bought?",
        key: "bought",
        filter: true,
        filterOptions: [
            {
                label: "Yes",
                value: "true",
            },
            {
                label: "No",
                value: "false",
            },
        ],
    },
    {
        title: "Name",
        key: "name",
        filter: true,
        sorter: true,
    },
    {
        title: "Qty",
        key: "qty",
        filter: false,
    },
    {
        title: "Where to buy?",
        key: "location",
        filter: true,
        sorter: true,
    },
    {
        title: "Date added",
        key: "date_added",
        sorter: true,
    },
    {
        title: "Contact",
        key: "contact",
        sorter: true,
    },
]

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