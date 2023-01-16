<template>
    <n-form>
        <n-form-item>
            <n-input v-model:value="formValue.name" placeholder="Name" />
        </n-form-item>
        <n-form-item>
            <n-input v-model:value:number="formValue.qty" placeholder="Qty." />
        </n-form-item>
        <n-form-item>
            <n-input v-model:value="formValue.location" placeholder="Where to buy?" />
        </n-form-item>
        <n-form-item>
            <n-select v-model:value="contactRef" :options="contactOptions" />
        </n-form-item>
    </n-form>
</template>

<script setup lang="ts">
import { NForm, NFormItem, NInput, NButton, NSelect, type FormInst } from 'naive-ui'
import { defineComponent, onMounted, reactive, ref, type Ref } from 'vue'
import axios from 'axios'
import { useUrlStore } from '@/stores/urls'
import type { SelectMixedOption } from 'naive-ui/es/select/src/interface'

interface GroceryEntry {
    name: string | null,
    qty: number | null,
    location: string | null,
    contact: string | null,
}

interface UserResult {
    first: string,
    last: string | null,
    full_name: string,
    profile_pic: ImageBitmap,
}

defineComponent({
    components: { NForm, NFormItem, NInput, NSelect }
})

const urlStore = useUrlStore()

const formRef: Ref<FormInst | null> = ref(null)
const formValue: GroceryEntry = reactive({
    'name': null,
    'qty': null,
    'location': null,
    'contact': null,
})

const contactRef: Ref<string | null> = ref(null)
let contactOptions: Ref<SelectMixedOption[]> = ref([])

onMounted(async () => {
    await axios.get(`${urlStore.backendIP}/users`).then((response) => {
        console.log(response.data.results)
        contactOptions.value = response.data.results.map((result: UserResult) => ({
            'label': result.full_name,
            'value': result.first,
        }))
    })
})

</script>

<style scoped>

</style>