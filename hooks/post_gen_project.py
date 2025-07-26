#!/usr/bin/env python
"""Post-generation hook for cookiecutter."""

import os
import shutil
from pathlib import Path


def remove_file(filepath):
    """Remove a file if it exists."""
    if os.path.exists(filepath):
        os.remove(filepath)


def remove_directory(dirpath):
    """Remove a directory tree if it exists."""
    if os.path.exists(dirpath):
        shutil.rmtree(dirpath)


def main():
    """Execute post-generation tasks."""
    project_dir = Path.cwd()

    # Remove .git directory if git initialization is disabled
    if not {{cookiecutter.initialize_git}}:
        git_dir = project_dir / ".git"
        if git_dir.exists():
            remove_directory(git_dir)
            print("🔧 Removed .git directory (initialize_git=false)")

    # Remove GitHub Actions if not needed
    if not {{cookiecutter.use_github_actions}}:
        remove_directory(project_dir / ".github")

    # Remove pre-commit config if not needed
    if not {{cookiecutter.use_pre_commit}}:
        remove_file(project_dir / ".pre-commit-config.yaml")


    # Remove profiling utilities if not needed
    if not {{cookiecutter.use_profiling}}:
        profiling_file = (
            project_dir
            / "src"
            / "{{ cookiecutter.package_name }}"
            / "utils"
            / "profiling.py"
        )
        if profiling_file.exists():
            remove_file(profiling_file)

    # Remove logging utilities if not needed
    if not {{cookiecutter.use_logging}}:
        logging_file = (
            project_dir
            / "src"
            / "{{ cookiecutter.package_name }}"
            / "utils"
            / "logging_config.py"
        )
        if logging_file.exists():
            remove_file(logging_file)

    # Remove hypothesis tests if not needed
    if not {{cookiecutter.use_hypothesis}}:
        property_tests = project_dir / "tests" / "property"
        if property_tests.exists():
            remove_directory(property_tests)

    # Clean up empty utils directory
    utils_dir = project_dir / "src" / "{{ cookiecutter.package_name }}" / "utils"
    if utils_dir.exists() and not any(utils_dir.glob("*.py")):
        remove_directory(utils_dir)

    print("✅ Project generation completed!")
    print(f"📁 Project created at: {project_dir}")

    # Print enabled features
    features = []
    if {{cookiecutter.use_github_actions}}:
        features.append("GitHub Actions CI/CD")
    if {{cookiecutter.use_pre_commit}}:
        features.append("pre-commit hooks")
    if {{cookiecutter.use_mypy_strict}}:
        features.append("mypy strict mode")
    if {{cookiecutter.use_hypothesis}}:
        features.append("Hypothesis property-based testing")
    if {{cookiecutter.use_benchmarks}}:
        features.append("Performance benchmarks")
    if {{cookiecutter.use_logging}}:
        features.append("Structured logging")
    if {{cookiecutter.use_profiling}}:
        features.append("Performance profiling")

    if features:
        print("\n🚀 Enabled features:")
        for feature in features:
            print(f"   - {feature}")

    print("\n📖 Next steps:")
    print("   1. cd {{ cookiecutter.project_slug }}")
    print("   2. make setup")
    print("   3. Start coding! 🎉")


if __name__ == "__main__":
    main()
