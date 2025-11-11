# 使用示例

本页面展示如何使用此模板创建你自己的项目。

## 示例 1: 创建数据处理项目

假设你想创建一个数据处理工具：

### 1. 初始化项目

```bash
# 克隆模板
git clone https://github.com/cagedbird043/python-project-template.git my-data-tool
cd my-data-tool

# 运行初始化脚本
pixi run init-template
```

### 2. 添加你的代码

在 `src/` 目录创建你的模块：

```python
# src/processor.py
def process_data(data: list[dict]) -> list[dict]:
    """处理数据"""
    return [item for item in data if item.get('valid')]
```

### 3. 编写测试

```python
# tests/test_processor.py
from src.processor import process_data

def test_process_data():
    data = [
        {'id': 1, 'valid': True},
        {'id': 2, 'valid': False},
        {'id': 3, 'valid': True}
    ]
    result = process_data(data)
    assert len(result) == 2
    assert all(item['valid'] for item in result)
```

### 4. 运行测试

```bash
pixi run test
```

## 示例 2: 创建 CLI 工具

### 添加 CLI 依赖

```bash
pixi add typer rich
```

### 创建 CLI 入口

```python
# src/cli.py
import typer
from rich import print

app = typer.Typer()

@app.command()
def hello(name: str):
    """问候用户"""
    print(f"[bold green]Hello {name}![/bold green]")

if __name__ == "__main__":
    app()
```

### 配置任务

在 `pixi.toml` 添加：

```toml
[tasks]
cli = "python -m src.cli"
```

### 使用

```bash
pixi run cli hello World
# Output: Hello World!
```

## 示例 3: 添加新的依赖

```bash
# 添加生产依赖
pixi add requests pandas

# 添加开发依赖
pixi add --feature dev pytest-cov

# 添加文档依赖
pixi add --feature docs mkdocs-material
```

## 示例 4: 配置 Pre-commit

模板已经包含 pre-commit 配置，你可以自定义：

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.8.4
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

## 示例 5: 多环境测试

测试多个 Python 版本：

```bash
# Python 3.12
pixi run test-312

# Python 3.13
pixi run test-313

# Python 3.14
pixi run test-314
```

## 示例 6: CI/CD 集成

模板已包含 GitHub Actions 配置，会自动：

- 运行测试
- 检查代码质量
- 构建项目
- 发布文档

你可以根据需要修改 `.github/workflows/` 下的文件。

## 更多资源

- [CLI 命令参考](cli.md)
- [Pre-commit 配置](pre-commit.md)
- [CI 优化指南](ci-optimization.md)
