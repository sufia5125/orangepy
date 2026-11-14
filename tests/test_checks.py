
import numpy as np
import pytest

from orangepy import inspect


def test_clean_array():
    report = inspect(np.array([[1, 2], [3, 4]]))

    assert report.shape == (2, 2)
    assert report.nan_count == 0
    assert report.infinite_count == 0
    assert report.constant_columns == ()
    assert report.duplicate_rows == 0
    assert report.issues == []


def test_detects_nan_and_infinity():
    data = np.array([1.0, np.nan, np.inf, -np.inf])

    report = inspect(data)

    assert report.nan_count == 1
    assert report.infinite_count == 2


def test_detects_constant_columns():
    data = np.array([
        [5.0, 1.0, 9.0],
        [5.0, 2.0, 9.0],
        [5.0, 3.0, 9.0],
    ])

    report = inspect(data)

    assert report.constant_columns == (0, 2)


def test_counts_duplicate_rows():
    data = np.array([
        [1, 2],
        [3, 4],
        [1, 2],
        [1, 2],
    ])

    report = inspect(data)

    assert report.duplicate_rows == 2


def test_does_not_modify_input():
    data = np.array([1.0, np.nan, 3.0])
    original = data.copy()

    inspect(data)

    np.testing.assert_equal(data, original)


def test_rejects_string_arrays():
    with pytest.raises(TypeError):
        inspect(np.array(["hello", "world"]))


def test_empty_array():
    report = inspect(np.array([]))

    assert report.size == 0
    assert report.nan_count == 0
    assert report.issues == []


def test_report_can_be_serialized():
    report = inspect(np.array([1, 2, 3]))
    result = report.to_dict()

    assert result["shape"] == (3,)
    assert result["dtype"] == "int64"
