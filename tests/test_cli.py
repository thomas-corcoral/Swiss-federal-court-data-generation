"""Tests for swiss_court_data_gen.cli module."""

from __future__ import annotations

from io import StringIO
from unittest.mock import patch


def test_main_returns_zero() -> None:
    """Test that main() returns 0 on success."""
    from swiss_court_data_gen.cli import main

    result = main()
    assert result == 0


def test_main_prints_version() -> None:
    """Test that main() prints the version."""
    from swiss_court_data_gen import __version__
    from swiss_court_data_gen.cli import main

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        output = mock_stdout.getvalue()

    assert __version__ in output
    assert "Swiss Court Data Generation" in output


def test_main_prints_hello_world() -> None:
    """Test that main() prints Hello World."""
    from swiss_court_data_gen.cli import main

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        output = mock_stdout.getvalue()

    assert "Hello World!" in output


def test_main_prints_coming_soon() -> None:
    """Test that main() indicates CLI implementation is coming soon."""
    from swiss_court_data_gen.cli import main

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        output = mock_stdout.getvalue()

    assert "CLI implementation coming soon" in output


def test_cli_module_can_be_imported() -> None:
    """Test that the CLI module can be imported."""
    from swiss_court_data_gen import cli

    assert cli is not None


def test_main_function_exists() -> None:
    """Test that main function is defined in cli module."""
    from swiss_court_data_gen.cli import main

    assert callable(main)


def test_cli_as_module() -> None:
    """Test that cli can be run as a module entry point."""
    from swiss_court_data_gen.cli import main

    # Simulate running as __main__
    with patch("sys.stdout", new_callable=StringIO):
        result = main()

    assert result == 0


def test_cli_output_line_count() -> None:
    """Test that main() produces expected number of output lines."""
    from swiss_court_data_gen.cli import main

    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        main()
        output = mock_stdout.getvalue()

    lines = [line for line in output.strip().split("\n") if line]
    assert len(lines) == 3, f"Expected 3 output lines, got {len(lines)}"


def test_main_return_type() -> None:
    """Test that main() returns an integer."""
    from swiss_court_data_gen.cli import main

    result = main()
    assert isinstance(result, int)
