import pandas as pd
import numpy as np

# Define states
states = [
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Chhattisgarh',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'Odisha',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal'
]

# Create an empty dataframe
date_rng = pd.date_range(start = '1/1/2020', end = '1/12/2023', freq = 'M')
index = pd.MultiIndex.from_product(
    [date_rng, states],
    names = [
        'Month',
        'State'
    ]
)
df = pd.DataFrame(
    index = index,
    columns = [
        'Coal_Production_TWh',
        'Coal_Consumption_TWh',
        'Petroleum_Production_TWh',
        'Petroleum_Consumption_TWh',
        'NaturalGas_Production_TWh',
        'NaturalGas_Consumption_TWh'
    ]
)

# Populate the dataframe with synthetic data
for month in date_rng:
    for state in states:
        df.loc[(month, state)] = {
            'Coal_Production_TWh': np.random.uniform(1, 10),
            'Coal_Consumption_TWh': np.random.uniform(1, 10),
            'Petroleum_Production_TWh': np.random.uniform(0.5, 5),
            'Petroleum_Consumption_TWh': np.random.uniform(0.5, 5),
            'NaturalGas_Production_TWh': np.random.uniform(2, 15),
            'NaturalGas_Consumption_TWh': np.random.uniform(2, 15),
        }

# Save the dataframe to a CSV file
df.to_csv('energy_data.csv', index=True)