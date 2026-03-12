import numpy as np
import pytest

from percolation.lattice import generate_lattice


def test_lattice_size():

    L = generate_lattice(10, 0.5)

    assert L.shape == (10, 10)


def test_probability_zero():

    L = generate_lattice(10, 0.0)

    assert np.sum(L) == 0


def test_invalid_probability():

    with pytest.raises(ValueError):
        generate_lattice(10, 1.5)