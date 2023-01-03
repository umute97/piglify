<template>
  <n-config-provider :theme-overrides="theme">
    <AppView />
    <n-global-style />
  </n-config-provider>
</template>

<script setup lang="ts">
import type { GlobalThemeOverrides } from 'naive-ui'
import { NConfigProvider, NGlobalStyle } from 'naive-ui'
import { defineComponent } from 'vue'
import AppView from '@/views/AppView.vue'

const darkTheme: GlobalThemeOverrides = {
  common: {
    primaryColor: "#ec407a",
  },
  Button: {
    textColor: "#ec407a",
  },
  //...
}

const lightTheme: GlobalThemeOverrides = {
  common: {
    primaryColor: "#000",
  },
  Button: {
    textColor: "#000",
  },
  //...
}

const theme = lightTheme;

defineComponent({
  components: {
    NConfigProvider,
    AppView,
  },
})
</script>