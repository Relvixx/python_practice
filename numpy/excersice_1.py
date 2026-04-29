import numpy as np

raw_sensor_data = np.random.normal(50,2,100)

raw_sensor_data[15] = -345.0
raw_sensor_data[47] = 999.
raw_sensor_data[65] = -13.8

print(raw_sensor_data)

valid_mask = (raw_sensor_data > 0) & (raw_sensor_data < 100)

filter_data = raw_sensor_data[valid_mask]
print("\n After removing glitches:", len(filter_data))

window_size = 10

window = np.ones(window_size)/ window_size

smooth_data = np.convolve(filter_data, window, mode = "valid")

print("\nFinal Smoothed Data (first 5):", smooth_data[:5])