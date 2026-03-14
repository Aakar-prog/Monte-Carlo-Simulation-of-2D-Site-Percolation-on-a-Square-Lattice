import numpy as np

from percolation.lattice import generate_lattice
from percolation.simulation import sweep_probabilities
from percolation.visualization import plot_lattice, plot_percolation_curve
from percolation.simulation import sweep_probabilities, estimate_threshold

def main():

    sizes = [20, 40, 60]
    trials = 100
    p_c_theory = 0.5927

    p_values = np.linspace(0.3, 0.8, 20)

    for size in sizes:

     probabilities = sweep_probabilities(size, p_values, trials)

    p_c_est = estimate_threshold(p_values, probabilities)

    error = abs(p_c_est - p_c_theory)

    print(f"\nLattice size L = {size}")
    print(f"Estimated p_c ≈ {p_c_est:.3f}")
    print(f"Theoretical p_c = {p_c_theory}")
    print(f"Error = {error:.4f}")

    plot_percolation_curve(p_values, probabilities, p_c_est)

    # Visualize one lattice configuration
    lattice = generate_lattice(size, 0.6)
    plot_lattice(lattice)


if __name__ == "__main__":
    main()