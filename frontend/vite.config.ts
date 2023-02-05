import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import Components from 'unplugin-vue-components/vite';
import { AntDesignVueResolver } from 'unplugin-vue-components/resolvers';
import OptimizationPersist from "vite-plugin-optimize-persist";
import PkgConfig from "vite-plugin-package-config";

import path from "path";
import themePreprocessorPlugin from "@zougt/vite-plugin-theme-preprocessor";

// https://vitejs.dev/config/
export default defineConfig({
  /* ... */
  plugins: [
    Components({
      resolvers: [AntDesignVueResolver()],
    }),
    vue(),
    PkgConfig(),
    OptimizationPersist(),
  ],
  optimizeDeps: {
    include: ["ant-design-vue","ant-design-vue/dist/antd.css","@ant-design/icons-vue"]
  },
  server: {
    proxy:{
			'/api': {
				target: 'http://localhost:8080/api',
				changeOrigin: true,
				rewrite: path => path.replace(/^\/api/, '')
			}
		} 
  },
  css: {
    preprocessorOptions: {
      less: {
        javascriptEnabled: true
      }
    }
  },
  build: {
    sourcemap: false,
    minify: 'terser',
    chunkSizeWarningLimit: 1500,
    terserOptions: {
      compress: {
        drop_console: true,
        drop_debugger: true
      }
    },
    commonjsOptions: {
      include: [/linked-dep/, /node_modules/]
    },
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes('node_modules')) {
            return id
              .toString()
              .split('node_modules/')[1]
              .split('/')[0]
              .toString();
          }
        },
        chunkFileNames: (chunkInfo) => {
          const facadeModuleId = chunkInfo.facadeModuleId
            ? chunkInfo.facadeModuleId.split('/')
            : [];
          const fileName =
            facadeModuleId[facadeModuleId.length - 2] || '[name]';
          return `js/${fileName}/[name].[hash].js`;
        }
      }
    }
  }
})
