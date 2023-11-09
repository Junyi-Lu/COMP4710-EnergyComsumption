# Owen Hnylycia 
# Comp 4710 Data mining Winter 2023
# Written with the help of ChatGPT

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("Daily_Electricity_Ontario.csv")

# Define the categories and their corresponding colors
categories = [
    'precipitation',
    'temperature',
    'irradiance_surface',
    'irradiance_toa',
    'snowfall',
    'snow_depth',
    'cloud_cover',
    'air_density',
    'Total Energy Use from Electricity (MW)'
]

#bin_ranges = {
#    'precipitation':[ 0.0 ,0.5 ,1.0 ,1.5 ,2.0 ,2.5 ,3.0 ,3.5 ,4.0 ,4.5 ,5.0],
#    'temperature':[-30.0 , -24.0, -18.0, -12.0,-6.0 , 0.0 , 6.0 , 12.0 , 18.0 , 24.0 , 30.0],
#    'irradiance_surface':[ 0.0 ,100.0 ,200.0 ,300.0 ,400.0 ,500.0 ,600.0 ,700.0 ,800.0 ,900.0 ,1000.0 ],
#    'irradiance_toa':[  0.0 ,130.0 ,260.0 ,390.0 ,520.0 ,650.0 ,780.0 ,910.0 ,1040.0 ,1170.0 ,1300.0],
#    'snowfall':[ 0.0 ,1.7 ,3.4 ,5.1 ,6.8 ,8.5 ,10.2 ,11.9 ,13.6 ,15.3 ,17.0],
#    'snow_depth':[ 0.0 ,3.0 ,6.0 ,9.0 ,12.0 ,15.0 ,18.0 ,21.0 ,24.0 ,27.0 ,30.0],
#    'cloud_cover':[ 0.0 ,10.0 ,20.0 ,30.0 ,40.0 ,50.0 ,60.0 ,70.0 ,80.0 ,90.0 ,100.0],
#    'air_density':[ 1.0 ,1.05 ,1.1 ,1.15 ,1.2 ,1.25 ,1.3 ,1.35 ,1.4 ,1.45 ,1.5],
#    'Total Energy Use from Electricity (MW)': [0,280000.0 ,308492.5 ,336985.0 ,365477.5 ,393970.0 ,422462.5 ,450955.0 ,479447.5 ,507940.0 ,536432.5 ,564925.0]
#}

bin_ranges = {
    'precipitation':[0.0 ,0.83 ,1.67 ,2.5 ,3.33 ,4.17 , 5.0],
    'temperature':[-30.0 ,-20.0 ,-10.0 ,0.0 ,10.0 ,20.0 , 30.0],
    'irradiance_surface':[0.0 ,166.67 ,333.33 ,500.0 ,666.67 ,833.33 , 1000.0],
    'irradiance_toa':[0.0 ,216.67 ,433.33 ,650.0 ,866.67 ,1083.33 , 1300.0],
    'snowfall':[0.0 ,2.83 ,5.67 ,8.5 ,11.33 ,14.17 , 17.0],
    'snow_depth':[0.0 ,5.0 ,10.0 ,15.0 ,20.0 ,25.0 , 30.0],
    'cloud_cover':[0.0 ,16.67 ,33.33 ,50.0 ,66.67 ,83.33 , 100.0],
    'air_density':[1.0 ,1.08 ,1.17 ,1.25 ,1.33 ,1.42 , 1.5],
    'Total Energy Use from Electricity (MW)':[0,280000.0 ,327487.5 ,374975.0 ,422462.5 ,469950.0 ,517437.5 , 564925.0], 
}

# Create a bar graph for each category
for col in categories:
    # Count the frequency of each value in the column
    value_counts = df[col].value_counts(bins=bin_ranges[col])

    # Sort the frequency counts by the index value
    value_counts = value_counts.sort_index()

    # Create a bar graph of the frequency counts
    fig, ax = plt.subplots()
    value_counts.plot(kind='bar', ax=ax)
    ax.set_title(f'{col} Frequency')
    ax.set_xlabel('Measurement Value')
    ax.set_ylabel('Frequency')

    # Save the plot , a PNG file
    plt.tight_layout()
    plt.savefig(f'{col}_frequency.png', dpi=300)

    # Show the plot
