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
        'Coal_Quantity_MTon',
        'Coal_Value_Lac',
        'Petroleum_Quantity_MTon',
        'Petroleum_Value_Lac',
        'NaturalGas_Quantity_MTon',
        'NaturalGas_Value_Lac'
    ]
)

# Populate the dataframe with synthetic data
for month in date_rng:
    for state in states:
        coal_qty = round(np.random.uniform(0.2, 7), 2)
        coal_val = np.random.uniform(12, 15)
        petrol_qty = round(np.random.uniform(0.5, 15), 2)
        petrol_val = np.random.uniform(20, 43)
        ng_qty = round(np.random.uniform(1, 15), 2)
        ng_val = np.random.uniform(15, 36)

        df.loc[(month, state)] = {
            'Coal_Quantity_MTon': coal_qty,
            'Coal_Value_Lac': round(coal_qty * coal_val, 2),
            'Petroleum_Quantity_MTon': petrol_qty,
            'Petroleum_Value_Lac': round(petrol_qty * petrol_val, 2),
            'NaturalGas_Quantity_MTon': ng_qty,
            'NaturalGas_Value_Lac': round(ng_qty * ng_val, 2),
        }

# Save the dataframe to a CSV file
df.to_csv('Data/export_data.csv', index=True)