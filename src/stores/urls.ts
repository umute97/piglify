import { defineStore } from "pinia";
import backendIP from "public/ips.json";

export const useUrlStore = defineStore({
    id: 'url',
    state: () => {
        return {
            backendIP
        }
    },
})