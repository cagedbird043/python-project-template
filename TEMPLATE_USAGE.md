# 如何使用此模板

## 🎯 快速开始

### 1. 复制模板创建新项目

```bash
# 复制整个模板目录
cp -r python-project-template my-new-project
cd my-new-project

# 重新初始化 Git（移除模板的 Git 历史）
rm -rf .git
git init
```

### 2. 必须修改的文件

#### `pyproject.toml`

```toml
[project]
name = "your-package-name"  # ← 改成你的包名（小写，用连字符）
version = "0.1.0"
description = "Your project description"  # ← 改成你的描述
authors = [{ name = "Your Name", email = "you@example.com" }]  # ← 改成你的信息

[project.urls]
Homepage = "https://github.com/yourusername/your-project"  # ← 改URL
Repository = "https://github.com/yourusername/your-project.git"
Issues = "https://github.com/yourusername/your-project/issues"
```

#### `pixi.toml`

```toml
[workspace]
name = "your-project-name"  # ← 改成你的项目名
version = "0.1.0"
description = "Your project description"  # ← 改成你的描述

[feature.docs.pypi-dependencies]
your-package-name = { path = ".", editable = true }  # ← 改成和pyproject.toml一致的包名
```

#### `README.md`

完全重写，包括：

- 项目名称和描述
- 安装说明
- 使用示例
- API 文档链接

#### `src/` 目录

重命名为你的包名：

```bash
mv src your_package_name
```

或者直接在 src/ 中开发（保持 src 布局）。

### 3. 安装依赖并测试

```bash
# 安装所有环境
pixi install --all

# 安装 pre-commit hooks
pixi run hooks-install

# 运行测试确保模板工作正常
pixi run test

# 运行所有检查
pixi run check-all
```

### 4. 创建 GitHub 仓库

```bash
# 在 GitHub 上创建一个新仓库（不要初始化）
# 然后连接到远程仓库

git remote add origin git@github.com:yourusername/your-project.git
git add .
git commit -m "feat: initialize project from template"
git push -u origin main
```

### 5. 配置 GitHub Pages（如果需要文档）

1. 推送一次代码后，GitHub Actions 会自动创建 `gh-pages` 分支
2. 去仓库 Settings → Pages
3. Source 选择 "Deploy from a branch"
4. Branch 选择 `gh-pages`，目录选择 `/ (root)`
5. 保存后，文档会发布到 `https://yourusername.github.io/your-project/`

## 📋 可选配置

### 添加文档

如果需要文档站点，创建 `mkdocs.yml`：

```yaml
site_name: Your Project
site_description: Your project description
site_author: Your Name
repo_url: https://github.com/yourusername/your-project
repo_name: yourusername/your-project

theme:
  name: material
  palette:
    - scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

nav:
  - Home: index.md
  - Getting Started:
      - Installation: getting-started/installation.md
  - API Reference:
      - Module: api/module.md
```

然后创建文档文件：

```bash
mkdir -p docs/getting-started docs/api
echo "# Your Project" > docs/index.md
echo "# Installation" > docs/getting-started/installation.md
echo "# API Reference" > docs/api/module.md
```

### 配置 PyPI 发布

如果要发布到 PyPI：

1. 在 PyPI 创建账号：https://pypi.org/account/register/
2. 创建 API Token：https://pypi.org/manage/account/token/
3. 在 GitHub 仓库 Settings → Secrets → Actions 添加：
   - `PYPI_API_TOKEN`: 你的 PyPI token

然后创建 tag 即可自动发布：

```bash
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

### 调整 Python 版本支持

如果不需要支持所有 Python 版本，可以删除相应的环境：

```toml
# 在 pixi.toml 中删除不需要的 feature
# [feature.py312.dependencies]  # 删除此部分如果不支持 3.12

[environments]
# 只保留需要的环境
default = { features = ["dev", "py314"] }
py314 = { features = ["dev", "py314"] }
docs = { features = ["docs", "py314"] }
prod = { features = ["py314"] }
```

然后在 `pyproject.toml` 中更新：

```toml
requires-python = ">=3.14,<3.15"  # 只支持 3.14

classifiers = [
    # 只保留 3.14
    "Programming Language :: Python :: 3.14",
]
```

### 自定义 CI/CD

#### 简化 CI（如果不需要多版本测试）

编辑 `.github/workflows/ci.yml`，删除 `test-compatibility` job，只保留基本检查。

#### 添加代码覆盖率上传

在 `test-compatibility` job 中取消注释 codecov 上传部分，并在 https://codecov.io 注册。

## 🎨 自定义工具配置

### Ruff 配置

在 `pyproject.toml` 中调整：

```toml
[tool.ruff]
line-length = 120  # 改成你喜欢的长度
target-version = "py312"  # 改成你的最低版本

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "B", "Q"]  # 添加更多规则
```

### MyPy 配置

```toml
[tool.mypy]
strict = true  # 改成 false 如果太严格
ignore_missing_imports = true
```

### Pytest 配置

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--cov=src",  # 改成你的包名
    "--cov-report=html",
    "--cov-report=term-missing",
]
```

## 🔧 常见问题

### Q: 为什么有这么多环境？

A: 多环境支持确保：

- `py312/py313/py314` - 多版本兼容性测试
- `docs` - 文档构建不干扰开发环境
- `prod` - 生产环境最小依赖

如果你的项目很简单，可以只保留 `default` 环境。

### Q: pre-commit hooks 太慢了怎么办？

A: 可以禁用某些 hook：

```yaml
# 在 .pre-commit-config.yaml 中注释掉不需要的
# - id: mypy  # 注释掉如果觉得太慢
```

### Q: CI 运行太久了

A: 调整策略：

- 移除 `test-cross-platform` job（如果不需要跨平台支持）
- 只在 `test-compatibility` 中测试一个 Python 版本
- 增加 `concurrency.cancel-in-progress: true`

### Q: 如何添加新的依赖？

A: 使用 Pixi：

```bash
# 添加运行时依赖（所有环境都有）
pixi add requests

# 添加开发依赖
pixi add --feature dev ipython

# 添加文档依赖
pixi add --feature docs mkdocs-awesome-pages-plugin
```

## 📚 更多资源

- [Pixi 文档](https://pixi.sh)
- [Ruff 文档](https://docs.astral.sh/ruff/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [Pre-commit](https://pre-commit.com/)

---

**🎉 现在开始你的新项目吧！**
