# flake8: noqa: S101
"""テスト"""

import pytest

from simple_tsp import tsp


@pytest.mark.parametrize(
    ("distances", "depot", "expected"),
    [
        ({(0, 2): 1, (2, 3): 1, (3, 1): 1, (1, 0): 1}, 0, [0, 2, 3, 1]),
        ({("a", "c"): 1, ("c", "d"): 1, ("d", "b"): 1, ("b", "a"): 1}, "a", ["a", "c", "d", "b"]),
        ([[0, 9, 1, 9], [1, 0, 9, 9], [9, 9, 0, 1], [9, 1, 9, 0]], 0, [0, 2, 3, 1]),
    ],
)
def test_tsp(distances, depot, expected) -> None:  # noqa: ANN001
    """tspのテスト"""
    assert tsp(distances, depot) == expected
