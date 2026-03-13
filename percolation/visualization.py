import matplotlib.pyplot as plt


def plot_lattice(lattice):
    """
    Visualize a lattice configuration.
    """

    plt.imshow(lattice, cmap="binary")
    plt.title("Lattice Configuration")
    plt.xlabel("Column")
    plt.ylabel("Row")
    plt.colorbar(label="Site state")

    plt.show()


def plot_percolation_curve(p_values, probabilities):
    """
    Plot percolation probability vs p.
    """

    plt.plot(p_values, probabilities, marker="o")

    plt.xlabel("Occupation probability p")
    plt.ylabel("Percolation probability")
    plt.title("Percolation Transition")

    plt.grid(True)

    plt.show()