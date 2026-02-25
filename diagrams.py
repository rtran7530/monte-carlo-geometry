import matplotlib.pyplot as plt
import numpy as np

# Create figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Unit Square
square = plt.Rectangle((0, 0), 1, 1, fill=False, edgecolor='m', linewidth=3)
ax1.add_patch(square)

# Two random points in square
p1 = np.random.uniform(0, 1, 2)
p2 = np.random.uniform(0, 1, 2)

ax1.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-', linewidth=2, alpha=0.5, label=f'Distance')
ax1.plot(p1[0], p1[1], 'ro', markersize=10, label='Point 1')
ax1.plot(p2[0], p2[1], 'bo', markersize=10, label='Point 2')

ax1.set_xlim(-0.5, 1.5)
ax1.set_ylim(-0.5, 1.5)
ax1.set_aspect('equal')
ax1.set_xlabel('x', fontsize=12)
ax1.set_ylabel('y', fontsize=12)
ax1.set_title('Unit Square [0,1] × [0,1]', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend(loc = 'upper left', fontsize=10)

# Unit Circle
theta = np.linspace(0, 2*np.pi, 100)
x_circle = np.cos(theta)
y_circle = np.sin(theta)
ax2.plot(x_circle, y_circle, 'm-', linewidth=3)

# Two random points in circle
def random_point_in_circle():
    while True:
        x = np.random.uniform(-1, 1)
        y = np.random.uniform(-1, 1)
        # checks if point lies inside the circle
        if x**2 + y**2 <= 1:
            return np.array([x, y])

c1 = random_point_in_circle()
c2 = random_point_in_circle()

ax2.plot([c1[0], c2[0]], [c1[1], c2[1]], color = '#000000', linestyle = '-', linewidth=2, alpha=0.5, label='Distance')
ax2.plot(c1[0], c1[1], 'ro', markersize=10, label='Point 1')
ax2.plot(c2[0], c2[1], 'bo', markersize=10, label='Point 2')

ax2.set_xlim(-1.8, 1.8)
ax2.set_ylim(-1.8, 1.8)
ax2.set_aspect('equal')
ax2.set_xlabel('x', fontsize=12)
ax2.set_ylabel('y', fontsize=12)
ax2.set_title('Unit Circle (r = 1)', fontsize=14, fontweight='bold')
ax2.grid(True, alpha=0.3)
ax2.legend(loc = 'upper left', fontsize=10)

plt.tight_layout()
plt.savefig('problem_diagrams.png', dpi=300, bbox_inches='tight')
print("✓ Saved: problem_diagrams.png")
plt.close()