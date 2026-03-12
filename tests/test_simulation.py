import numpy as np

from percolation.simulation import sweep_probabilities


def test_probability_range():

    p_vals = np.linspace(0.2, 0.8, 5)

    results = sweep_probabilities(10, p_vals, trials=5)

    assert np.all(results >= 0)
    assert np.all(results <= 1)