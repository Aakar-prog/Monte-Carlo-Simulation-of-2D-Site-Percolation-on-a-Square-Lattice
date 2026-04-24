import numpy as np


def generate_lattice(size: int, p: float, seed=None) -> np.ndarray:
    """
    Generate a random 2D square lattice for site percolation simulations.

    In site percolation, each lattice site is independently assigned
    one of two possible states:

        1 -> open (occupied) site
        0 -> closed (unoccupied) site

    The probability that a site is open is controlled by the occupation
    probability p. As p increases, larger connected clusters emerge,
    eventually leading to a spanning cluster near the critical
    percolation threshold.

    Parameters
    ----------
    size : int
        Linear dimension of the square lattice (L x L).

    p : float
        Probability that an individual site is open,
        where 0 ≤ p ≤ 1.

    seed : int, optional
        Random seed used to ensure reproducibility
        in Monte Carlo simulations.

    Returns
    -------
    numpy.ndarray
        Binary L x L lattice where:
            1 = open site
            0 = closed site

    Raises
    ------
    TypeError
        If size is not an integer.

    ValueError
        If size is non-positive or if p is outside [0,1].
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