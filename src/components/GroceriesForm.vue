<template>
    <div>
        <n-form ref="formRef" :model="formValue" label-placement="left" size="medium" label-width="auto" :rules="rules">
            <n-form-item label="Name" path="name">
                <n-input v-model:value="formValue.name" />
            </n-form-item>
            <n-form-item label="Quantity" path="qty">
                <n-input-number v-model:value="formValue.qty" />
            </n-form-item>
            <n-form-item label="Where to buy?" path="location">
                <n-input v-model:value="formValue.location" />
            </n-form-item>
            <n-form-item label="Contact" path="contact">
                <n-select v-model:value="contactRef" :options="contactOptions" :render-label="renderLabel"
                    size="medium" />
            </n-form-item>
        </n-form>
        <n-button class="submit-button" @click="validateAndTrySubmit">Submit</n-button>
    </div>
</template>

<script setup lang="ts">
import { NForm, NFormItem, NInput, NInputNumber, NSelect, NAvatar, NButton, useMessage, type FormInst, type SelectRenderLabel, NA, NText, type FormRules, type FormItemRule } from 'naive-ui'
import { defineComponent, h, onMounted, reactive, ref, type Ref } from 'vue'
import axios from 'axios'
import { useUrlStore } from '@/stores/urls'
import type { SelectMixedOption } from 'naive-ui/es/select/src/interface'

// INTERFACES START -------------
interface GroceryEntry {
    name: string | null,
    qty: number | null,
    location: string | null,
    contact: string | null,
}

interface UserResult {
    id: number,
    first: string,
    last: string | null,
    full_name: string,
    profile_pic: string,
}
// INTERFACES END -------------
// VUE ECOSYSTEM + APIs START -------------
defineComponent({
    components: { NForm, NFormItem, NInput, NSelect, NAvatar, NInputNumber, NButton, }
})

const urlStore = useUrlStore()
const message = useMessage()
const emit = defineEmits(['closeAndRefreshGroceries'])
// VUE ECOSYSTEM + APIs END -------------
// REFS DEFINITIONS ----------------
const formRef: Ref<FormInst | null> = ref(null)
const formValue: GroceryEntry = reactive({
    'name': null,
    'qty': null,
    'location': null,
    'contact': null,
})

const contactRef: Ref<string | null> = ref(null)
const contactOptions: Ref<SelectMixedOption[]> = ref([])
// REFS DEFINITIONS ----------------

const renderLabel: SelectRenderLabel = (option) => {
    return h(
        'div',
        {
            style: {
                display: 'flex',
                alignItems: 'center'
            }
        },
        [
            h(NAvatar, {
                src: option.profile_pic as string,
                round: true,
                size: 'small'
            }),
            h(
                'div',
                {
                    style: {
                        marginLeft: '12px',
                        padding: '4px 0'
                    }
                },
                [
                    h('div', null, [option.label as string]),
                ]
            )
        ]
    )
}

const rules: FormRules = {
    name: [
        {
            required: true,
            message: 'Grocery name is required.',
            trigger: ['input', 'blur']
        }
    ],
    qty: [
        {
            required: true,
            validator(_rule: FormItemRule, value: number) {
                if (value === 0) {
                    return new Error('Quantity can\'t be 0.')
                }
                if (!value) {
                    return new Error('Quantity is required.')
                }
                return true
            },
            trigger: ['input', 'blur']
        }
    ],
    location: [
        {
            required: false,
        }
    ],
    contact: [
        {
            required: true,
            validator(_rule: FormItemRule, _value: null) {
                if (!contactRef.value) {
                    return Object.freeze(new Error('Contact is required.'))
                }
                return true
            },
            trigger: ['input', 'blur']
        }
    ],
}

function validateAndTrySubmit(e: MouseEvent) {
    e.preventDefault()
    formRef.value?.validate(async (errors) => {
        if (!errors) {
            formValue.contact = contactRef.value;
            console.log("formValue", formValue)
            await axios.post(`${urlStore.backendIP}/groceries/`, formValue).then((response) => {
                if (response.status === 201) {
                    message.success('Added grocery!')
                    emit('closeAndRefreshGroceries')
                } else {
                    message.error(response.statusText)
                }
            })

        } else {
            message.error('Grocery invalid and could not be added. Please try again.')
        }
    })
}

onMounted(async () => {
    await axios.get(`${urlStore.backendIP}/users`).then((response) => {
        console.log(response.data.results)
        contactOptions.value = response.data.results.map((result: UserResult) => ({
            'label': result.full_name,
            'value': result.id,
            'profile_pic': result.profile_pic,
        }))
    })
})

</script>

<style scoped>
.submit-button {
    float: right;
}
</style>