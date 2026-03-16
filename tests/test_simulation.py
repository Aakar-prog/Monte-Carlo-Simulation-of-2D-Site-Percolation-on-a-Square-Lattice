import numpy as np

from percolation.simulation import sweep_probabilities,estimate_threshold




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


def test_percolation_probability_monotonic():
    """
    Percolation probability should increase as occupation probability increases.
    """

    p_vals = np.linspace(0.3, 0.8, 6)

    results = sweep_probabilities(20, p_vals, trials=30)

    # Differences between successive probabilities
    diffs = np.diff(results)

    # Allow small statistical noise
    assert np.all(diffs >= -0.15)   


def test_threshold_estimate_reasonable():
    """
    Estimated threshold should be close to theoretical value for square lattice.
    """

    p_vals = np.linspace(0.4, 0.75, 15)

    probs = sweep_probabilities(30, p_vals, trials=50)

    p_est = estimate_threshold(p_vals, probs)

    assert abs(p_est - 0.5927) < 0.1


def test_extreme_probabilities():
    """
    No percolation at p=0 and guaranteed percolation at p=1.
    """

    p_vals = np.array([0.0, 1.0])

    results = sweep_probabilities(10, p_vals, trials=10)

    assert results[0] == 0
    assert results[1] == 1


def test_reproducibility():
    """
    The simulation should produce identical results when the same random seed is used.
    """

    p_vals = np.linspace(0.4, 0.7, 5)

    results1 = sweep_probabilities(10, p_vals, trials=10, seed=42)
    results2 = sweep_probabilities(10, p_vals, trials=10, seed=42)

    assert np.allclose(results1, results2)