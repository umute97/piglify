<template>
    <n-data-table remote ref="table" :columns="columns" :data="groceries" :loading="loading" :pagination="pagination"
        @update:sorter="handleSorterChange" @update:page="handlePageChange" />
</template>

<script setup lang="ts">
import { useUrlStore } from '@/stores/urls'
import axios from 'axios'
import { NDataTable, type DataTableColumn, type DataTableSortState } from 'naive-ui';
import type { SortOrder } from 'naive-ui/es/data-table/src/interface';
import { defineComponent, onMounted, reactive, ref, type Ref } from 'vue';

defineComponent({
    components: { NDataTable }
})

interface Grocery {
    id: number,
    date_added: string,
    name: string,
    qty: number,
    location: string | null,
    bought: boolean,
    contact: number,
    contact_name: string
}

interface QueryResponse {
    pageCount: number,
    total: number,
    data: Grocery[],
}

const urlStore = useUrlStore()

const groceries: Ref<Grocery[]> = ref([])
const dateColumnTemp: DataTableColumn = {
    title: "Date added",
    key: "date_added",
    sorter: true,
    sortOrder: "descend",
}
const dateColumn = reactive(dateColumnTemp)
const columns = reactive([
    {
        title: "Bought?",
        key: "bought",
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
        key: "contact_name",
    },
])
const pagination = reactive({
    page: 1,
    pageCount: 1,
    pageSize: 10,
})
const loading = ref(true)

function query(page: number, pageSize = 10, order: SortOrder = 'descend'): Promise<QueryResponse> {
    return new Promise(async (resolve) => {
        let data: Grocery[] = []
        let total = 0
        const offset = (page - 1) * pageSize
        let url = `${urlStore.backendIP}/groceries?format=json&limit=${pageSize}&offset=${offset}&ordering=`

        if (order === 'descend') {
            url += '-'
        }
        url += 'date_added'

        await axios.get(url).then((response) => {
            data = response.data.results
            total = response.data.count
        })

        const pageCount = Math.ceil(total / pageSize)
        resolve({ pageCount, data, total })
    })
}

function handlePageChange(currentPage: number) {
    if (!loading.value) {
        loading.value = true;
        query(currentPage, pagination.pageSize, dateColumn.sortOrder)
            .then((response: QueryResponse) => {
                groceries.value = response.data
                pagination.page = currentPage
                pagination.pageCount = response.pageCount
                loading.value = false
            })
    }
}

function handleSorterChange(sorter: DataTableSortState) {
    if (!sorter || sorter.columnKey === 'date_added') {
        if (!loading.value) {
            loading.value = true
            query(pagination.page, pagination.pageSize, !sorter ? false : sorter.order)
                .then((response: QueryResponse) => {
                    dateColumn.sortOrder = !sorter ? false : sorter.order
                    groceries.value = response.data
                    pagination.pageCount = response.pageCount
                    loading.value = false
                })
        }
    }
}

onMounted(async () => {
    query(pagination.page, pagination.pageSize, dateColumn.sortOrder)
        .then((response: QueryResponse) => {
            groceries.value = response.data
            pagination.pageCount = response.pageCount
            loading.value = false
        })
})


</script>

<style scoped>

</style>