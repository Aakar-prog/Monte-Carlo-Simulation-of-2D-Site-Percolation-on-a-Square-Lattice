import numpy as np
from percolation.cluster import percolates


def test_simple_percolation():
    """
    A connected path from the top row to the bottom row
    should result in percolation.
    """

    lattice = np.array([
        [1,0,0],
        [1,1,0],
        [0,1,1]
    ])

    assert percolates(lattice)


def test_no_percolation():
    """
    Disconnected open sites should not produce a
    percolating path.
    """

    lattice = np.array([
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ])

    assert not percolates(lattice)


def test_full_lattice():
    """
    A lattice where all sites are open must percolate.
    """

    lattice = np.ones((5,5))

    assert percolates(lattice)


def test_empty_lattice():
    """
    A lattice where all sites are closed cannot percolate.
    """

    lattice = np.zeros((5,5))

    assert not percolates(lattice)


def test_single_open_site():
    """
    A 1x1 lattice with an open site should percolate.
    """

    lattice = np.array([[1]])

    assert percolates(lattice)


def test_single_closed_site():
    """
    A 1x1 lattice with a closed site should not percolate.
    """

    lattice = np.array([[0]])

    assert not percolates(lattice)


def test_vertical_percolation():

    lattice = np.array([
        [1,0,0],
        [1,0,0],
        [1,0,0]
    ])

    # A continuous vertical path should percolate
    assert percolates(lattice)


def test_blocked_lattice():

    lattice = np.array([
        [1,0,1],
        [0,0,0],
        [1,0,1]
    ])

    # No connected path from top to bottom
    assert not percolates(lattice)


def test_diagonal_not_connected():

    lattice = np.array([
        [1,0],
        [0,1]
    ])

    # Diagonal connections should NOT count
    assert not percolates(lattice)

def test_diagonal_not_connected():

    lattice = np.array([
        [1,0],
        [0,1]
    ])

    
