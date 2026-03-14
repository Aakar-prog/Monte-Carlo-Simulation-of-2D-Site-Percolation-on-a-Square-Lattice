import numpy as np

from percolation.lattice import generate_lattice
from percolation.simulation import sweep_probabilities
from percolation.visualization import plot_lattice, plot_percolation_curve
from percolation.simulation import sweep_probabilities, estimate_threshold

def main():

    # Lattice size and number of Monte Carlo trials
    size = 30
    trials = 100

    # Range of occupation probabilities
    p_values = np.linspace(0.3, 0.8, 20)

    probabilities = sweep_probabilities(size, p_values, trials)

    # Estimate critical threshold
    p_c_est = estimate_threshold(p_values, probabilities)

    print(f"Estimated critical threshold p_c ≈ {p_c_est:.3f}")
    print("Theoretical value ≈ 0.5927")

    # Plot percolation transition
    plot_percolation_curve(p_values, probabilities, p_c_est)

    # Visualize one lattice configuration
    lattice = generate_lattice(size, 0.6)
    plot_lattice(lattice)


if __name__ == "__main__":
    main()