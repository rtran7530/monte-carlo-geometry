"""
Monte Carlo Methods for Geometric Probability Problems
Computational approach to solving the classic problem(s): 
What is the average distance between two random points in a unit square? A unit circle?
"""

import numpy as np
from typing import Tuple, List


def distance_between_points(p1: np.ndarray, p2: np.ndarray) -> float:
    # calculates Eucliean distance (Pythagorean Theorem) between two points
    return np.sqrt(np.sum((p1 - p2) ** 2))


def average_distance_unit_square(num_simulations: int = 100000) -> Tuple[float, List[float]]:
   
    distances = []
    
    for _ in range(num_simulations):
        # generate two random points in unit square
        point1 = np.random.uniform(0, 1, 2)
        point2 = np.random.uniform(0, 1, 2)
        
        # calculate distance
        dist = distance_between_points(point1, point2)
        distances.append(dist)
    
    average_dist = np.mean(distances)
    return average_dist, distances


def generate_random_point_in_circle() -> np.ndarray:

    while True:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            return np.array([x, y])


def average_distance_unit_circle(num_simulations: int = 100000) -> Tuple[float, List[float]]:

    distances = []
    
    for _ in range(num_simulations):
        # generate two random points in unit circle
        point1 = generate_random_point_in_circle()
        point2 = generate_random_point_in_circle()
        
        # calculate distance
        dist = distance_between_points(point1, point2)
        distances.append(dist)
    
    average_dist = np.mean(distances)
    return average_dist, distances


def run_simulations(num_simulations: int = 100000) -> dict:
    # run Monte Carlo
    print(f"Running Monte Carlo simulations with {num_simulations:,} iterations...\n")
    
    # unit square
    avg_dist_square, distances_square = average_distance_unit_square(num_simulations)
    true_square = (np.sqrt(2) + 2 + 5 * np.log(1 + np.sqrt(2))) / 15

    print("Problem 1: Average distance in unit square")
    print(f"Monte Carlo Result: {avg_dist_square:.5f}")
    print(f"Analytical Value: {true_square:.5f}")

    error_percent = abs(avg_dist_square - true_square) / true_square * 100
    print(f"Error: {error_percent:.2f}%\n")
    
    # unit circle
    avg_dist_circle, distances_circle = average_distance_unit_circle(num_simulations)
    true_circle = 128 / (45 * np.pi)
    
    print("Problem 2: Average distance in unit circle")
    print(f"Monte Carlo Result: {avg_dist_circle:.5f}")
    print(f"Analytical Value: {true_circle:.5f}")
    
    error_percent = abs(avg_dist_circle - true_circle) / true_circle * 100
    print(f"Error: {error_percent:.2f}%\n")
    
    return {
        'avg_dist_square': avg_dist_square,
        'distances_square': distances_square,
        'avg_dist_circle': avg_dist_circle,
        'distances_circle': distances_circle
    }


if __name__ == "__main__":
    # run simulations
    results = run_simulations(num_simulations=100000)
    
    print("="*60)
    print("SUMMARY OF RESULTS")
    print("="*60)
    print(f"Average distance (unit square): {results['avg_dist_square']:.5f}")
    print(f"Average distance (unit circle): {results['avg_dist_circle']:.5f}")
    print("="*60)