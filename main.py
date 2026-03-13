import numpy as np

from percolation.lattice import generate_lattice
from percolation.simulation import sweep_probabilities
from percolation.visualization import plot_lattice, plot_percolation_curve


def main():
    # Lattice size and number of Monte Carlo trials
    size = 30
    trials = 100

    # Range of occupation probabilities
    p_values = np.linspace(0.3, 0.8, 20)

    # Estimate percolation probability for each p
    probabilities = sweep_probabilities(size, p_values, trials)

    # Plot percolation transition curve
    plot_percolation_curve(p_values, probabilities)

    # Visualize one lattice configuration
    lattice = generate_lattice(size, 0.6)
    plot_lattice(lattice)


if __name__ == "__main__":
    main()