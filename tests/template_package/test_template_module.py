import pytest

from template_package.template_module import Greeter


@pytest.mark.parametrize(
    "name, expected_start",
    [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("", "Hello, !"),
    ],
)
def test_greet(name: str, expected_start: str) -> None:
    greeter = Greeter(name)
    greeting = greeter.greet()
    assert greeting.startswith(expected_start)
