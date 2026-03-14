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


def plot_percolation_curve(p_values, probabilities, p_c=None):
    """
    Plot percolation probability vs occupation probability.
    """

    plt.plot(p_values, probabilities, marker="o", label="Simulation")

    # Draw vertical line at estimated threshold
    if p_c is not None:
        plt.axvline(p_c, linestyle="--", color="red", label=f"Estimated p_c ≈ {p_c:.3f}")

    plt.xlabel("Occupation probability p")
    plt.ylabel("Percolation probability")
    plt.title("Percolation Transition")

    plt.legend()
    plt.grid(True)

    plt.show()