# 贡献指南

感谢你对 Python Project Template 的关注！我们欢迎任何形式的贡献。

## 📋 贡献方式

### 报告问题

发现 Bug 或有功能建议？请 [创建 Issue](https://github.com/cagedbird043/python-project-template/issues/new)。

**好的 Issue 应包含：**

- ✅ 清晰的标题
- ✅ 详细的描述
- ✅ 重现步骤（如果是 Bug）
- ✅ 预期行为 vs 实际行为
- ✅ 环境信息（OS、Python 版本、Pixi 版本）

### 提交代码

1. **Fork 仓库**

   点击右上角的 "Fork" 按钮

2. **克隆你的 Fork**

   ```bash
   git clone https://github.com/yourusername/python-project-template.git
   cd python-project-template
   ```

3. **安装开发环境**

   ```bash
   pixi install --all
   pixi run hooks-install
   ```

4. **创建功能分支**

   ```bash
   git checkout -b feature/your-feature-name
   ```

5. **进行修改**

   - 编写代码
   - 添加测试
   - 更新文档

6. **运行检查**

   ```bash
   pixi run check-all
   ```

7. **提交更改**

   ```bash
   git add .
   git commit -m "feat: add awesome feature"
   ```

8. **推送到你的 Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

9. **创建 Pull Request**

   访问你的 Fork 页面，点击 "New Pull Request"

## 📝 提交规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建/工具配置
- `ci`: CI/CD 相关

### 示例

```bash
# 好的提交消息
feat: add calculator module with basic operations
fix: correct type hints in hello function
docs: update installation guide with Windows support
ci: optimize cache strategy for faster builds

# 不好的提交消息
update code
fix bug
wip
```

## 🧪 测试要求

所有代码贡献必须包含测试：

```bash
# 运行测试
pixi run test

# 检查覆盖率
pixi run test

# 多版本测试
pixi run -e py312 test
pixi run -e py313 test
pixi run -e py314 test
```

**测试覆盖率要求**: >= 80%

## 📚 文档要求

- ✅ 所有公共 API 必须有 docstring
- ✅ docstring 使用 Google 风格
- ✅ 复杂功能需要使用示例
- ✅ 新功能需要更新用户文档

**Docstring 示例：**

```python
def calculate_sum(numbers: list[int]) -> int:
    """计算数字列表的总和。

    Args:
        numbers: 要相加的整数列表

    Returns:
        所有数字的总和

    Raises:
        ValueError: 如果列表为空

    Examples:
        >>> calculate_sum([1, 2, 3])
        6
        >>> calculate_sum([])
        Traceback (most recent call last):
        ValueError: List cannot be empty
    """
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers)
```

## 🎨 代码风格

我们使用自动化工具确保代码风格一致：

- **Ruff** - 代码格式化和检查
- **MyPy** - 类型检查
- **Bandit** - 安全检查

配置已内置，Pre-commit hooks 会自动运行这些检查。

**最佳实践：**

- ✅ 使用类型提示
- ✅ 保持函数简短（< 50 行）
- ✅ 避免全局变量
- ✅ 使用有意义的变量名
- ✅ 每个函数只做一件事

## 🔄 PR 审查流程

提交 PR 后：

1. **自动检查** - GitHub Actions 会运行所有测试
2. **代码审查** - 维护者会审查你的代码
3. **修改反馈** - 根据反馈进行修改
4. **合并** - 审查通过后合并到 main 分支

**PR 被接受的要求：**

- ✅ 所有 CI 检查通过
- ✅ 代码覆盖率不下降
- ✅ 有清晰的提交消息
- ✅ 功能完整且经过测试
- ✅ 文档已更新

## 🏗️ 项目结构

```
python-project-template/
├── .github/
│   └── workflows/        # CI/CD 配置
├── docs/                 # 文档源文件
├── scripts/              # 辅助脚本
│   └── init_template.py  # 初始化脚本
├── src/                  # 模板示例代码
├── tests/                # 测试代码
├── mkdocs.yml            # 文档配置
├── pixi.toml             # Pixi 配置
├── pyproject.toml        # 项目元数据
└── .pre-commit-config.yaml  # Pre-commit 配置
```

## 📬 联系方式

- **GitHub Issues**: [提交问题](https://github.com/cagedbird043/python-project-template/issues)
- **GitHub Discussions**: [讨论区](https://github.com/cagedbird043/python-project-template/discussions)
- **作者**: [@cagedbird043](https://github.com/cagedbird043)

## 📄 许可证

贡献的代码将使用 [MIT License](https://github.com/cagedbird043/python-project-template/blob/main/LICENSE) 许可。

---

再次感谢你的贡献！🎉
