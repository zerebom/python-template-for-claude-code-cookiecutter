"""Basic integration tests."""

from {{ cookiecutter.package_name }}.core.example import ExampleConfig


def test_config_integration_with_default_values() -> None:
    """Test integration between components with default values."""
    config = ExampleConfig(name="integration_test")
    
    # Test that default values work together
    assert config.name == "integration_test"
    assert config.max_items == 100
    assert config.enable_validation is True


def test_config_integration_with_custom_values() -> None:
    """Test integration between components with custom values."""
    config = ExampleConfig(
        name="custom_test",
        max_items=50,
        enable_validation=False,
    )
    
    # Test that custom values work together
    assert config.name == "custom_test"
    assert config.max_items == 50
    assert config.enable_validation is False