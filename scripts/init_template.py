#!/usr/bin/env python3
"""Initialize the template project with a package name and project name.

Usage:
    python scripts/init_template.py --name my_package --project "My Project"
    pixi run init --name my_package --project "My Project"

If no args provided, the script will prompt interactively.

What this does:
- Replaces placeholder names in pyproject.toml, README.md, TEMPLATE_USAGE.md, mkdocs.yml
- Renames src/your_package_name/ to src/{package_name}/
- Updates [tool.pixi.pypi-dependencies] in pyproject.toml
- Prints next steps
"""
import argparse
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(__file__))

FILES_TO_UPDATE = [
    "pyproject.toml",
    "README.md",
    "TEMPLATE_USAGE.md",
    "mkdocs.yml",
]


def replace_in_file(path: str, old: str, new: str) -> None:
    """Replace all occurrences of old string with new string in a file."""
    with open(path, "r", encoding="utf-8") as f:
        s = f.read()
    ns = s.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ns)


def normalize_package_name(name: str) -> str:
    """Convert package name to valid Python module name."""
    # Convert hyphens and dots to underscores
    normalized = re.sub(r'[-.]', '_', name)
    # Remove non-alphanumeric characters (except underscores)
    normalized = re.sub(r'[^\w]', '', normalized)
    # Ensure it doesn't start with a digit
    if normalized and normalized[0].isdigit():
        normalized = f"_{normalized}"
    return normalized.lower()


def rename_package_directory(old_name: str, new_name: str) -> None:
    """Rename the package directory from old_name to new_name."""
    old_path = os.path.join(ROOT, "src", old_name)
    new_path = os.path.join(ROOT, "src", new_name)

    if not os.path.exists(old_path):
        print(f"Warning: Package directory not found at {old_path}")
        return

    if os.path.exists(new_path):
        if new_path != old_path:  # Only remove if they're different
            print(f"Package directory {new_path} already exists, removing old one...")
            shutil.rmtree(old_path)
            return

    print(f"Renaming package directory: {old_name} -> {new_name}")
    shutil.move(old_path, new_path)


def update_pyproject_pypi_dependencies(package_name: str) -> None:
    """Update the [tool.pixi.pypi-dependencies] section in pyproject.toml."""
    p = os.path.join(ROOT, "pyproject.toml")
    with open(p, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find and update the pypi-dependencies section
    in_section = False
    updated = False
    for i, line in enumerate(lines):
        if "[tool.pixi.pypi-dependencies]" in line:
            in_section = True
            continue
        if in_section:
            if line.startswith("["):
                # Found the next section
                break
            if "your-package-name" in line:
                lines[i] = f'{package_name} = {{ path = ".", editable = true }}\n'
                updated = True
                break

    if updated:
        with open(p, "w", encoding="utf-8") as f:
            f.writelines(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize python-project-template")
    parser.add_argument("--name", help="package name (e.g. my_package or my-package)")
    parser.add_argument("--project", help="project display name (e.g. My Project)")
    args = parser.parse_args()

    pkg_input = args.name
    project = args.project

    if not pkg_input:
        pkg_input = input("Package name (e.g. my_package or my-package): ").strip()
    if not project:
        project = input("Project display name (e.g. My Project): ").strip()

    if not pkg_input:
        print("❌ Package name is required")
        return 2

    # Normalize package name to valid Python module name
    pkg_normalized = normalize_package_name(pkg_input)
    pkg_hyphenated = pkg_normalized.replace("_", "-")

    print(f"\n🔧 Initializing template...")
    print(f"  Package name: {pkg_hyphenated} (module: {pkg_normalized})")
    print(f"  Project name: {project}\n")

    # Step 1: Update file contents
    for fname in FILES_TO_UPDATE:
        path = os.path.join(ROOT, fname)
        if not os.path.exists(path):
            continue
        print(f"  Updating {fname}...")
        replace_in_file(path, "your-package-name", pkg_hyphenated)
        replace_in_file(path, "your_package_name", pkg_normalized)
        replace_in_file(path, "your-project-name", project)

    # Step 2: Update pyproject.toml pypi-dependencies
    print(f"  Updating pyproject.toml pypi-dependencies...")
    try:
        update_pyproject_pypi_dependencies(pkg_hyphenated)
    except Exception as e:
        print(f"  ⚠️  Warning: Failed to update pypi-dependencies: {e}")

    # Step 3: Rename package directory
    rename_package_directory("your_package_name", pkg_normalized)

    print("\n✅ Initialization complete!\n")
    print("📋 Next steps:")
    print(f"  1. Review pyproject.toml for any remaining placeholders")
    print(f"  2. Update src/{pkg_normalized}/__init__.py with your package description")
    print(f"  3. Update src/{pkg_normalized}/cli.py with your actual CLI commands")
    print(f"  4. Replace example tests in tests/ with your test implementation")
    print(f"  5. Update mkdocs.yml documentation")
    print(f"\n  6. Commit the changes:")
    print(f'     git add . && git commit -m "chore: initialize project as {pkg_hyphenated}"')
    print(f"\n🚀 Run checks with:")
    print(f"  pixi run check-all    # All quality checks")
    print(f"  pixi run test         # Run tests")
    print(f"  pixi run docs-serve   # Preview documentation (in docs env)")
    print(f"  pixi run -e docs docs-serve")
    return 0



if __name__ == "__main__":
    raise SystemExit(main())
