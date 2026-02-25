# Monte Carlo Methods for Geometric Probability

A computational approach to solving the classic problem(s): 
What is the average distance between two random points in a unit square? A unit circle?

## The Problem

![Problem Diagrams](problem_diagrams.png)

**Unit Square:** If you randomly pick two points in a square with sides of length 1, what is the expected distance between them?

**Unit Circle:** What about if the points are in a circle with radius 1?

These problems are difficult to solve analytically (they require complex multivariable calculus), but Monte Carlo simulation provides an elegant computational solution.

## Monte Carlo Approach

Instead of solving with calculus:
1. Generate 100,000 pairs of random points
2. Calculate the distance for each pair
3. Average all the distances

This approximates the analytical solution with high accuracy.

## Results

| Geometry | Monte Carlo Result | Analytical Value | Error |
|----------|-------------------|------------------|-------|
| Unit Square | ~0.521405 | 0.521405 | <0.01% |
| Unit Circle | ~0.905414 | 128/(45π) ≈ 0.905414 | <0.01% |

## Implementation

### Core Algorithm
```python
distances = []
for i in range(100000):
    point1 = random_point_in_square()
    point2 = random_point_in_square()
    distance = calculate_distance(point1, point2)
    distances.append(distance)

average_distance = mean(distances)
```

### Key Techniques
- **Random sampling:** Generating uniform random points
- **Rejection sampling:** For uniform distribution within circles
- **Convergence analysis:** Demonstrating the Law of Large Numbers
- **Statistical visualization:** Plotting distributions and convergence

## Files

- `monte_carlo_geometry.py` - Core Monte Carlo simulation functions
- `visualizations.py` - Plotting and visualization code  
- `README.md` - This file
- `requirements.txt` - Python dependencies

## Installation & Usage
```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run simulations
python monte_carlo_geometry.py

# Generate visualizations
python visualizations.py
```

## Visualizations

The code generates three plots:

1. **Distance Distributions** - Histograms showing how distances are distributed
2. **Convergence Plot** - Demonstrates how accuracy improves with more samples
3. **Sample Points** - Visual representation of random point generation

## Mathematical Background

Monte Carlo methods rely on the **Law of Large Numbers**: as sample size increases, the sample average converges to the expected value.

Accuracy improves with √n:
- 100 samples → ±10% error
- 10,000 samples → ±1% error
- 100,000 samples → ±0.1% error

## Applications of Monte Carlo Methods

- Financial modeling (options pricing, risk analysis)
- Physics simulations (particle interactions, quantum mechanics)
- Machine learning (reinforcement learning, Bayesian inference)
- Computer graphics (ray tracing, global illumination)

## Author

**Robert Tran**  
Applied Mathematics & Computer Science  
San Diego State University