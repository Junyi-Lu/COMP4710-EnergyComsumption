# Owen Hnylycia 
# Comp 4710 Data mining Winter 2023
# Written with the help of ChatGPT

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("Daily_Electricity_Ontario.csv")

# Set the first column as the index and convert it to a datetime format
df.set_index('time', inplace=True)
df.index = pd.to_datetime(df.index)

# Define the categories and their corresponding colors
categories = {
    'precipitation': 'blue',
    'temperature': 'red',
    'irradiance_surface': 'green',
    'irradiance_toa': 'orange',
    'snowfall': 'purple',
    'snow_depth': 'brown',
    'cloud_cover': 'gray',
    'air_density': 'pink',
    'Total Energy Use from Electricity (MW)': 'black'
}

# Define the height ratio for each subplot
height_ratios = [2, 1, 1, 1, 1, 1, 1, 1, 5]

# Create a subplot for each category
fig, axes = plt.subplots(nrows=len(categories), ncols=1, figsize=(30,50), sharex=True, gridspec_kw={'height_ratios': height_ratios})

# Plot each category with its corresponding color
for i, (col, color) in enumerate(categories.items()):
    axes[i].plot(df.index, df[col], color=color)
    axes[i].set_title(col)
    axes[i].set_ylim(df[col].min() - 0.1*(df[col].max()-df[col].min()), df[col].max() + 0.1*(df[col].max()-df[col].min()))

    
    # Save each subplot to a separate file
    plt.figure(figsize=(16, 8))
    plt.plot(df.index, df[col], color=color)
    plt.title(col)
    plt.xlabel('Date')
    plt.ylabel('Measurement')
    plt.ylim(df[col].min() - 0.1*(df[col].max()-df[col].min()), df[col].max() + 0.1*(df[col].max()-df[col].min()))
    plt.tight_layout()
    plt.savefig(f'{col}.png', dpi=300)
    plt.close()

# Set the title and axis labels for the entire plot
fig.suptitle('Climate and Energy Use Data')
fig.text(0.5, 0.04, 'Date', ha='center')
fig.text(0.04, 0.5, 'Measurement', va='center', rotation='vertical')

# Adjust the subplot layout to avoid overlapping
plt.tight_layout()

# Save the graph to a PNG file with a higher resolution
plt.savefig('lines_colour.png', dpi=300)

# Show the graph
#plt.show()
