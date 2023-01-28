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
    primaryColor: "#9b27afFF",
    baseColor: "#FFFFFFFF",
    primaryColorHover: "#CF5CE2FF",
    primaryColorPressed: "#69007fFF",
    fontSize: "16px",
    fontSizeMedium: "14px"
  }
}

const theme = lightTheme;

defineComponent({
  components: {
    NConfigProvider,
    AppView,
  },
})
</script>