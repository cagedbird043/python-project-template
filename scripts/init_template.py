#!/usr/bin/env python3
"""Initialize the template project with a package name and project name.

Usage:
    python scripts/init_template.py --name my_package --project "My Project"
    pixi run init --name my_package --project "My Project"

If no args provided, the script will prompt interactively.

What this does:
- Replaces placeholder names in pyproject.toml, pixi.toml, README.md, TEMPLATE_USAGE.md, mkdocs.yml
- Updates [feature.docs.pypi-dependencies] key in pixi.toml
- Prints next steps
"""
import argparse
import os
import re

ROOT = os.path.dirname(os.path.dirname(__file__))

FILES_TO_UPDATE = [
    "pyproject.toml",
    "pixi.toml",
    "README.md",
    "TEMPLATE_USAGE.md",
    "mkdocs.yml",
]


def replace_in_file(path: str, old: str, new: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    ns = s.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ns)


def update_pixi_pypi_dependency(old_name: str, new_name: str) -> None:
    """Update the pypi-dependencies key in pixi.toml's docs feature."""
    p = os.path.join(ROOT, "pixi.toml")
    with open(p, "r", encoding="utf-8") as f:
        s = f.read()
    # Replace the single-line pypi-dependencies entry under the docs feature
    pattern = re.compile(r"(\[feature.docs.pypi-dependencies\]\s*\n)([^\n]*\n?)", re.M)
    replacement = f'[feature.docs.pypi-dependencies]\n{new_name} = {{ path = ".", editable = true }}\n'
    s_new = pattern.sub(replacement, s)
    if s_new != s:
        s = s_new
    with open(p, "w", encoding="utf-8") as f:
        f.write(s)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="package name (e.g. my_package)")
    parser.add_argument("--project", help="project display name (e.g. My Project)")
    args = parser.parse_args()

    pkg = args.name
    project = args.project

    if not pkg:
        pkg = input("Package name (e.g. my_package): ").strip()
    if not project:
        project = input("Project display name (e.g. My Project): ").strip()

    if not pkg:
        print("Package name is required")
        return 2

    # Replace basic placeholders
    print(f"Setting package name to: {pkg}")
    print(f"Setting project name to: {project}")

    for fname in FILES_TO_UPDATE:
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            continue
        replace_in_file(path, "your-package-name", pkg)
        replace_in_file(path, "your-project-name", project)

    # Update pixi pypi-dependencies section
    print("Updating pixi.toml pypi-dependencies...")
    try:
        update_pixi_pypi_dependency("your-package-name", pkg)
    except Exception as e:
        print(f"Warning: Failed to update pypi-dependencies: {e}")

    print("\n✅ Initialization complete!\n")
    print("Next steps:")
    print("  1. Review pyproject.toml and pixi.toml for any remaining placeholders")
    print("  2. Update src/__init__.py with your package description")
    print("  3. Replace example tests in tests/ with your test implementation")
    print("  4. Commit the changes:")
    print(f'     git add . && git commit -m "chore: initialize project as {pkg}"')
    print("\nRun checks with:")
    print("  pixi run check-all    # All quality checks")
    print("  pixi run test         # Run tests")
    print("  pixi run docs-serve   # Preview documentation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
