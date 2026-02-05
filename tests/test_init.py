"""Tests for swiss_court_data_gen package initialization."""

from __future__ import annotations


def test_version_is_string() -> None:
    """Test that __version__ is a string."""
    from swiss_court_data_gen import __version__

    assert isinstance(__version__, str)


def test_version_format() -> None:
    """Test that __version__ follows semantic versioning format."""
    from swiss_court_data_gen import __version__

    # Should have at least major.minor.patch format
    parts = __version__.split(".")
    assert len(parts) >= 2, f"Version {__version__} should have at least major.minor format"

    # First two parts should be numeric
    assert parts[0].isdigit(), f"Major version '{parts[0]}' should be numeric"
    assert parts[1].isdigit(), f"Minor version '{parts[1]}' should be numeric"


def test_all_exports() -> None:
    """Test that __all__ contains expected exports."""
    from swiss_court_data_gen import __all__

    assert "__version__" in __all__


def test_package_import() -> None:
    """Test that the package can be imported."""
    import swiss_court_data_gen

    assert swiss_court_data_gen is not None


def test_version_not_empty() -> None:
    """Test that __version__ is not empty."""
    from swiss_court_data_gen import __version__

    assert __version__, "__version__ should not be empty"
    assert len(__version__) > 0
