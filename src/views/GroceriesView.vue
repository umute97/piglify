<template>
    <div>
        <n-layout has-sider sider-placement="right">
            <n-layout-content class="container">
                <n-button @click="showModal=true" size="large" round type="primary" class="grocery-button">
                    <template #icon>
                        <n-icon :component="CartPlus"></n-icon>
                    </template>
                    Add item
                </n-button>
                <groceries-table />
            </n-layout-content>
            <n-layout-sider bordered>
                Test
            </n-layout-sider>
        </n-layout>
        <n-modal v-model:show="showModal" preset="dialog" title="Add Grocery">
            <template #action>
                <n-button type="primary" @click="submit">Submit</n-button>
            </template>
            <groceries-form />
        </n-modal>
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider, NButton, NIcon, NModal } from 'naive-ui'
import { defineComponent, ref } from 'vue'
import { CartPlus } from '@vicons/fa'
import GroceriesTable from '@/components/GroceriesTable.vue'
import GroceriesForm from '@/components/GroceriesForm.vue'

defineComponent({
    components: { NLayout, NLayoutContent, NLayoutSider, NButton, NModal, GroceriesTable, GroceriesForm, NIcon, CartPlus }
})

const showModal = ref(false);

function submit(e: MouseEvent) {
    console.log("Clicked submit!")
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