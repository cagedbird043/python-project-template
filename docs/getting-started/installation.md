# 安装指南

本页面详细介绍如何安装和配置 Python Project Template。

## 系统要求

- **操作系统**: Linux, macOS, 或 Windows
- **Python**: 3.12 或更高版本（由 Pixi 自动安装）
- **Git**: 用于版本控制

## 安装 Pixi

Pixi 是这个模板的核心依赖管理工具。

=== "Linux/macOS"
`bash
    curl -fsSL https://pixi.sh/install.sh | bash
    `

=== "Windows PowerShell"
`powershell
    iwr -useb https://pixi.sh/install.ps1 | iex
    `

=== "使用包管理器"
```bash # Homebrew (macOS/Linux)
brew install pixi

    # Cargo (Rust)
    cargo install pixi
    ```

安装完成后，重新启动终端或运行：

```bash
source ~/.bashrc  # 或 ~/.zshrc
```

验证安装：

```bash
pixi --version
```

## 获取模板

### 方法 1: 克隆仓库（推荐）

```bash
# 克隆模板到本地
git clone https://github.com/cagedbird043/python-project-template.git my-project
cd my-project

# 删除模板的 Git 历史
rm -rf .git

# 初始化自己的仓库
git init
git add .
git commit -m "chore: initial commit from template"
```

### 方法 2: 使用 GitHub 模板功能

1. 访问 [模板仓库](https://github.com/cagedbird043/python-project-template)
2. 点击绿色的 **"Use this template"** 按钮
3. 选择 **"Create a new repository"**
4. 填写你的仓库信息
5. 克隆你创建的新仓库

```bash
git clone https://github.com/yourusername/your-project.git
cd your-project
```

## 初始化项目

使用初始化脚本配置项目名称：

```bash
# CLI 模式
pixi run init --name my_package --project "My Awesome Project"

# 交互式模式
pixi run init
```

这会自动更新：

- ✅ `pyproject.toml` - 包名和项目信息
- ✅ `pixi.toml` - 环境配置
- ✅ `mkdocs.yml` - 文档配置
- ✅ `README.md` - 项目说明

## 安装开发环境

```bash
# 安装所有环境（推荐）
pixi install --all

# 或只安装默认开发环境
pixi install
```

这会创建以下环境：

| 环境      | Python 版本 | 用途                 |
| --------- | ----------- | -------------------- |
| `default` | 3.14        | 默认开发环境         |
| `py312`   | 3.12        | Python 3.12 测试     |
| `py313`   | 3.13        | Python 3.13 测试     |
| `py314`   | 3.14        | Python 3.14 测试     |
| `docs`    | 3.14        | 文档构建             |
| `prod`    | 3.14        | 生产环境（最小依赖） |

## 安装 Pre-commit Hooks

```bash
pixi run hooks-install
```

这会在每次 `git commit` 时自动运行代码检查。

## 验证安装

运行快速检查确保一切正常：

```bash
pixi run check
```

你应该看到：

```
✨ Pixi task (format in default): ruff format src/ tests/
✨ Pixi task (lint in default): ruff check src/ tests/
✨ Pixi task (typecheck in default): mypy src/
```

## 下一步

- 📖 阅读 [快速入门](quickstart.md) 开始开发
- 🛠️ 查看 [CLI 命令](../guide/cli.md) 了解所有可用命令
- 🔧 配置 [Pre-commit](../guide/pre-commit.md) 自定义检查
