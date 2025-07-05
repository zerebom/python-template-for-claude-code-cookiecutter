"""Basic unit tests for example module."""

import pytest
from {{ cookiecutter.package_name }}.core.example import ExampleConfig


class TestExampleConfig:
    """Test ExampleConfig class."""

    def test_valid_config_creation(self, example_config: ExampleConfig) -> None:
        """Test that a valid config can be created."""
        assert example_config.name == "test"
        assert example_config.max_items == 10
        assert example_config.enable_validation is True

    def test_invalid_max_items_raises_error(self) -> None:
        """Test that invalid max_items raises ValueError."""
        with pytest.raises(ValueError, match="max_items must be positive"):
            ExampleConfig(name="test", max_items=0)

    def test_negative_max_items_raises_error(self) -> None:
        """Test that negative max_items raises ValueError.""" 
        with pytest.raises(ValueError, match="max_items must be positive"):
            ExampleConfig(name="test", max_items=-1)