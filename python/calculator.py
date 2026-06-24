"""Basic arithmetic calculator functions."""


def add(a: float, b: float) -> float:
    """Return the sum of ``a`` and ``b``."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of ``a`` and ``b``."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of ``a`` and ``b``."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of ``a`` and ``b``."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 2))
    print(multiply(4, 6))
    print(divide(10, 2))
