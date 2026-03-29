# 纯 Python 实现更新日志

## 主要变更

### 移除依赖
- ❌ 移除 `PyExecJS` 依赖
- ❌ 移除 Node.js 环境要求
- ❌ 删除所有 JavaScript 文件（hexin-v.js, hexin-v.bundle.js, package.json, webpack.config.js）

### 新增功能
- ✅ 新增 `hexin_v_pure.py` - 纯 Python 实现的 token 生成器
- ✅ 完全使用 Python 标准库和现有依赖实现 token 生成
- ✅ 保持与原有 API 完全兼容

### 优势
1. **无需 Node.js**：不再需要安装 Node.js 环境
2. **更简单的部署**：只需 Python 环境即可运行
3. **更好的跨平台支持**：避免了 Node.js 在某些环境下的兼容性问题
4. **更快的启动速度**：不需要启动 Node.js 子进程
5. **更容易调试**：纯 Python 代码更容易理解和调试

### 技术实现
- 使用 Python 重新实现了原 JS 的 token 生成算法
- 模拟浏览器特征和用户行为
- 使用标准库的 base64、hashlib、random 等模块
- 保持了原有的加密和编码逻辑

### 测试
运行 `python test_pure_python.py` 验证功能正常。

## 使用方法

使用方法完全不变：

```python
import pywencai

res = pywencai.get(query='退市股票', cookie='your_cookie')
print(res)
```

不再需要安装 Node.js！
