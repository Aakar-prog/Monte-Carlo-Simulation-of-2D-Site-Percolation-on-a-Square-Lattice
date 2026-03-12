import numpy as np


def generate_lattice(size: int, p: float, seed=None) -> np.ndarray:
    """
    Generate an LxL lattice where each site is open with probability p.

    Parameters
    ----------
    size : int
        Size of the lattice.
    p : float
        Probability that a site is open (0 ≤ p ≤ 1).
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    numpy.ndarray
        2D array with
        1 = open site
        0 = closed site
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size <= 0:
        raise ValueError("size must be positive")

    if not (0 <= p <= 1):
        raise ValueError("p must be between 0 and 1")

    rng = np.random.default_rng(seed)

    lattice = rng.random((size, size)) < p

    return lattice.astype(int)