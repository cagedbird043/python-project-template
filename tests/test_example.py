"""Test suite for your awesome package.

This module contains example tests that demonstrate best practices for
testing with pytest. These are placeholders and should be replaced with
your actual test cases.

Examples:
    Run the tests:

    ```bash
    pixi run test
    ```

    Run with coverage:

    ```bash
    pixi run test --cov=src
    ```
"""


def test_example() -> None:
    """Test basic functionality.

    A simple test to verify that basic assertions work correctly.
    This is a placeholder test and should be replaced with actual tests.

    Raises:
        AssertionError: If the assertion fails.
    """
    assert True


def test_arithmetic() -> None:
    """Test basic arithmetic operations.

    Verifies that simple mathematical operations produce expected results.
    This demonstrates proper test organization and naming conventions.

    Raises:
        AssertionError: If the assertion fails.
    """
    result = 1 + 1
    assert result == 2, "Basic arithmetic should work correctly"


def test_string_operations() -> None:
    """Test string operations.

    Demonstrates testing string manipulation and formatting.

    Raises:
        AssertionError: If the assertion fails.
    """
    text = "hello"
    assert text.upper() == "HELLO"
    assert len(text) == 5
