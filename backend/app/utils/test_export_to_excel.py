import pandas as pd
from datetime import datetime

# Sample data array of dictionaries, adjusted to have same timestamps for a group of five readings
data = [
    {'Temperature': 22, 'timestamp': '2024-05-12T17:36:24.682765'},
    {'Temperature': 23, 'timestamp': '2024-05-12T17:36:24.682765'},
    {'Temperature': 24, 'timestamp': '2024-05-12T17:36:24.682765'},
    {'Temperature': 25, 'timestamp': '2024-05-12T17:36:24.682765'},
    {'Temperature': 26, 'timestamp': '2024-05-12T17:36:24.682765'},
    {'Temperature': 27, 'timestamp': '2024-04-24T22:37:26.440734'},
    {'Temperature': 28, 'timestamp': '2024-04-24T22:37:26.440734'},
    {'Temperature': 29, 'timestamp': '2024-04-24T22:37:26.440734'},
    {'Temperature': 30, 'timestamp': '2024-04-24T22:37:26.440734'},
    {'Temperature': 31, 'timestamp': '2024-04-24T22:37:26.440734'},
]

# Convert to DataFrame
df = pd.DataFrame(data)

# Convert timestamp strings to datetime objects
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Extract Date and Time
df['Date'] = df['timestamp'].dt.date
df['Time'] = df['timestamp'].dt.time

# Assign sensor numbers by index within each timestamp group
df['Sensor'] = 'Sensor ' + (df.groupby('timestamp').cumcount() + 1).astype(str)

# Pivot table to widen the DataFrame
pivot_df = df.pivot(index=['Date', 'Time'], columns='Sensor', values='Temperature').reset_index()


# Save the pivoted DataFrame to an Excel file using the 'openpyxl' engine
pivot_df.to_excel('sensor_readings.xlsx', index=False, engine='openpyxl')

print(df)