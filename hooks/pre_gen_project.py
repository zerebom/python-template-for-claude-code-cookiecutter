#!/usr/bin/env python
"""Pre-generation hook for cookiecutter."""

import re
import sys


def validate_project_name(project_name):
    """Validate project name."""
    if not project_name:
        print("ERROR: Project name cannot be empty")
        return False
    
    if not re.match(r'^[a-zA-Z0-9]([a-zA-Z0-9\s\-_]*[a-zA-Z0-9])?$', project_name):
        print("ERROR: Project name must start and end with alphanumeric characters")
        print("       and can contain spaces, hyphens, and underscores in between")
        return False
    
    return True


def validate_package_name(package_name):
    """Validate Python package name."""
    if not package_name:
        print("ERROR: Package name cannot be empty")
        return False
    
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', package_name):
        print("ERROR: Package name must be a valid Python identifier")
        print("       (start with letter, contain only letters, numbers, and underscores)")
        return False
    
    # Check for Python reserved keywords
    import keyword
    if keyword.iskeyword(package_name):
        print(f"ERROR: '{package_name}' is a Python reserved keyword")
        return False
    
    return True


def validate_version(version):
    """Validate version string."""
    if not version:
        print("ERROR: Version cannot be empty")
        return False
    
    # Basic semantic version pattern
    if not re.match(r'^\d+\.\d+\.\d+([a-zA-Z0-9\-\.]*)?$', version):
        print("ERROR: Version must follow semantic versioning (e.g., 1.0.0)")
        return False
    
    return True


def validate_python_version(python_version):
    """Validate Python version."""
    if not python_version:
        print("ERROR: Python version cannot be empty")
        return False
    
    if not re.match(r'^\d+\.\d+$', python_version):
        print("ERROR: Python version must be in format X.Y (e.g., 3.12)")
        return False
    
    # Check minimum supported version
    major, minor = map(int, python_version.split('.'))
    if (major, minor) < (3, 10):
        print("ERROR: Minimum supported Python version is 3.10")
        return False
    
    return True


def main():
    """Execute pre-generation validations."""
    project_name = "{{ cookiecutter.project_name }}"
    package_name = "{{ cookiecutter.package_name }}"
    version = "{{ cookiecutter.version }}"
    python_version = "{{ cookiecutter.python_version }}"
    
    print("🔍 Validating cookiecutter parameters...")
    
    validations = [
        ("Project name", project_name, validate_project_name),
        ("Package name", package_name, validate_package_name), 
        ("Version", version, validate_version),
        ("Python version", python_version, validate_python_version),
    ]
    
    for name, value, validator in validations:
        print(f"   ✓ Checking {name}: {value}")
        if not validator(value):
            sys.exit(1)
    
    print("✅ All validations passed!")
    print(f"🎯 Creating project: {project_name}")
    print(f"📦 Package name: {package_name}")
    print(f"🐍 Python version: {python_version}")


if __name__ == "__main__":
    main()