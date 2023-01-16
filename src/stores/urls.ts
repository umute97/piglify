import { defineStore } from "pinia";

export const useUrlStore = defineStore({
    id: 'url',
    state: () => {
        return {
            backendIP: 'http://localhost:8000/piglify',
        }
    },
})