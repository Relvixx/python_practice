import matplotlib.pyplot as plt
import numpy as np

# Dataset 1: Passenger Volume (For the Bar Chart)
stops = ['CBS', 'Nashik Road', 'Panchavati', 'Satpur', 'Pathardi Phata']
boardings = [1250, 2100, 850, 1400, 600]

# Dataset 2: Travel Time via AI Routing (For the Line Chart)
# Simulating hours from 6 AM to 8 PM (6 to 20)
hours = np.arange(6, 21)
# Base travel time fluctuating throughout the day (Peak traffic around 10 AM and 6 PM)
avg_travel_time = [20, 22, 28, 35, 40, 32, 25, 24, 25, 28, 30, 35, 42, 45, 30]
# Variance represents the unpredictability of traffic (wider band during rush hour)
variance = np.array([2, 3, 5, 8, 10, 6, 3, 3, 4, 5, 6, 8, 12, 15, 4])
# Create a figure that is 12 inches wide and 5 inches tall, containing 1 row and 2 columns
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
# Create the bar chart on the left axis
ax1.bar(stops, boardings, color='#4A90E2')

# Customize the left axis
ax1.set_title('Daily Passenger Boardings per Hub')
ax1.set_ylabel('Total Passengers')
# Rotate the stop names by 45 degrees so they do not overlap each other
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', linestyle='--', alpha=0.7)
# Plot the main average time line
ax2.plot(hours, avg_travel_time, color='#E05759', linewidth=2, label='Avg Travel Time')

# Fill the area between (Average - Variance) and (Average + Variance)
ax2.fill_between(hours, 
                 avg_travel_time - variance, 
                 avg_travel_time + variance, 
                 color='#E05759', alpha=0.2, label='Traffic Variance')

# Customize the right axis
ax2.set_title('Network Travel Time Fluctuations')
ax2.set_xlabel('Time of Day (24hr)')
ax2.set_ylabel('Minutes')
ax2.set_xticks(hours) # Force the X-axis to show every hour
ax2.legend()
ax2.grid(True, alpha=0.3)
# Adjust layout to prevent clipping of titles or rotated labels
plt.tight_layout()

# Render the dashboard
plt.show()