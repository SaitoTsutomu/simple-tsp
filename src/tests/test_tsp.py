# flake8: noqa: S101
"""テスト"""

from math import isclose

import pytest

from simple_tsp import distance, tsp


def test_distance_near() -> None:
    """distanceのテスト"""
    d = distance(36, 135, 36.1, 134.9)
    assert isclose(d, 14.300, abs_tol=0.001)


def test_distance_far() -> None:
    """distanceのテスト"""
    d = distance(36, 135, 35, 136)
    assert isclose(d, 143.38, abs_tol=0.01)


def test_distance_same_location() -> None:
    """distanceの同一地点のテスト"""
    lat, lon = 36.172522266885586, 135
    d = distance(lat, lon, lat, lon)
    assert isclose(d, 0, abs_tol=0.00000001)


@pytest.mark.parametrize(
    ("distances", "depot", "expected"),
    [
        ({(0, 2): 1, (2, 3): 1, (3, 1): 1, (1, 0): 1}, 0, [0, 2, 3, 1]),
        ({("a", "c"): 1, ("c", "d"): 1, ("d", "b"): 1, ("b", "a"): 1}, "a", ["a", "c", "d", "b"]),
        ([[0, 9, 1, 9], [1, 0, 9, 9], [9, 9, 0, 1], [9, 1, 9, 0]], 0, [0, 2, 3, 1]),
    ],
)
def test_tsp(distances: dict, depot: int, expected: list[int]) -> None:
    """tspのテスト"""
    assert tsp(distances, depot) == expected
