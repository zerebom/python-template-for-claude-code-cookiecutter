"""Pytest configuration and fixtures."""

import pytest
from {{ cookiecutter.package_name }}.core.example import ExampleConfig


@pytest.fixture
def example_config() -> ExampleConfig:
    """Create a basic test configuration."""
    return ExampleConfig(
        name="test",
        max_items=10,
        enable_validation=True,
    )