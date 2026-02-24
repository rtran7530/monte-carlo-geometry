"""
Monte Carlo Methods for Geometric Probability Problems
Computational approach to solving the classic problem(s): 
What is the average distance between two random points in a unit square? A unit circle?
"""

import numpy as np
from typing import Tuple, List


def distance_between_points(p1: np.ndarray, p2: np.ndarray) -> float:
    """
    Calculate Euclidean distance between two points.
    
    Args:
        p1: First point as numpy array [x, y]
        p2: Second point as numpy array [x, y]
    
    Returns:
        Euclidean distance between points
    """
    return np.sqrt(np.sum((p1 - p2) ** 2))


def average_distance_unit_square(num_simulations: int = 100000) -> Tuple[float, List[float]]:
    """
    Calculate average distance between two random points in a unit square using Monte Carlo.
    
    The unit square is defined as [0,1] x [0,1].
    
    Args:
        num_simulations: Number of Monte Carlo iterations
    
    Returns:
        Tuple of (average_distance, list_of_all_distances)
    """
    distances = []
    
    for _ in range(num_simulations):
        # Generate two random points in unit square
        point1 = np.random.uniform(0, 1, 2)
        point2 = np.random.uniform(0, 1, 2)
        
        # Calculate distance
        dist = distance_between_points(point1, point2)
        distances.append(dist)
    
    average_dist = np.mean(distances)
    return average_dist, distances


def generate_random_point_in_circle() -> np.ndarray:
    """
    Generate a random point uniformly distributed in a unit circle.
    
    Uses rejection sampling: generate random point in square [-1,1] x [-1,1]
    and reject if outside unit circle.
    
    Returns:
        Random point [x, y] inside unit circle
    """
    while True:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            return np.array([x, y])


def average_distance_unit_circle(num_simulations: int = 100000) -> Tuple[float, List[float]]:
    """
    Calculate average distance between two random points in a unit circle using Monte Carlo.
    
    Points are generated using rejection sampling to ensure uniform distribution.
    
    Args:
        num_simulations: Number of Monte Carlo iterations
    
    Returns:
        Tuple of (average_distance, list_of_all_distances)
    """
    distances = []
    
    for _ in range(num_simulations):
        # Generate two random points in unit circle using rejection sampling
        point1 = generate_random_point_in_circle()
        point2 = generate_random_point_in_circle()
        
        # Calculate distance
        dist = distance_between_points(point1, point2)
        distances.append(dist)
    
    average_dist = np.mean(distances)
    return average_dist, distances


def run_simulations(num_simulations: int = 100000) -> dict:
    """
    Run Monte Carlo simulations for both unit square and unit circle.
    
    Args:
        num_simulations: Number of iterations for each simulation
    
    Returns:
        Dictionary containing all simulation results
    """
    print(f"Running Monte Carlo simulations with {num_simulations:,} iterations...\n")
    
    # Unit square
    print("Problem 1: Average distance between two random points in unit square")
    avg_dist_square, distances_square = average_distance_unit_square(num_simulations)
    print(f"Monte Carlo Result: {avg_dist_square:.6f}")
    print(f"Analytical Value:   ~0.521405\n")
    
    # Unit circle
    print("Problem 2: Average distance between two random points in unit circle")
    avg_dist_circle, distances_circle = average_distance_unit_circle(num_simulations)
    print(f"Monte Carlo Result: {avg_dist_circle:.6f}")
    print(f"Analytical Value:   ~0.905414 (128/(45π))\n")
    
    return {
        'avg_dist_square': avg_dist_square,
        'distances_square': distances_square,
        'avg_dist_circle': avg_dist_circle,
        'distances_circle': distances_circle
    }


if __name__ == "__main__":
    # Run simulations
    results = run_simulations(num_simulations=100000)
    
    print("="*60)
    print("SUMMARY OF RESULTS")
    print("="*60)
    print(f"Average distance (unit square): {results['avg_dist_square']:.6f}")
    print(f"Average distance (unit circle): {results['avg_dist_circle']:.6f}")
    print("="*60)