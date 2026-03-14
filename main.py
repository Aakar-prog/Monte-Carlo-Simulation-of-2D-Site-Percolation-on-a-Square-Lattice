import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) # Set random seed for preproducibility

from percolation.lattice import generate_lattice
from percolation.simulation import sweep_probabilities, estimate_threshold
from percolation.visualization import plot_lattice


def main():              

    sizes = [20, 40, 60]   # Different lattice sizes used to study finite-size effects
                           #sizes = [20, 40, 60]
    trials = 100
    p_c_theory = 0.5927

    p_values = np.linspace(0.3, 0.8, 20)

    plt.figure()

    for size in sizes:

        probabilities = sweep_probabilities(size, p_values, trials)

        p_c_est = estimate_threshold(p_values, probabilities)

        error = abs(p_c_est - p_c_theory)

        print(f"\nLattice size L = {size}")
        print(f"Estimated p_c ≈ {p_c_est:.3f}")
        print(f"Theoretical p_c = {p_c_theory}")
        print(f"Error = {error:.4f}")

        plt.plot(p_values, probabilities, marker="o", label=f"L = {size}")

    # theoretical threshold
    plt.axvline(p_c_theory, color="red", linestyle="--", label="Theory $p_c$")

    plt.xlabel("Occupation probability p")
    plt.ylabel("Percolation probability")
    plt.title("Finite-Size Comparison of Percolation Transition")
    plt.legend()

    plt.show()

    # visualize one lattice
    lattice = generate_lattice(60, 0.6)
    plot_lattice(lattice)


if __name__ == "__main__":
    main()