import numpy as np

from percolation.simulation import sweep_probabilities


def test_probability_range():

    p_vals = np.linspace(0.2, 0.8, 5)

    results = sweep_probabilities(10, p_vals, trials=5)

    assert np.all(results >= 0)
    assert np.all(results <= 1)

def test_output_length():

    p_vals = np.linspace(0.2, 0.8, 5)

    results = sweep_probabilities(10, p_vals, trials=5)

    # The simulation should return one probability for each p value
    assert len(results) == len(p_vals)

def test_full_percolation():

    p_vals = np.array([1.0])

    results = sweep_probabilities(10, p_vals, trials=5)

    # When p = 1 all sites are open, so the system must always percolate
    assert results[0] == 1.0