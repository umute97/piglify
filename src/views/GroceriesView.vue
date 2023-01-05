<template>
    <div id="groceries-container">
        <n-layout has-sider sider-placement="right">
            <n-layout-content>
                <n-data-table remote ref="table" :columns="columns" :data="groceries" :loading="loading"
                    :pagination="pagination" @update:sorter="handleSorterChange" @update:page="handlePageChange" />
            </n-layout-content>
            <n-layout-sider bordered>
                Test
            </n-layout-sider>
        </n-layout>
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider, NDataTable } from 'naive-ui'
import { defineComponent, onMounted, reactive, ref, type Ref } from 'vue'
import { useUrlStore } from '@/stores/urls'
import axios from 'axios'
import type { FilterOptionValue, TableColumn } from 'naive-ui/es/data-table/src/interface';

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
const dateColumn = {
    title: "Date added",
    key: "date_added",
    sorter: true,
}

const columns: TableColumn[] = [
    {
        title: "Bought?",
        key: "bought",
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
    },
    {
        title: "Qty",
        key: "qty",
    },
    {
        title: "Where to buy?",
        key: "location",
    },
    dateColumn,
    {
        title: "Contact",
        key: "contact",
    },
]

const urlStore = useUrlStore()

let groceries: Ref<Grocery[]> = ref([])
const dateColumnReactive = reactive(dateColumn)
const pagination = reactive({
    page: 1,
    pageCount: 1,
    pageSize: 10,
})

function query(page: number, pageSize = 10, order = 'ascend', filterValues: FilterOptionValue[] = []) {
    return new Promise(async (resolve) => {
        let data: Grocery[] = []
        const offset = (page - 1) * pageSize
        let url = `${urlStore.backendIP}/groceries?format=json&limit=${pageSize}&offset=${offset}`

        await axios.get(url).then((response) => {
            data = response.data.results
        })

        const orderedData = order === 'descend' ? data.reverse() : data
        // const filteredData = filterValues.length
        //     ? orderedData.filter((row) => filterValues.includes(row.column2))
        //     : orderedData

        const total = data.length
        const pageCount = Math.ceil(total / pageSize)
        resolve({ pageCount, data, total })
    })
}

onMounted(async () => {
    query(pagination.page, pagination.pageSize, dateColumnReactive.sortOrder,)
})

</script>

<style scoped>

</style>