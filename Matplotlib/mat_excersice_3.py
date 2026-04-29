import matplotlib.pyplot as plt

# 1. The spatial path (X and Y coordinates in meters)
x_coords = [0, 10, 20, 25, 25, 40, 50]
y_coords = [0,  5,  5, 15, 35, 35, 45]

# 2. The telemetry data: Target speed at each waypoint (meters per second)
# Slower around corners, faster on straightaways, 0 at start/end
speeds = [0.0, 2.5, 2.5, 1.0, 3.0, 3.0, 0.0]

fig, ax = plt.subplots(figsize=(8, 8))

# CRITICAL: Force the X and Y axes to scale equally so the physical geometry isn't distorted
ax.set_aspect('equal')

# Plot the continuous path as a dashed gray line
ax.plot(x_coords, y_coords, color='gray', linestyle='--', linewidth=2, zorder=1, label='Planned Route')

# Scatter the waypoints. 
# c=speeds links the color to the speed data.
# s=100 controls the size of the dots.
waypoint_scatter = ax.scatter(x_coords, y_coords, c=speeds, cmap='coolwarm', s=100, zorder=2)

# Create a Colorbar on the right side to act as a legend for the speeds
cbar = fig.colorbar(waypoint_scatter, ax=ax, fraction=0.046, pad=0.04)
cbar.set_label('Target Speed (m/s)')

# Label the Start Point (Index 0)
ax.annotate('Start Point', 
            xy=(x_coords[0], y_coords[0]), 
            xytext=(-15, 15), textcoords='offset points', 
            fontweight='bold', color='green')

# Label the End Point (Last Index)
ax.annotate('Destination', 
            xy=(x_coords[-1], y_coords[-1]), 
            xytext=(10, -15), textcoords='offset points', 
            fontweight='bold')

# Point an arrow at the sharp turn (Index 3)
ax.annotate('Sharp Turn\n(Speed Drop)', 
            xy=(x_coords[3], y_coords[3]), 
            xytext=(30, -20), textcoords='offset points',
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5))

ax.set_title('Autonomous Trajectory & Velocity Map')
ax.set_xlabel('X Coordinate (m)')
ax.set_ylabel('Y Coordinate (m)')

ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()