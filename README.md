# 聚曜 · 手势驱动的实时 3D 粒子交互系统

通过摄像头识别手势，实时操控三维粒子星云。

## 功能

- **手势识别**：接入 MediaPipe Hands 提取手部关键点，把手掌旋转、握拳、张掌映射为轨道相机的旋转与推拉
- **粒子渲染**：Three.js 构建 8000 粒子星球与 2 × 4000 粒子光环，叠加辉光效果
- **离线运行**：Three.js、手势模型与 WASM 资源全部放在 `vendor/` 本地目录
- **摄像头生命周期管理**：显式授权、失败提示与重试、离开页面时释放摄像头

## 运行

Windows 双击 `启动游戏.cmd`，或运行：

```bash
python start_game.py
```

脚本会在本机启动服务（自动探测并复用 8000–8020 端口）并打开浏览器。摄像头需要通过 localhost / HTTPS 访问，不能直接双击 HTML 打开。

## 技术栈

JavaScript · Three.js · MediaPipe Hands · WebAssembly · Python

第三方组件（Three.js、MediaPipe）遵循各自的开源许可证。
