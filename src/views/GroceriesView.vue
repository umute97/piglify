<template>
    <div class="container">
        <div class="actions">
            <n-button @click="showModal = true" size="large" round type="primary" class="grocery-button">
                <template #icon>
                    <n-icon :component="CartPlus"></n-icon>
                </template>
                Add item
            </n-button>
            <n-button @click="showTutorial = true" size="medium" circle type="default" class="question-button">
                <template #icon>
                    <n-icon :component="Question"></n-icon>
                </template>
            </n-button>
        </div>
        <div class="grocery-table-wrapper">
            <groceries-table ref="groceryTable" />
        </div>
        <n-modal v-model:show="showModal" preset="dialog" title="Add Grocery">
            <n-message-provider>
                <groceries-form @close-and-refresh-groceries="closeFormAndRefreshTable" />
            </n-message-provider>
        </n-modal>
        <n-modal v-model:show="showTutorial" preset="dialog" title="Tutorial">
            <n-message-provider>
                <groceries-tutorial @close-tutorial-dialog="closeTutorialDialog" />
            </n-message-provider>
        </n-modal>
    </div>
</template>

<script setup lang="ts">
import { NLayout, NLayoutContent, NLayoutSider, NButton, NIcon, NModal, NMessageProvider, useMessage } from 'naive-ui'
import { defineComponent, ref } from 'vue'
import { CartPlus, Question } from '@vicons/fa'
import GroceriesTable from '@/components/GroceriesTable.vue'
import GroceriesForm from '@/components/GroceriesForm.vue'
import GroceriesTutorial from '@/components/GroceriesTutorial.vue'

defineComponent({
    components: { NLayout, NLayoutContent, NLayoutSider, NButton, NModal, GroceriesTable, GroceriesTutorial, GroceriesForm, NIcon, CartPlus, Question }
})

const showModal = ref(false)
const showTutorial = ref(false)
const message = useMessage()
const groceryTable = ref()

function closeFormAndRefreshTable() {
    showModal.value = showModal.value ? !showModal.value : showModal.value
    message.success('Successfully added grocery!')
    groceryTable.value.refreshTable()
}

function closeTutorialDialog() {
    showTutorial.value = showTutorial.value ? !showTutorial.value : showTutorial.value
}
</script>

<style scoped>
.container {
    padding: 1rem;
}

.actions {
    display: flex;
    justify-content: end;
    margin-bottom: 1rem;
    gap: 1rem;
}

.grocery-table-wrapper {
    overflow: hidden;
}

@media only screen and (max-width: 768px) {
    .grocery-button {
        flex-grow: 1;
    }
}
</style>