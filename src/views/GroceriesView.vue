<template>
    <div>
        <n-layout has-sider sider-placement="right">
            <n-layout-content class="container">
                <n-button @click="showModal = true" size="large" round type="primary" class="grocery-button">
                    <template #icon>
                        <n-icon :component="CartPlus"></n-icon>
                    </template>
                    Add item
                </n-button>
                <groceries-table ref="groceryTable"/>
            </n-layout-content>
            <n-layout-sider bordered>
                Test
            </n-layout-sider>
        </n-layout>
        <n-modal v-model:show="showModal" preset="dialog" title="Add Grocery">
            <n-message-provider>
                <groceries-form @close-and-refresh-groceries="closeFormAndRefreshTable"/>
            </n-message-provider>
        </n-modal>
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider, NButton, NIcon, NModal, NMessageProvider, useMessage } from 'naive-ui'
import { defineComponent, ref } from 'vue'
import { CartPlus } from '@vicons/fa'
import GroceriesTable from '@/components/GroceriesTable.vue'
import GroceriesForm from '@/components/GroceriesForm.vue'

defineComponent({
    components: { NLayout, NLayoutContent, NLayoutSider, NButton, NModal, GroceriesTable, GroceriesForm, NIcon, CartPlus }
})

const showModal = ref(false)
const message = useMessage()
const groceryTable = ref()

function closeFormAndRefreshTable() {
    showModal.value = showModal.value ? !showModal.value : showModal.value
    message.success('Successfully added grocery!')
    groceryTable.value.refreshTable()
}
</script>

<style scoped>
.container {
    margin: 0 1em;
    text-align: end;
}

.grocery-button {
    margin-bottom: 1em;
}
</style>