# CLI 使用

本模板提供了 Pixi 任务系统来管理常用命令。

## 查看可用任务

```bash
pixi task list
```

这会显示项目中配置的所有可用任务。

## 常用任务

### 开发任务

```bash
# 运行测试
pixi run test

# 运行特定测试文件
pixi run test tests/test_example.py

# 多版本测试
pixi run test-312  # Python 3.12
pixi run test-313  # Python 3.13
pixi run test-314  # Python 3.14
```

### 代码质量检查

```bash
# 代码格式检查
pixi run lint

# 类型检查
pixi run typecheck

# 安全检查
pixi run security

# 运行所有检查
pixi run check
```

### 代码格式化

```bash
# 自动格式化代码
pixi run format

# 修复所有可修复的问题
pixi run fix
```

### 构建和发布

```bash
# 构建项目
pixi run build

# 清理构建文件
pixi run clean
```

### 文档

```bash
# 构建文档
pixi run -e docs docs-build

# 启动文档服务器
pixi run -e docs docs-serve

# 在浏览器中查看文档
# 访问 http://127.0.0.1:8000
```

## 添加自定义任务

在 `pixi.toml` 中的 `[tasks]` 部分添加你的任务：

```toml
[tasks]
your-task = "your-command"
```

示例：

```toml
[tasks]
# 运行你的主程序
run = "python -m your_package_name"

# 自定义测试
test-verbose = "pytest -v"

# 数据处理
process-data = "python scripts/process.py"
```

## 使用 Python 包

在你的项目中导入和使用你的代码：

```python
# 从 src 目录导入
from src.your_module import your_function

# 使用你的代码
result = your_function()
```

## 环境管理

```bash
# 安装依赖
pixi install

# 添加新依赖
pixi add package-name

# 添加开发依赖
pixi add --feature dev package-name

# 更新依赖
pixi update

# 查看环境信息
pixi info
```
