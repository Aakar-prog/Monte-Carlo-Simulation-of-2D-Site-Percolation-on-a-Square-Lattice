import numpy as np
from percolation.simulation import sweep_probabilities, estimate_threshold


def test_probability_range():
    """
    Ensure that simulated percolation probabilities remain
    within physically meaningful bounds.

    Since percolation probability represents the fraction
    of successful spanning events, every returned value
    must lie between 0 and 1.
    """

    p_vals = np.linspace(0.2, 0.8, 5)
    results = sweep_probabilities(10, p_vals, trials=5)

    assert np.all(results >= 0)
    assert np.all(results <= 1)


def test_output_length():
    """
    Confirm that the simulation returns one output
    probability for every occupation probability tested.

    This ensures that the probability sweep produces
    a complete percolation curve.
    """

    p_vals = np.linspace(0.2, 0.8, 5)
    results = sweep_probabilities(10, p_vals, trials=5)

    assert len(results) == len(p_vals)


def test_full_percolation():
    """
    Check that percolation is guaranteed when p = 1.

    If every lattice site is open, a spanning path
    must always exist.
    """

    p_vals = np.array([1.0])
    results = sweep_probabilities(10, p_vals, trials=5)

    assert results[0] == 1.0


def test_percolation_probability_monotonic():
    """
    Confirm that percolation probability generally increases
    as site occupation probability increases.

    Higher occupation probabilities should statistically
    produce larger connected clusters and increase the
    likelihood of forming a spanning cluster.

    A small tolerance is allowed due to Monte Carlo noise.
    """

    p_vals = np.linspace(0.3, 0.8, 6)
    results = sweep_probabilities(20, p_vals, trials=30)

    diffs = np.diff(results)

    assert np.all(diffs >= -0.15)


def test_threshold_estimate_reasonable():
    """
    Check that the estimated critical threshold is
    reasonably close to the theoretical value for
    2D square lattice site percolation.

    The accepted theoretical threshold is:

        p_c ≈ 0.5927
    """

    p_vals = np.linspace(0.4, 0.75, 15)
    probs = sweep_probabilities(30, p_vals, trials=50)

    p_est = estimate_threshold(p_vals, probs)

    assert abs(p_est - 0.5927) < 0.1


def test_extreme_probabilities():
    """
    Test physically expected behavior at extreme
    occupation probabilities.

    At p = 0:
        all sites are closed → no percolation

    At p = 1:
        all sites are open → guaranteed percolation
    """

    p_vals = np.array([0.0, 1.0])
    results = sweep_probabilities(10, p_vals, trials=10)

    assert results[0] == 0
    assert results[1] == 1


def test_reproducibility():
    """
    Ensure reproducibility of Monte Carlo simulations
    when the same random seed is used.

    Identical seeds should generate identical
    probability curves.
    """

    p_vals = np.linspace(0.4, 0.7, 5)

    results1 = sweep_probabilities(
        10, p_vals, trials=10, seed=42
    )

    results2 = sweep_probabilities(
        10, p_vals, trials=10, seed=42
    )

    assert np.allclose(results1, results2)