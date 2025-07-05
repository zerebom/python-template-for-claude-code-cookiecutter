{%- if cookiecutter.use_hypothesis %}
"""Basic property-based tests using Hypothesis."""

from hypothesis import given
from hypothesis import strategies as st
from {{ cookiecutter.package_name }}.core.example import ExampleConfig


class TestExampleConfigProperty:
    """Property-based tests for ExampleConfig."""

    @given(
        name=st.text(min_size=1),
        max_items=st.integers(min_value=1, max_value=1000),
    )
    def test_valid_config_properties(self, name: str, max_items: int) -> None:
        """Test that valid configurations always work."""
        config = ExampleConfig(name=name, max_items=max_items)
        assert config.name == name
        assert config.max_items == max_items
        assert config.enable_validation is True

    @given(max_items=st.integers(max_value=0))
    def test_invalid_max_items_always_raises(self, max_items: int) -> None:
        """Test that non-positive max_items always raises ValueError."""
        import pytest
        with pytest.raises(ValueError):
            ExampleConfig(name="test", max_items=max_items)
{%- else %}
"""Property-based tests are disabled. Enable with use_hypothesis=true."""

def test_placeholder() -> None:
    """Placeholder test when Hypothesis is disabled."""
    assert True
{%- endif %}