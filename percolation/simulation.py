import numpy as np

from percolation.lattice import generate_lattice
from percolation.cluster import percolates


def run_simulation(size: int, p: float, trials: int = 100, seed=None):
    """
    Run multiple Monte Carlo experiments to estimate the percolation probability
    for a given lattice size and occupation probability.

    Each trial generates a random lattice and checks whether a spanning cluster
    connects the top and bottom boundaries.

    Parameters
    ----------
    size : int
        Linear dimension of the square lattice (L x L).

    p : float
        Site occupation probability (0 ≤ p ≤ 1).

    trials : int
        Number of independent Monte Carlo simulations.

    seed : int, optional
        Base random seed used for reproducibility. Each trial uses a shifted
        seed to ensure independent random configurations.

    Returns
    -------
    float
        Estimated probability that the lattice percolates.
    """

    count = 0

    for t in range(trials):
        trial_seed = None if seed is None else seed + t
        lattice = generate_lattice(size, p, seed=trial_seed)

        if percolates(lattice):
            count += 1

    return count / trials




def sweep_probabilities(size, p_values, trials, seed=None):
    """
    Compute percolation probability for multiple p values.
    """

    results = []

    for p in p_values:

        prob = run_simulation(size, p, trials, seed)

        results.append(prob)

    return np.array(results)


def estimate_threshold(p_values, probabilities):
    """
    Estimate the critical percolation threshold p_c.
    We approximate it as the p where percolation probability is closest to 0.5.
    """

    idx = np.argmin(np.abs(probabilities - 0.5))
    return p_values[idx]

def compute_uncertainty(probabilities, trials):
    """
    Estimate statistical uncertainty of Monte Carlo probabilities.
    """
    return np.sqrt(probabilities * (1 - probabilities) / trials)