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

n_bins = 6

# Manually set bin edges for temperature, humidity, pressure, and energy_kWh columns
#temp_bins = np.linspace(-30, 30, n_bins+1)
#precipitation_bins = np.linspace(0, 5, n_bins+1)
#irradiance_surface_bins = np.linspace(0, 1000, n_bins+1)
#irradiance_toa_bins = np.linspace(0, 1300, n_bins+1)
#snowfall_bins = np.linspace(0, 17, n_bins+1)
#snowdepth_bins = np.linspace(0, 30, n_bins+1)
#cloud_cover_bins = np.linspace(0, 100, n_bins+1)
#air_density_bins = np.linspace(1.0, 1.5, n_bins+1)
#energy_bins = np.linspace(280000, 564925, n_bins+1)

snowdepth_bins = [0.0,  0.0032, 0.9671, 15.2245, 17.360799999999998, 27.988] 
energy_bins = [283623.0, 355161.5, 375794.0, 394611.5, 414854.0, 440494.0, 564925.0]
temp_bins = [-16.162, -0.8215, 5.363, 12.6695, 19.886, 24.700000000000003, 33.833]
irradiance_surface_bins = [66.757, 282.67580000000004, 410.6121, 552.68285, 708.5123, 837.59285, 994.8331]
irradiance_toa_bins = [533.5116, 609.1935, 789.4702000000001, 985.06545, 1130.1857, 1207.3493500000002, 1229.8585]
snowfall_bins =  [0.0,  0.007050000000000001, 0.1301, 0.63385, 16.6532]
cloud_cover_bins =  [0.01, 0.6006, 0.7868, 0.8761, 0.9292000000000001, 0.9674, 0.997]
air_density_bins =  [1.1379, 1.18565, 1.2079, 1.2375, 1.2654, 1.2963500000000001, 1.4123]
precipitation_bins =  [0.001,  0.1372, 0.2545, 0.53735, 4.6871]



# Discretize temperature, humidity, pressure, and energy_kWh columns into 4 bins each
df['temp '] = pd.cut(df['temperature'], bins=temp_bins, labels=['very low', 'low',  'neutral', 'high', 'very high', 'extremely high'])
df['irradiance_toa '] = pd.cut(df['irradiance_toa'], bins=irradiance_toa_bins, labels=['very low', 'low',  'neutral',  'high', 'very high', 'extremely high'])
df['irradiance_surface '] = pd.cut(df['irradiance_surface'], bins=irradiance_surface_bins, labels=['very low', 'low',  'neutral',  'high', 'very high', 'extremely high'])
df['precipitation '] = pd.cut(df['precipitation'], bins=precipitation_bins, labels=[ 'low',    'high', 'very high', 'extremely high'])
df['snowfall '] = pd.cut(df['snowfall'], bins=snowfall_bins, labels=['low',   'high', 'very high', 'extremely high'])
df['snow_depth '] = pd.cut(df['snow_depth'], bins=snowdepth_bins, labels=[ 'low',  'neutral',  'high', 'very high', 'extremely high'])
df['cloud_cover '] = pd.cut(df['cloud_cover'], bins=cloud_cover_bins, labels=['very low', 'low',  'neutral', 'high', 'very high', 'extremely high'])
df['air_density '] = pd.cut(df['air_density'], bins=air_density_bins, labels=['very low', 'low',  'neutral',  'high', 'very high', 'extremely high'])
df['energy '] = pd.cut(df['Total Energy Use from Electricity (MW)'], bins=energy_bins, labels=['very low', 'low', 'neutral',  'high', 'very high', 'extremely high'])

# Create a dictionary to store bin labels for each column
bin_labels = {'temp_': temp_bins, 'irradiance_toa_': irradiance_toa_bins, 'irradiance_surface_': irradiance_surface_bins,
              'precipitation_': precipitation_bins,# 'snowfall_': snowfall_bins, 'snow_depth_': snowdepth_bins,
              'cloud_cover_': cloud_cover_bins, 'air_density_': air_density_bins, 'energy_': energy_bins}

