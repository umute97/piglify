<template>
  <n-config-provider :theme-overrides="theme">
    <AppView @set-dark-theme="setDarkTheme"/>
    <n-global-style />
  </n-config-provider>
</template>

<script setup lang="ts">
import type { GlobalThemeOverrides } from 'naive-ui'
import { NConfigProvider, NGlobalStyle } from 'naive-ui'
import { defineComponent, ref, type Ref } from 'vue'
import AppView from '@/views/AppView.vue'


const darkTheme: GlobalThemeOverrides = {
  common: {
    primaryColor: "#9c27b0FF",
    primaryColorHover: "#d05ce3FF",
    primaryColorPressed: "#6a0080FF",
    primaryColorSuppl: "#6A0080FF",
    popoverColor: "#131417FF",
    textColor3: "rgba(255, 255, 255, 1)",
    textColorBase: "#FFFFFFFF",
    textColor1: "rgba(255, 255, 255, 1)",
    textColor2: "rgba(255, 255, 255, 1)",
    tableColor: "#131417FF",
    cardColor: "#131417FF",
    modalColor: "#131417FF",
    bodyColor: "#131417FF",
    tagColor: "#2F3239FF",
    inputColor: "rgba(23, 17, 26, 1)",
    codeColor: "rgba(88, 37, 116, 1)",
    hoverColor: "rgba(157, 0, 255, 1)",
    tableHeaderColor: "rgba(46, 15, 65, 1)",
    dividerColor: "rgba(118, 4, 180, 1)",
    borderColor: "rgba(118, 4, 180, 1)",
    tabColor: "rgba(30, 30, 35, 1)",
    actionColor: "rgba(38, 13, 44, 1)",
    baseColor: "#131417FF",
    inputColorDisabled: "rgba(123, 123, 123, 1)"
  },
  Skeleton: {
    color: "#85619CFF",
    colorEnd: "#6F2DA2FF"
  },
  Button: {
    textColorPrimary: "#FFF",
  }
}

const lightTheme: GlobalThemeOverrides = {
  common: {
    primaryColor: "#9c27b0",
    baseColor: "#FFFFFFFF",
    primaryColorHover: "#CF5CE2FF",
    primaryColorPressed: "#69007fFF",
  }
}

const theme: Ref<GlobalThemeOverrides> = ref(darkTheme)

function setDarkTheme(state: boolean) {
  theme.value = state? darkTheme : lightTheme;
}

defineComponent({
  components: {
    NConfigProvider,
    AppView,
  },
})
</script>