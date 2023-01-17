<template>
    <div>
        <n-layout has-sider sider-placement="right">
            <n-layout-content class="container">
                <n-button @click="showGroceriesForm" size="large" round type="primary" class="grocery-button">
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
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider, NButton, NIcon } from 'naive-ui'
import { defineComponent } from 'vue'
import { CartPlus } from '@vicons/fa'
import GroceriesTable from '@/components/GroceriesTable.vue'
import GroceriesForm from '@/components/GroceriesForm.vue'

defineComponent({
    components: { NLayout, NLayoutContent, NLayoutSider, NButton, GroceriesTable, GroceriesForm, NIcon, CartPlus }
})

function showGroceriesForm(event: MouseEvent) {
    console.log("Grocery form should show up now!")
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