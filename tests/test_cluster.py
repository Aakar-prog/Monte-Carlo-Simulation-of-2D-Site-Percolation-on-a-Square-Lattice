import numpy as np
from percolation.cluster import percolates, neighbors


def test_simple_percolation():
    """
    Verify successful percolation in a finite square lattice.

    A continuous connected path of open sites spanning
    from the top boundary to the bottom boundary
    should result in percolation.
    """

    lattice = np.array([
        [1, 0, 0],
        [1, 1, 0],
        [0, 1, 1]
    ])

    assert percolates(lattice)


def test_no_percolation():
    """
    Ensure disconnected clusters do not percolate.

    Even when multiple open sites are present,
    percolation should not occur if no continuous
    spanning path exists.
    """

    lattice = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    assert not percolates(lattice)


def test_full_lattice():
    """
    Confirm percolation in a fully occupied lattice.

    When all lattice sites are open, multiple connected
    paths exist and the system should always percolate.
    """

    lattice = np.ones((5, 5))

    assert percolates(lattice)


def test_empty_lattice():
    """
    Check percolation behavior in an empty lattice.

    When all lattice sites are closed, no connected
    cluster can form and percolation should never occur.
    """

    lattice = np.zeros((5, 5))

    assert not percolates(lattice)


def test_single_open_site():
    """
    Test percolation in the smallest possible system.

    For a 1x1 lattice, a single open site should percolate
    because the top and bottom boundaries coincide.
    """

    lattice = np.array([[1]])

    assert percolates(lattice)


def test_single_closed_site():
    """
    Ensure non-percolation in the smallest possible system.

    For a 1x1 lattice with a closed site,
    no conducting path exists.
    """

    lattice = np.array([[0]])

    assert not percolates(lattice)


def test_vertical_percolation():
    """
    Verify vertical spanning cluster formation.

    A continuous vertical chain of open sites connecting
    the top and bottom boundaries should percolate.
    """

    lattice = np.array([
        [1, 0, 0],
        [1, 0, 0],
        [1, 0, 0]
    ])

    assert percolates(lattice)


def test_blocked_lattice():
    """
    Confirm that broken paths prevent percolation.

    Blocked intermediate sites should interrupt connectivity
    and stop spanning cluster formation.
    """

    lattice = np.array([
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ])

    assert not percolates(lattice)


def test_diagonal_not_connected():
    """
    Check nearest-neighbor connectivity rules.

    Diagonal sites should not be treated as connected
    in standard square-lattice site percolation.
    """

    lattice = np.array([
        [1, 0],
        [0, 1]
    ])

    assert not percolates(lattice)


def test_neighbors_center():
    """
    Verify nearest-neighbor connectivity for an interior site
    in a 2D square lattice.

    A site located away from lattice boundaries should have
    exactly four valid nearest neighbors (up, down, left, right),
    consistent with standard site percolation rules.
    """

    result = neighbors(1, 1, 3)

    expected = [
        (0, 1),
        (2, 1),
        (1, 0),
        (1, 2)
    ]

    assert sorted(result) == sorted(expected)


def test_neighbors_corner():
    """
    Examine boundary behavior for a corner lattice site.

    Corner sites should return only two valid neighbors
    because positions outside finite lattice boundaries
    must be excluded.
    """

    result = neighbors(0, 0, 3)

    expected = [
        (1, 0),
        (0, 1)
    ]

    assert sorted(result) == sorted(expected)


def test_neighbors_edge():
    """
    Test boundary behavior for an edge lattice site.

    Edge sites should return exactly three valid neighbors
    while excluding out-of-bound coordinates.
    """

    result = neighbors(0, 1, 3)

    expected = [
        (0, 0),
        (0, 2),
        (1, 1)
    ]

    assert sorted(result) == sorted(expected)




    
