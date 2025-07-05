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
    
    # Remove GitHub Actions if not needed
    if not {{ cookiecutter.use_github_actions }}:
        remove_directory(project_dir / ".github")
    
    # Remove pre-commit config if not needed
    if not {{ cookiecutter.use_pre_commit }}:
        remove_file(project_dir / ".pre-commit-config.yaml")
    
    # Remove dependabot config if not needed
    if not {{ cookiecutter.use_dependabot }} and (project_dir / ".github" / "dependabot.yml").exists():
        remove_file(project_dir / ".github" / "dependabot.yml")
        # If .github is empty after removing dependabot.yml, remove it
        github_dir = project_dir / ".github"
        if github_dir.exists() and not any(github_dir.iterdir()):
            remove_directory(github_dir)
    
    # Remove profiling utilities if not needed
    if not {{ cookiecutter.use_profiling }}:
        # Remove from main source
        profiling_file = project_dir / "src" / "{{ cookiecutter.package_name }}" / "utils" / "profiling.py"
        if profiling_file.exists():
            remove_file(profiling_file)
        
        # Remove from template
        template_profiling = project_dir / "template" / "src" / "{{ cookiecutter.package_name }}" / "utils" / "profiling.py"
        if template_profiling.exists():
            remove_file(template_profiling)
    
    # Remove logging utilities if not needed
    if not {{ cookiecutter.use_logging }}:
        # Remove from main source
        logging_file = project_dir / "src" / "{{ cookiecutter.package_name }}" / "utils" / "logging_config.py"
        if logging_file.exists():
            remove_file(logging_file)
        
        # Remove from template
        template_logging = project_dir / "template" / "src" / "{{ cookiecutter.package_name }}" / "utils" / "logging_config.py"
        if template_logging.exists():
            remove_file(template_logging)
    
    # Remove hypothesis tests if not needed
    if not {{ cookiecutter.use_hypothesis }}:
        # Remove property-based test directories
        property_tests = project_dir / "tests" / "property"
        if property_tests.exists():
            remove_directory(property_tests)
        
        template_property = project_dir / "template" / "tests" / "property"
        if template_property.exists():
            remove_directory(template_property)
    
    # Clean up empty directories
    for utils_dir in [
        project_dir / "src" / "{{ cookiecutter.package_name }}" / "utils",
        project_dir / "template" / "src" / "{{ cookiecutter.package_name }}" / "utils"
    ]:
        if utils_dir.exists() and not any(utils_dir.glob("*.py")):
            remove_directory(utils_dir)
    
    print("✅ Project generation completed!")
    print(f"📁 Project created at: {project_dir}")
    
    # Print enabled features
    features = []
    if {{ cookiecutter.use_github_actions }}:
        features.append("GitHub Actions CI/CD")
    if {{ cookiecutter.use_pre_commit }}:
        features.append("pre-commit hooks")
    if {{ cookiecutter.use_mypy_strict }}:
        features.append("mypy strict mode")
    if {{ cookiecutter.use_hypothesis }}:
        features.append("Hypothesis property-based testing")
    if {{ cookiecutter.use_benchmarks }}:
        features.append("Performance benchmarks")
    if {{ cookiecutter.use_logging }}:
        features.append("Structured logging")
    if {{ cookiecutter.use_profiling }}:
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