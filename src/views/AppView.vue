<template>
    <div id="content">
        <n-page-header class="nav" title="Piglify" subtitle="Managing the life of 3 little piglets since 2023.">
            <template #extra>
                <n-space justify="space-between">
                    <n-switch>
                        <template #icon>
                            <n-icon :component="MoonRegular"></n-icon>
                        </template>
                    </n-switch>
                </n-space>
            </template>
            <template #avatar>
                <n-avatar src="https://cdnimg103.lizhi.fm/user/2017/02/04/2583325032200238082_160x160.jpg" />
            </template>
        </n-page-header>
        <n-layout has-sider>
            <n-layout-sider bordered>
                <n-menu :options="siderOptions" />
            </n-layout-sider>
            <n-layout-content>
                <router-view></router-view>
            </n-layout-content>
        </n-layout>
        <n-page-header class="footer">
            Made with love in Waldstadt, ver. {{ version }}
        </n-page-header>
    </div>
</template>

<script setup lang="ts">
import { defineComponent, h } from 'vue'
import { NPageHeader, NSpace, NButton, NSwitch, NIcon, NLayout, NLayoutContent, NLayoutSider, NMenu, NAvatar, NLayoutFooter, type MenuOption } from 'naive-ui'
import { RouterLink, RouterView } from 'vue-router'
import { MoonRegular } from '@vicons/fa'
import { version } from '@/../package.json'

defineComponent({
    components: {
        NPageHeader,
        NIcon,
        MoonRegular,
        NButton,
        NLayout,
        NLayoutContent,
        NLayoutSider,
        NLayoutFooter,
        NMenu,
        NAvatar,

        RouterView,
        RouterLink,
    }
})

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
            { default: () => 'Default chores'}
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
            { default: () => 'Default groceries'}
        ),
        key: 'groceries',
    },
]
</script>

<style scoped>
.nav {
    padding: 10px 15px;
}

.footer {
    height: 50px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid lightgrey;
}

#content {
    display: grid;
    grid-template-rows: auto 1fr auto;
    min-height: 100vh;
    margin: 0;
    font-size: 1.5em;
}
</style>