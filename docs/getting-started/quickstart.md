# 快速入门

跟随本指南，5 分钟内开始使用模板开发你的项目！

## 前置条件

确保你已经：

- ✅ [安装了 Pixi](installation.md)
- ✅ 克隆或创建了项目
- ✅ 运行了初始化脚本
- ✅ 安装了开发环境

## 基本工作流程

### 1. 编写代码

在 `src/` 目录下编写你的代码：

```python title="src/__init__.py"
"""我的项目包。"""

def hello(name: str) -> str:
    """问候函数。

    Args:
        name: 要问候的名字

    Returns:
        问候语
    """
    return f"Hello, {name}!"
```

### 2. 编写测试

在 `tests/` 目录下编写测试：

```python title="tests/test_example.py"
from src import hello

def test_hello():
    """测试 hello 函数。"""
    assert hello("World") == "Hello, World!"
    assert hello("Python") == "Hello, Python!"
```

### 3. 运行检查

```bash
# 快速检查（格式化 + Lint + 类型检查）
pixi run check

# 运行测试
pixi run test

# 完整检查（包括安全扫描）
pixi run check-all
```

### 4. 提交代码

```bash
git add src/ tests/
git commit -m "feat: add hello function"
```

Pre-commit hooks 会自动运行，确保代码质量。

### 5. 推送代码

```bash
git push origin main
```

GitHub Actions 会自动运行 CI/CD 流程。

## 常用命令速查

### 代码质量

```bash
pixi run format      # 格式化代码
pixi run lint        # 检查代码质量
pixi run typecheck   # 类型检查
pixi run security    # 安全扫描
```

### 测试

```bash
pixi run test                # 运行所有测试
pixi run -e py312 test       # Python 3.12 测试
pixi run -e py313 test       # Python 3.13 测试
pixi run -e py314 test       # Python 3.14 测试
```

### 文档

```bash
pixi run -e docs docs-serve  # 本地预览 (http://127.0.0.1:8000)
pixi run -e docs docs-build  # 构建静态文件
```

## 实战示例

### 添加新功能

**1. 创建功能分支**

```bash
git checkout -b feature/awesome-feature
```

**2. 编写代码**

```python title="src/calculator.py"
"""简单的计算器模块。"""

def add(a: int | float, b: int | float) -> int | float:
    """加法运算。"""
    return a + b

def multiply(a: int | float, b: int | float) -> int | float:
    """乘法运算。"""
    return a * b
```

**3. 编写测试**

```python title="tests/test_calculator.py"
import pytest
from src.calculator import add, multiply

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
    assert multiply(0, 100) == 0
```

**4. 运行检查**

```bash
pixi run check-all
```

**5. 提交并推送**

```bash
git add src/calculator.py tests/test_calculator.py
git commit -m "feat: add calculator module with add and multiply"
git push origin feature/awesome-feature
```

**6. 创建 Pull Request**

GitHub Actions 会自动运行所有检查。

### 添加依赖

**添加运行时依赖：**

```bash
pixi add requests httpx
```

这会更新 `pixi.toml` 并安装依赖。

**添加开发依赖：**

```bash
pixi add --feature dev pytest-asyncio pytest-mock
```

**添加文档依赖：**

```bash
pixi add --feature docs mkdocs-material pymdown-extensions
```

### 多版本测试

测试你的代码在所有支持的 Python 版本上都能运行：

```bash
# 在所有版本上运行测试
pixi run -e py312 test
pixi run -e py313 test
pixi run -e py314 test

# 或者使用 CI（推送后自动运行）
```

## 项目结构建议

```
my-project/
├── src/
│   ├── __init__.py        # 包入口
│   ├── core.py            # 核心功能
│   ├── utils.py           # 工具函数
│   └── models/            # 数据模型
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_core.py       # 核心功能测试
│   ├── test_utils.py      # 工具测试
│   └── conftest.py        # pytest 配置和 fixtures
├── docs/
│   ├── index.md           # 文档首页
│   ├── api/               # API 文档（自动生成）
│   └── guide/             # 使用指南
└── examples/              # 示例代码
    └── basic_usage.py
```

## 配置 GitHub Pages

推送代码后，配置文档自动部署：

1. 进入仓库 **Settings** → **Pages**
2. **Build and deployment** → **Source** 选择 **GitHub Actions**
3. 完成！推送到 `main` 分支时文档会自动部署

文档地址: `https://yourusername.github.io/your-project/`

## 下一步

- 🛠️ 查看所有 [CLI 命令](../guide/cli.md)
- 🔧 自定义 [Pre-commit 配置](../guide/pre-commit.md)
- 📊 了解 [CI 优化策略](../guide/ci-optimization.md)
- 💡 查看更多 [示例](../guide/examples.md)

## 常见问题

??? question "如何禁用某个 pre-commit hook？"
编辑 `.pre-commit-config.yaml`，注释掉不需要的 hook：

    ```yaml
    # - id: mypy-check
    #   name: mypy type check
    #   ...
    ```

??? question "测试很慢怎么办？" - 使用 `pixi run test -k test_name` 只运行特定测试 - 使用 `pixi run test --lf` 只运行上次失败的测试 - 使用 `pytest-xdist` 并行运行测试

??? question "如何添加新的 Pixi 任务？"
在 `pixi.toml` 的 `[tasks]` 部分添加：

    ```toml
    [tasks]
    my-task = "python scripts/my_script.py"
    ```

??? question "CI 运行太慢？"
查看 [CI 优化指南](../guide/ci-optimization.md) 了解如何优化。
