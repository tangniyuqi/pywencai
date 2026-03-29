# 迁移指南：从 Node.js 版本到纯 Python 版本

## 概述

pywencai 已经完全移除了对 Node.js 的依赖，现在是纯 Python 实现。

## 对用户的影响

### ✅ 好消息

1. **无需更改代码**：API 完全兼容，现有代码无需修改
2. **无需 Node.js**：不再需要安装 Node.js 环境
3. **更简单的部署**：只需 Python 环境
4. **更快的启动**：不需要启动 Node.js 子进程

### 升级步骤

1. 卸载旧版本（可选）：
```bash
pip uninstall pywencai
```

2. 安装新版本：
```bash
pip install pywencai --upgrade
```

3. 如果之前安装了 Node.js 仅用于 pywencai，现在可以卸载它了

### 代码示例

使用方法完全不变：

```python
import pywencai

# 之前的代码
res = pywencai.get(query='昨日涨幅', cookie='your_cookie')

# 现在的代码（完全相同）
res = pywencai.get(query='昨日涨幅', cookie='your_cookie')
```

## 技术细节

### 移除的依赖
- PyExecJS
- Node.js 环境

### 新增的实现
- `hexin_v_pure.py`：纯 Python 的 token 生成器

### 保留的依赖
- requests
- pandas
- fake-useragent
- pydash
- ipykernel

## 常见问题

### Q: 我需要修改代码吗？
A: 不需要，API 完全兼容。

### Q: 性能会受影响吗？
A: 不会，实际上启动速度更快了，因为不需要启动 Node.js 子进程。

### Q: 如果遇到问题怎么办？
A: 请在 GitHub 上提交 issue，并提供详细的错误信息。

## 反馈

如有任何问题或建议，欢迎提交 issue 或 PR。
