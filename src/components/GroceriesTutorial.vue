<template>
    <div>
        <p>
            Welcome to the groceries tab! This is where all our needs will be recorded for one of us to pick
            up at a time of convenience.
        </p>
        <p>
            To add an entry
        </p>
        <ul>
            <li>Click on "Add item"</li>
            <li>Enter
                <ol>
                    <li>the name of the item</li>
                    <li>the desired quantity (if you need to provide weights or volumes, please write one
                        unit in the name field like "Salt (100g)")</li>
                    <li>(if you know where to best get it) the location to buy the item from</li>
                    <li>the person responsible for <b>the entry of this item</b> (namely: you)</li>
                </ol>
            </li>
        </ul>
    </div>
    <n-button @click="closeTutorialDialog" type="primary">Got it.</n-button>
</template>

<script setup lang="ts">
import { NButton } from 'naive-ui'

const emit = defineEmits(['closeTutorialDialog']) 

function closeTutorialDialog() {
    emit('closeTutorialDialog')
}
</script>

<style scoped>
.submit-button {
    float: right;
}
</style>