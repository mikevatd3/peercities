import pytest
from src.model import weighted_distances, select_n_closest, apply_scale
import numpy as np
from scipy.stats import zscore


@pytest.fixture
def dataset():
    return np.array(
        [
            [0, 0, 0, 0],  # 0
            [0, 1, 1, 2],  # 1
            [0, 2, 0, 3],  # 2
            [0, 1, 1, 2.1],  # 3
            [1, 4, 3, 1],  # 4
            [1, 1, 2, 0],  # 5
        ]
    )


@pytest.fixture
def repeats():
    return np.array([1, 2, 1])


@pytest.fixture
def weights():
    return np.array([1, 1, 1]).reshape(1, -1)


@pytest.fixture
def weights_2d():
    return np.array(
        [
            [1, 1, 1.5],
            [1, 2, 1],
            [1, 1, 0.1],
        ]
    )


@pytest.fixture
def id_weights():
    return np.array(
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1],
        ]
    )


@pytest.fixture
def expected_output():
    return np.array(
        [
            [0.0, 2.17263206, 3.12256242, 2.24709302, 4.8280822, 2.9400296],
            [2.17263206, 0.0, 1.52062596, 0.08959216, 3.80776591, 2.93065711],
            [3.12256242, 1.52062596, 0.0, 1.46962409, 4.25904416, 3.98344754],
            [2.24709302, 0.08959216, 1.46962409, 0.0, 3.82983591, 2.98627663],
            [4.8280822, 3.80776591, 4.25904416, 3.82983591, 0.0, 2.71384135],
            [2.9400296, 2.93065711, 3.98344754, 2.98627663, 2.71384135, 0.0],
        ]
    )


@pytest.fixture
def expected_summary():
    return np.array(
        [
            [3, 2, 1, 0, 3, 3],
            [3, 1, 0, 3, 0, 0],
            [3, 1, 2, 3, 0, 0],
            [0, 3, 2, 3, 0, 0],
            [0, 0, 3, 0, 3, 3],
            [0, 2, 1, 0, 3, 3],
        ]
    )


def test_weighted_distances(
    dataset,
    weights,
    repeats,
    expected_output,
):
    zscores = zscore(dataset)
    scaled_data = apply_scale(zscores, weights, repeats)
    result = weighted_distances(scaled_data)
    result = result.reshape(result.shape[0], result.shape[1])

    assert np.isclose(result, expected_output).all()


def test_weighted_distances_id(dataset, id_weights, repeats):
    zscores = zscore(dataset)
    scaled_data = apply_scale(zscores, id_weights, repeats)
    distances = weighted_distances(scaled_data)
    closest = select_n_closest(distances, select=1)

    assert (closest.sum(axis=2).sum(axis=1) == 3).all()


def test_weighted_distances_simple(dataset, id_weights, repeats):
    zscores = zscore(dataset)
    scaled_data = apply_scale(zscores, id_weights, repeats)
    distances = weighted_distances(scaled_data)
    assert (distances.diagonal() == 0).all()

    closest = select_n_closest(distances, select=1)

    assert (closest.sum(axis=2) == np.eye(6) * id_weights.shape[1]).all()
