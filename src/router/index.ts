import GroceriesViewVue from "@/views/GroceriesView.vue";
import ChoresViewVue from "@/views/ChoresView.vue";
import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "default",
      component: ChoresViewVue,
    },
    {
      path: "/groceries",
      name: "groceries",
      component: GroceriesViewVue,
    },
    {
      path: "/chores",
      name: "chores",
      component: ChoresViewVue,
    },
  ],
});

export default router;
