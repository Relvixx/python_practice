import numpy as np

grid_size = 50

occupency_map = np.zeros((grid_size, grid_size))

occupency_map[10:15, 20:40] = 1
occupency_map[30:40, 10:20] = 1
occupency_map[35:45, 35:45] = 1

print("Map created! total cells : ", occupency_map.size)
print(f"Total obstacle cells: {np.sum(occupency_map):.0f}")

obstacle_chords = np.argwhere(occupency_map == 1)

print(f"\nExtracted coordinates for {len(obstacle_chords)} obstacle cells.")

robot_pos = np.array([18, 45])


distance = np.sqrt(np.sum((obstacle_chords - robot_pos)**2, axis=1))

# np.argmin finds the *index position* of the smallest value in the array
closest_index = np.argmin(distance)

# Use that index to pull the exact coordinate and distance
closest_obstacle = obstacle_chords[closest_index]
min_distance = distance[closest_index]

print(f"\nRobot Position: {robot_pos}")
print(f"Closest Obstacle at: {closest_obstacle}")
print(f"Distance to Collision: {min_distance:.2f} units")