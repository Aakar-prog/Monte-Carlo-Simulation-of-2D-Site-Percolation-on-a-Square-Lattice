import numpy as np

from percolation.lattice import generate_lattice
from percolation.cluster import percolates


def run_simulation(size: int, p: float, trials: int = 100):
    """
    Run multiple percolation experiments for a given probability p.

    Parameters
    ----------
    size : int
        Lattice dimension
    p : float
        Site occupation probability
    trials : int
        Number of Monte Carlo simulations

    Returns
    -------
    float
        Estimated percolation probability
    """

    count = 0

    for _ in range(trials):

        lattice = generate_lattice(size, p)

        if percolates(lattice):
            count += 1

    return count / trials


def sweep_probabilities(size, p_values, trials=100):
    """
    Compute percolation probability for multiple p values.
    """

    results = []

    for p in p_values:

        prob = run_simulation(size, p, trials)

        results.append(prob)

    return np.array(results)


def estimate_threshold(p_values, probabilities):
    """
    Estimate the critical percolation threshold p_c.
    We approximate it as the p where percolation probability is closest to 0.5.
    """

    idx = np.argmin(np.abs(probabilities - 0.5))
    return p_values[idx]