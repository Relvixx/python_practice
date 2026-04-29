import matplotlib.pyplot as plt

# 1. The Data (measured in centimeters)
true_distance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Notice how the sensor gets slightly more inaccurate as distance increases
sensor_reading = [10.2, 20.5, 29.8, 41.0, 52.5, 63.8, 75.5, 88.0, 99.5, 112.0]

# Plotting true_distance against itself creates a perfect 1-to-1 diagonal line.
# We make it dashed ('--') and green to indicate it is a reference line.
plt.plot(true_distance, true_distance, color='green', linestyle='--', label='Ideal (Perfect Accuracy)')

# Plot the actual readings as red 'x' markers
plt.scatter(true_distance, sensor_reading, color='red', marker='x', label='Actual Sensor Data') 

# Title and Axis Labels
plt.title('Ultrasonic Sensor Calibration Curve')
plt.xlabel('True Measured Distance (cm)')
plt.ylabel('Sensor Output (cm)')

# Generate the legend and add a background grid for readability
plt.legend()
plt.grid(True)
# Command Matplotlib to open the window and render the graph
plt.show()