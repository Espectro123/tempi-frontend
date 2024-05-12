import pandas as pd

def export_to_excel(data):
    print("THE DATA IS: ")
    print(data)
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
    pivot_df = df.pivot(index=['Date', 'Time'], columns='Sensor', values='temperature').reset_index()

    # Save the pivoted DataFrame to an Excel file using the 'openpyxl' engine
    pivot_df.to_excel('tempi_experiment.xlsx', index=False, engine='openpyxl')