# Create an empty DataFrame to store the bin labels and their corresponding values
bin_values_df = pd.DataFrame(columns=['bin_label', 'very low', 'low', 'neutral', 'high', 'very high', 'extremely high'])

#for bin in bin_labels.items():
#    #new_row = {'bin_label': bin[0], 'very low': f'{round(bin[1][0],2)} to {round(bin[1][1],2)}', 'low':f'{round(bin[1][1],2)} to {round(bin[1][2],2)}', 'moderately low':f'{round(bin[1][2],2)} to {round(bin[1][3],2)}', 'slightly low':f'{round(bin[1][3],2)} to {round(bin[1][4],2)}', 'neutral':f'{round(bin[1][4],2)} to {round(bin[1][5],2)}', 'slightly high':f'{round(bin[1][5],2)} to {round(bin[1][6],2)}', 'moderately high':f'{round(bin[1][6],2)} to {round(bin[1][7],2)}', 'high':f'{round(bin[1][7],2)} to {round(bin[1][8],2)}', 'very high':f'{round(bin[1][8],2)} to {round(bin[1][9],2)}', 'extremely high':f'{round(bin[1][9],2)} to {round(bin[1][10],2)}'}
#    new_row = {'bin_label': bin[0], 'very low': f'{round(bin[1][0],2)} to {round(bin[1][1],2)}', 'low':f'{round(bin[1][1],2)} to {round(bin[1][2],2)}', 'neutral':f'{round(bin[1][2],2)} to {round(bin[1][3],2)}', 'high':f'{round(bin[1][3],2)} to {round(bin[1][4],2)}', 'very high':f'{round(bin[1][4],2)} to {round(bin[1][5],2)}', 'extremely high':f'{round(bin[1][5],2)} to {round(bin[1][6],2)}'}
#    bin_values_df = bin_values_df.append(new_row, ignore_index=True)
#    print(f'{bin[1][0]} to {bin[1][1]}')

# # Loop through each column and its bin labels to get the values for each bin
# for col, bins in bin_labels.items():
#     values = pd.cut(df[col.replace('_', '')], bins=bins, labels=[f'{bins[i]} - {bins[i+1]}' for i in range(len(bins)-1)])
#     for label in values.unique():
#         bin_values_df.loc[label, 'bin_label'] = col
#         bin_values_df.loc[label, col] = ', '.join(df.loc[values==label, col.replace('_', '')].astype(str).tolist())


# Export the DataFrame to a CSV file
#bin_values_df.to_csv('bin_values.csv', index=False)


# Drop original columns
df = df.drop(['temperature', 'irradiance_toa', 'irradiance_surface', 'precipitation', 'snowfall', 'snow_depth', 'cloud_cover', 'air_density', 'Total Energy Use from Electricity (MW)'], axis=1)

# Convert categorical variables to dummies
df = pd.get_dummies(df)
print(df)
#df.to_csv('test.csv', index=False)
# Run Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.04, use_colnames=True)

# Filter out rows that do not contain "energy_" in the itemset
frequent_itemsets_x = frequent_itemsets[frequent_itemsets['itemsets'].apply(lambda x: any(["energy" in item for item in x]))]
frequent_itemsets_x['itemsets'] = frequent_itemsets_x['itemsets'].apply(lambda x: list(x))

# Create CSV for frequent items 
frequent_itemsets_x.to_csv('frequentItemSets.csv', index=False)
print("Output file 'frequentItemSets.csv' was written successfully!")


## RULES ##

# Generate association rules
rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.04)
#rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)
rules['antecedents'] = rules['antecedents'].apply(lambda x: list(x))
rules['consequents'] = rules['consequents'].apply(lambda x: list(x))
rules = rules[['antecedents', 'consequents', 'support', 'confidence']]
print(rules)

# Filter out rules that don't contain "energy_" in the antecedent or consequent
rules = rules[
    rules['antecedents'].apply(lambda x: any(["energy" in item for item in x])) |
    rules['consequents'].apply(lambda x: any(["energy" in item for item in x]))
]

#Create CSV for rules 
rules.to_csv('Rules.csv', index=False)
print("Output file 'Rules.csv' was written successfully!")

