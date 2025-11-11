# Python Project Template

**现代化 Python 项目模板，内置最佳实践**

作者: [cagedbird043](https://github.com/cagedbird043)
仓库: [python-project-template](https://github.com/cagedbird043/python-project-template)

---

## 🎯 这是什么？

这是一个开箱即用的 Python 项目模板，集成了所有现代化开发工具和最佳实践：

- ✅ **Pixi** - 快速、可靠的包管理
- ✅ **Ruff** - 极速代码检查和格式化
- ✅ **MyPy** - 严格类型检查
- ✅ **pytest** - 现代化测试框架
- ✅ **Pre-commit** - 自动化 Git hooks
- ✅ **GitHub Actions** - 4 层 CI/CD 架构
- ✅ **MkDocs** - 自动化文档生成

支持 **Python 3.12、3.13、3.14** 三个版本。

## 🚀 快速开始

### 1. 复制模板

```bash
# 克隆模板
git clone https://github.com/cagedbird043/python-project-template.git my-project
cd my-project

# 删除模板的 Git 历史
rm -rf .git
git init
git add .
git commit -m "chore: initial commit from template"
```

### 2. 安装 Pixi

=== "Linux/macOS"
`bash
    curl -fsSL https://pixi.sh/install.sh | bash
    `

=== "Windows"
`powershell
    iwr -useb https://pixi.sh/install.ps1 | iex
    `

### 3. 初始化项目

```bash
# 运行初始化脚本
pixi run init --name my_package --project "My Awesome Project"

# 或者交互式初始化
pixi run init
```

初始化脚本会自动：

- ✅ 替换项目名称和包名
- ✅ 更新所有配置文件
- ✅ 配置文档构建

### 4. 安装环境

```bash
# 安装所有环境（default, py312, py313, py314, docs, prod）
pixi install --all

# 或只安装默认环境
pixi install
```

### 5. 开始开发！

```bash
# 运行快速检查
pixi run check

# 运行完整检查
pixi run check-all

# 运行测试
pixi run test

# 启动文档预览
pixi run -e docs docs-serve
```

## 📚 详细文档

- [安装指南](getting-started/installation.md) - 详细的安装步骤
- [快速入门](getting-started/quickstart.md) - 快速上手教程
- [CLI 命令](guide/cli.md) - 所有可用命令
- [Pre-commit 配置](guide/pre-commit.md) - Git hooks 配置
- [CI 优化](guide/ci-optimization.md) - CI/CD 最佳实践
- [示例](guide/examples.md) - 实际使用示例

## 🛠️ 可用命令

### 代码质量检查

```bash
pixi run format      # 格式化代码 (Ruff)
pixi run lint        # 检查代码质量 (Ruff)
pixi run typecheck   # 类型检查 (MyPy)
pixi run security    # 安全扫描 (Bandit)
pixi run test        # 运行测试 (pytest)

pixi run check       # 快速检查（format + lint + typecheck）
pixi run check-all   # 完整检查（包括测试和安全扫描）
```

### 多版本测试

```bash
pixi run -e py312 test   # Python 3.12 测试
pixi run -e py313 test   # Python 3.13 测试
pixi run -e py314 test   # Python 3.14 测试
```

### 文档

```bash
pixi run -e docs docs-serve   # 本地预览 (http://127.0.0.1:8000)
pixi run -e docs docs-build   # 构建静态文件
```

### Pre-commit Hooks

```bash
pixi run hooks-install   # 安装 hooks
pixi run hooks-run       # 手动运行所有 hooks
```

### 构建发布

```bash
pixi run build           # 构建包
pixi run clean-build     # 清理构建产物
```

## 🏗️ 项目结构

```
my-project/
├── .github/
│   └── workflows/
│       ├── ci.yml           # 主 CI（4 层架构）
│       ├── docs.yml         # 文档自动部署
│       ├── pr-check.yml     # PR 快速检查
│       └── release.yml      # 发布流程
├── docs/                    # 文档源文件
│   └── index.md
├── src/                     # 你的源代码
│   └── __init__.py
├── tests/                   # 测试代码
│   └── test_example.py
├── scripts/
│   └── init_template.py     # 初始化脚本
├── mkdocs.yml               # 文档配置
├── pixi.toml                # Pixi 配置
├── pyproject.toml           # 项目配置
└── .pre-commit-config.yaml  # Pre-commit 配置
```

## 🔧 配置 GitHub Pages

推送代码后，需要配置一次：

1. 进入仓库 **Settings** → **Pages**
2. **Build and deployment** → **Source** 选择 **GitHub Actions**
3. 完成！文档会自动部署到 `https://<username>.github.io/<repo-name>/`

## ❓ 常见问题

### 为什么选择 Pixi？

- **快速**: 比 conda 快 10-100 倍
- **可靠**: 完全可重现的环境
- **简单**: 一个 `pixi.toml` 管理所有依赖
- **强大**: 支持多环境、任务管理、跨平台

### 如何添加依赖？

```bash
# 添加运行时依赖
pixi add requests

# 添加开发依赖
pixi add --feature dev pytest

# 添加特定环境依赖
pixi add --feature docs mkdocs-material
```

### 如何自定义 CI？

查看 [CI 优化指南](guide/ci-optimization.md) 了解如何调整 4 层 CI 架构。

### Pre-commit hooks 运行慢？

所有 hooks 都有缓存支持，首次运行较慢是正常的。

## 📝 贡献

欢迎提交 Issue 和 Pull Request！

仓库: [https://github.com/cagedbird043/python-project-template](https://github.com/cagedbird043/python-project-template)

## 📄 许可证

MIT License - 自由使用、修改和分发。

---

**Happy Coding! 🎉**
