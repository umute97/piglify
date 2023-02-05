<template>
    <div class="wrapper">
        <div class="nav">
            <div class="nav__icon">
                <n-avatar src="https://cdnimg103.lizhi.fm/user/2017/02/04/2583325032200238082_160x160.jpg" />
                <h1>Piglify</h1>
            </div>
            <div class="nav__content">
                Managing the life of 3 little piglets since 2023.
            </div>
            <div class="nav__themeswitcher">
                <n-switch v-model:value="darkTheme" @update:value="setDarkTheme">
                    <template #unchecked-icon>
                        <n-icon :component="MoonRegular"></n-icon>
                    </template>
                    <template #checked-icon>
                        <n-icon :component="Sun"></n-icon>
                    </template>
                </n-switch>
            </div>
        </div>
        <n-layout has-sider position="absolute" style="top: 4rem;">
            <n-layout-sider bordered collapse-mode="width" :collapsed-width=10 show-trigger="arrow-circle">
                <n-menu :options="siderOptions" />
            </n-layout-sider>
            <n-layout-content id="router-view">
                <n-message-provider>
                    <router-view></router-view>
                </n-message-provider>
            </n-layout-content>
        </n-layout>
    </div>
</template>

<script setup lang="ts">
import { defineComponent, h, ref, type Ref } from 'vue'
import { NPageHeader, NButton, NSwitch, NIcon, NLayout, NLayoutContent, NLayoutSider, NMenu, NAvatar, NLayoutFooter, NMessageProvider, type MenuOption } from 'naive-ui'
import { RouterLink, RouterView } from 'vue-router'
import { MoonRegular, Sun } from '@vicons/fa'

defineComponent({
    components: {
        NPageHeader,
        NIcon,
        MoonRegular,
        Sun,
        NButton,
        NLayout,
        NLayoutContent,
        NLayoutSider,
        NLayoutFooter,
        NMenu,
        NAvatar,
        NMessageProvider,

        RouterView,
        RouterLink,
    }
})

const darkTheme: Ref<boolean> = ref(true);
const emit = defineEmits(["setDarkTheme"])

const siderOptions: MenuOption[] = [
    {
        label: () => h(
            RouterLink,
            {
                to: {
                    name: 'chores',
                    path: '/chores',
                }
            },
            { default: () => 'Chores' }
        ),
        key: 'chores',
    },
    {
        label: () => h(
            RouterLink,
            {
                to: {
                    name: 'groceries',
                    path: '/groceries'
                }
            },
            { default: () => 'Groceries' }
        ),
        key: 'groceries',
    },
]

function setDarkTheme() {
    emit("setDarkTheme", darkTheme.value)
}
</script>

<style>
.wrapper {
    --band-height: 3rem;
    --primary-color-300: #CF5CE2FF;
    --primary-color-400: #9b27afFF;
    --primary-color-500: #69007fFF;
    --base-color: #FFFFFFFF;
}

.nav {
    display: flex;
    justify-content: space-between;
    gap: 0.75rem;
    align-items: center;
    padding: 0.5rem 0.5rem;
    height: var(--band-height);
    background-color: var(--primary-color-400);

}
.nav__icon {
    display: flex;
    flex-direction: row;
    align-items: center;
    gap: 0.5rem;
    justify-content: center;
}
.nav__icon > h1 {
    font-size: 1.5rem;
    color: var(--base-color);
}

.nav__content {
    font-size: 0.8rem;
    color: var(--base-color);
    font-weight: 700;
    flex-grow: 1;
}
</style>