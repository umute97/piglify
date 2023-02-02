import { defineStore } from "pinia";

export const useUrlStore = defineStore({
    id: 'url',
    state: () => {
        return {
            backendIP: import.meta.env.VITE_BACKEND_BASE_URL,
        }
    },
})