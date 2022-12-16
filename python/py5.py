"""
https://platform.stratascratch.com/coding/10156-number-of-units-per-nationality?code_type=2

Number Of Units Per Nationality

Find the number of apartments per nationality that are owned by people under 30 years old. Since a person can own 1 or more properties, duplicates should be removed.
Output the nationality along with the number of apartments.
Sort records by the apartments count in descending order.

<airbnb_hosts> table

host_id: int64
nationality: object
gender: object
age: int64

<airbnb_units> table

host_id: int64
unit_id: object
unit_type: object
n_beds: int64
n_bedrooms: int64
country: object
city: object

"""

# Import your libraries
import pandas as pd

# Start writing code
# df = airbnb_hosts.sort_values(['nationality','age'])
# df_new = df[df['age'] < 30]

combined = pd.merge(airbnb_hosts, airbnb_units)

df = combined.sort_values('age')
df = df[df['age']<30]
df = df[df['unit_type']=='Apartment']

new_df = df.drop_duplicates()

new_df['apartment_count'] = new_df['city'].value_counts().sum()

new_df
