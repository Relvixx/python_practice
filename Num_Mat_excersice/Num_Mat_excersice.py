import numpy as np
import matplotlib.pyplot as plt

# 1. Create a time array (1440 minutes in a day)
time_minutes = np.linspace(0, 24 * 60, 1440)

# 2. Create a base temperature curve (e.g., motor heating up during operation)
# Starts around 35°C, peaks in the middle, and dips
base_temp = 45 + 20 * np.sin(time_minutes / (4 * 60)) 

# 3. Inject realistic hardware noise
# np.random.normal(mean, standard_deviation, size)
noise = np.random.normal(0, 3.0, size=len(time_minutes))
sensor_readings = base_temp + noise
print(sensor_readings)

# Find the index positions of the highest and lowest temperatures
max_idx = np.argmax(sensor_readings)
min_idx = np.argmin(sensor_readings)

# Extract the exact time and temperature for those indices
max_time, max_temp = time_minutes[max_idx], sensor_readings[max_idx]
min_time, min_temp = time_minutes[min_idx], sensor_readings[min_idx]

print(f"Max Temp: {max_temp:.1f}°C at minute {max_time:.0f}")
print(f"Min Temp: {min_temp:.1f}°C at minute {min_time:.0f}")

# Initialize the figure
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the raw, noisy sensor data in the background
# We divide time by 60 so the X-axis shows hours instead of minutes
ax.plot(time_minutes / 60, sensor_readings, color='lightslategray', alpha=0.5, label='Raw Sensor Data')

# Apply a sliding window moving average to smooth the data
window_size = 45
smoothed_trend = np.convolve(sensor_readings, np.ones(window_size)/window_size, mode='same')
ax.plot(time_minutes / 60, smoothed_trend, color='#4A90E2', linewidth=2.5, label='Smoothed Trendline')

# Highlight Max (Red) and Min (Cyan)
ax.scatter(max_time / 60, max_temp, color='#E05759', s=120, zorder=5, label=f'Peak: {max_temp:.1f}°C')
ax.scatter(min_time / 60, min_temp, color='#59A14F', s=120, zorder=5, label=f'Low: {min_temp:.1f}°C')

# Add text pointing to the maximum value
ax.annotate('Critical Heat Limit', 
            xy=(max_time / 60, max_temp), 
            xytext=(0, 20), textcoords='offset points', 
            ha='center', color='#E05759', fontweight='bold',
            arrowprops=dict(facecolor='#E05759', arrowstyle='->'))

# Format the axes and grid
ax.set_title('Hardware Thermal Profile (24-Hour Simulation)', fontsize=14, fontweight='bold')
ax.set_xlabel('Time (Hours)', fontsize=12)
ax.set_ylabel('Temperature (°C)', fontsize=12)
ax.set_xlim(0, 24)
ax.set_xticks(np.arange(0, 25, 2)) # Force ticks every 2 hours
ax.grid(True, linestyle='--', alpha=0.6)
ax.legend(loc='upper right')

plt.tight_layout()

# Export to a high-resolution PNG file
# dpi=300 ensures it looks crisp in presentations or reports
# bbox_inches='tight' trims any excess white space around the borders
fig.savefig('thermal_profile_export.png', dpi=300, bbox_inches='tight')
print("\nExport complete! Check your project folder for 'thermal_profile_export.png'.")

# Render to the screen
plt.show()