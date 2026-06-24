"""Fibonacci sequence utilities."""

from typing import List


def fibonacci(n: int) -> List[int]:
    """Return the first ``n`` numbers of the Fibonacci sequence."""
    if n < 0:
        raise ValueError("n must be non-negative")

    sequence: List[int] = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def main() -> None:
    print(fibonacci(10))


if __name__ == "__main__":
    main()
