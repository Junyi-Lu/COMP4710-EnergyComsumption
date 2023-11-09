#############
#Dont remove non energy frequent itemsets
#####################

import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import numpy as np

# Read CSV file
df = pd.read_csv('Daily_Electricity_Ontario.csv')

# Drop date and hour columns
df = df.drop(['time'], axis=1)

n_bins = 10

# Manually set bin edges for temperature, humidity, pressure, and energy_kWh columns
temp_bins = np.linspace(-30, 30, n_bins+1)
precipitation_bins = np.linspace(0, 5, n_bins+1)
irradiance_surface_bins = np.linspace(0, 1000, n_bins+1)
irradiance_toa_bins = np.linspace(0, 1300, n_bins+1)
snowfall_bins = np.linspace(0, 17, n_bins+1)
snowdepth_bins = np.linspace(0, 30, n_bins+1)
cloud_cover_bins = np.linspace(0, 100, n_bins+1)
air_density_bins = np.linspace(1.0, 1.5, n_bins+1)
energy_bins = np.linspace(280000, 564925, n_bins+1)

# Discretize temperature, humidity, pressure, and energy_kWh columns into 4 bins each
df['temp_'] = pd.cut(df['temperature'], bins=temp_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['irradiance_toa_'] = pd.cut(df['irradiance_toa'], bins=irradiance_toa_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['irradiance_surface_'] = pd.cut(df['irradiance_surface'], bins=irradiance_surface_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['precipitation_'] = pd.cut(df['precipitation'], bins=precipitation_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['snowfall_'] = pd.cut(df['snowfall'], bins=snowfall_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['snow_depth_'] = pd.cut(df['snow_depth'], bins=snowdepth_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['cloud_cover_'] = pd.cut(df['cloud_cover'], bins=cloud_cover_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['air_density_'] = pd.cut(df['air_density'], bins=air_density_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])
df['energy_'] = pd.cut(df['Total Energy Use from Electricity (MW)'], bins=energy_bins, labels=['very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])

# Create a dictionary to store bin labels for each column
bin_labels = {'temp_': temp_bins, 'irradiance_toa_': irradiance_toa_bins, 'irradiance_surface_': irradiance_surface_bins,
              'precipitation_': precipitation_bins, 'snowfall_': snowfall_bins, 'snow_depth_': snowdepth_bins,
              'cloud_cover_': cloud_cover_bins, 'air_density_': air_density_bins, 'energy_': energy_bins}

# Create an empty DataFrame to store the bin labels and their corresponding values
bin_values_df = pd.DataFrame(columns=['bin_label', 'very low', 'low', 'moderately low', 'slightly low', 'neutral', 'slightly high', 'moderately high', 'high', 'very high', 'extremely high'])

for bin in bin_labels.items():
    new_row = {'bin_label': bin[0], 'very low': f'{round(bin[1][0],2)} to {round(bin[1][1],2)}', 'low':f'{round(bin[1][1],2)} to {round(bin[1][2],2)}', 'moderately low':f'{round(bin[1][2],2)} to {round(bin[1][3],2)}', 'slightly low':f'{round(bin[1][3],2)} to {round(bin[1][4],2)}', 'neutral':f'{round(bin[1][4],2)} to {round(bin[1][5],2)}', 'slightly high':f'{round(bin[1][5],2)} to {round(bin[1][6],2)}', 'moderately high':f'{round(bin[1][6],2)} to {round(bin[1][7],2)}', 'high':f'{round(bin[1][7],2)} to {round(bin[1][8],2)}', 'very high':f'{round(bin[1][8],2)} to {round(bin[1][9],2)}', 'extremely high':f'{round(bin[1][9],2)} to {round(bin[1][10],2)}'}
    bin_values_df = bin_values_df.append(new_row, ignore_index=True)
    print(f'{bin[1][0]} to {bin[1][1]}')

# # Loop through each column and its bin labels to get the values for each bin
# for col, bins in bin_labels.items():
#     values = pd.cut(df[col.replace('_', '')], bins=bins, labels=[f'{bins[i]} - {bins[i+1]}' for i in range(len(bins)-1)])
#     for label in values.unique():
#         bin_values_df.loc[label, 'bin_label'] = col
#         bin_values_df.loc[label, col] = ', '.join(df.loc[values==label, col.replace('_', '')].astype(str).tolist())


# Export the DataFrame to a CSV file
bin_values_df.to_csv('bin_values.csv', index=False)


# Drop original columns
df = df.drop(['temperature', 'irradiance_toa', 'irradiance_surface', 'precipitation', 'snowfall', 'snow_depth', 'cloud_cover', 'air_density', 'Total Energy Use from Electricity (MW)'], axis=1)

# Convert categorical variables to dummies
df = pd.get_dummies(df)
print(df);
# Run Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.10, use_colnames=True)

# Filter out rows that do not contain "energy_" in the itemset
frequent_itemsets_x = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: any(["energy_" in item for item in x]))]
frequent_itemsets_x['itemsets'] = frequent_itemsets_x['itemsets'].apply(lambda x: list(x))

# Create CSV for frequent items 
frequent_itemsets_x.to_csv('frequentItemSets.csv', index=False)
print("Output file 'frequentItemSets.csv' was written successfully!")


## RULES ##

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x))
rules['consequents'] = rules['consequents'].apply(lambda x: list(x))
rules = rules[['antecedents', 'consequents', 'support', 'confidence']]

# Filter out rules that don't contain "energy_" in the antecedent or consequent
rules = rules[
    rules['antecedents'].apply(lambda x: any(["energy_" in item for item in x])) |
    rules['consequents'].apply(lambda x: any(["energy_" in item for item in x]))
]

#Create CSV for rules 
rules.to_csv('Rules.csv', index=False)
print("Output file 'Rules.csv' was written successfully!")

