"""A simple Python script to practice with."""


def greet(name: str = "World") -> str:
    """Return a greeting string."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print(greet())
    print(f"2 + 3 = {add(2, 3)}")
