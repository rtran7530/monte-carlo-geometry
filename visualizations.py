"""
Visualizations for Monte Carlo geometric probability simulations
"""

import numpy as np
import matplotlib.pyplot as plt
from monte_carlo_geometry import run_simulations, average_distance_unit_square


def plot_distance_distributions(distances_square: list, distances_circle: list):
    """
    Plot histograms of distance distributions for unit square and unit circle.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # unit square distances
    ax1.hist(distances_square, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black')
    ax1.axvline(np.mean(distances_square), color='red', linestyle='--', linewidth=2, 
                label=f'Mean: {np.mean(distances_square):.4f}')
    ax1.set_xlabel('Distance', fontsize=12)
    ax1.set_ylabel('Probability Density', fontsize=12)
    ax1.set_title('Distance Distribution: Unit Square', fontsize=14, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # unit circle distances
    ax2.hist(distances_circle, bins=50, density=True, alpha=0.7, color='green', edgecolor='black')
    ax2.axvline(np.mean(distances_circle), color='red', linestyle='--', linewidth=2,
                label=f'Mean: {np.mean(distances_circle):.4f}')
    ax2.set_xlabel('Distance', fontsize=12)
    ax2.set_ylabel('Probability Density', fontsize=12)
    ax2.set_title('Distance Distribution: Unit Circle', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('distance_distributions.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: distance_distributions.png")
    plt.close()


def plot_convergence(num_samples_list: list = [100, 500, 1000, 5000, 10000, 50000, 100000]):
    """
    Plot how Monte Carlo estimate converges to true value as sample size increases.
    Demonstrates the Law of Large Numbers.
    """
    estimates = []
    true_value = 0.521405
    
    print("\nCalculating convergence for different sample sizes...")
    for n in num_samples_list:
        avg_dist, _ = average_distance_unit_square(n)
        estimates.append(avg_dist)
        error = abs(avg_dist - true_value)
        print(f"  n={n:6d}: estimate = {avg_dist:.5f}, error = {error:.5f}")
    
    # create plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(num_samples_list, estimates, 'bo-', linewidth=2, markersize=8, label='Monte Carlo Estimate')
    ax.axhline(true_value, color='red', linestyle='--', linewidth=2, label=f'Analytical Value: {true_value:.5f}')
    ax.set_xscale('log')
    ax.set_xlabel('Number of Samples (log scale)', fontsize=12)
    ax.set_ylabel('Estimated Average Distance', fontsize=12)
    ax.set_title('Monte Carlo Convergence: Unit Square Average Distance', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('convergence_plot.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: convergence_plot.png")
    plt.close()


def plot_sample_points():
    """
    Visualize random point sampling in unit square and unit circle.
    """
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Unit square sample
    num_points = 1000
    points_square = np.random.uniform(0, 1, (num_points, 2))
    
    ax1.scatter(points_square[:, 0], points_square[:, 1], alpha=0.5, s=20, color='blue')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_aspect('equal')
    ax1.set_xlabel('x', fontsize=12)
    ax1.set_ylabel('y', fontsize=12)
    ax1.set_title(f'Random Points in Unit Square (n={num_points})', fontsize=14, fontweight='bold')
    ax1.grid(True, alpha=0.3)
    
    # unit circle sample with rejection sampling
    points_circle = []
    while len(points_circle) < num_points:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            points_circle.append([x, y])
    points_circle = np.array(points_circle)
    
    # draw circle boundary
    theta = np.linspace(0, 2*np.pi, 100)
    circle_x = np.cos(theta)
    circle_y = np.sin(theta)
    
    ax2.plot(circle_x, circle_y, 'r-', linewidth=2, label='Unit Circle')
    ax2.scatter(points_circle[:, 0], points_circle[:, 1], alpha=0.5, s=20, color='green')
    ax2.set_xlim(-1.2, 1.2)
    ax2.set_ylim(-1.2, 1.2)
    ax2.set_aspect('equal')
    ax2.set_xlabel('x', fontsize=12)
    ax2.set_ylabel('y', fontsize=12)
    ax2.set_title(f'Random Points in Unit Circle (n={num_points})', fontsize=14, fontweight='bold')
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('sample_points.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: sample_points.png")
    plt.close()


if __name__ == "__main__":
    print("="*60)
    print("MONTE CARLO GEOMETRIC PROBABILITY SIMULATIONS")
    print("="*60 + "\n")
    
    # run simulations
    results = run_simulations(num_simulations=100000)
    
    print("\n" + "="*60)
    print("GENERATING VISUALIZATIONS")
    print("="*60)
    
    # generate all plots
    plot_distance_distributions(results['distances_square'], results['distances_circle'])
    plot_convergence()
    plot_sample_points()
    
    print("\n" + "="*60)
    print("COMPLETE - All visualizations saved")
    print("="*60)
    print("\nGenerated files:")
    print("  • distance_distributions.png")
    print("  • convergence_plot.png")
    print("  • sample_points.png")