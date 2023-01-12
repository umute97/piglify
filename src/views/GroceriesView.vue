<template>
    <div>
        <n-layout has-sider sider-placement="right">
            <n-layout-content id="table-container">
                <groceries-table />
            </n-layout-content>
            <n-layout-sider bordered>
                Test
            </n-layout-sider>
        </n-layout>
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider, NDataTable } from 'naive-ui'
import { defineComponent } from 'vue'
import GroceriesTable from '@/components/GroceriesTable.vue'

defineComponent({
    components: { NLayout, NLayoutContent, NLayoutSider, GroceriesTable }
})

</script>

<style scoped>
#table-container {
    padding: 1em;
}
</style>