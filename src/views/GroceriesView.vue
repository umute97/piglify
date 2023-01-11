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

interface QueryResponse {
    pageCount: number,
    total: number,
    data: Grocery[],
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
let loading = ref(true)
const pagination = reactive({
    page: 1,
    pageCount: 1,
    pageSize: 1,
})

function query(page: number, pageSize = 10, order = true): Promise<QueryResponse> {
    return new Promise(async (resolve) => {
        let data: Grocery[] = []
        let total = 0
        const offset = (page - 1) * pageSize
        let url = `${urlStore.backendIP}/groceries?format=json&limit=${pageSize}&offset=${offset}`

        await axios.get(url).then((response) => {
            data = response.data.results
            total = response.data.count
        })

        const orderedData = order ? data.reverse() : data
        // const filteredData = filterValues.length
        //     ? orderedData.filter((row) => filterValues.includes(row.column2))
        //     : orderedData

        const pageCount = Math.ceil(total / pageSize)
        resolve({ pageCount, data: orderedData, total })
    })
}

function handlePageChange(currentPage: number) {
    if (!loading.value) {
        loading.value = true;
        query(currentPage, pagination.pageSize, dateColumnReactive.sorter)
            .then((response: QueryResponse) => {
                groceries.value = response.data
                pagination.page = currentPage
                pagination.pageCount = response.pageCount
                loading.value = false
            })
    }
}

onMounted(async () => {
    query(pagination.page, pagination.pageSize, dateColumnReactive.sorter)
        .then((response: QueryResponse) => {
            groceries.value = response.data
            pagination.pageCount = response.pageCount
            loading.value = false
        })
})

</script>

<style scoped>

</style>