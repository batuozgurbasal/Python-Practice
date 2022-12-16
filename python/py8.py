"""
https://platform.stratascratch.com/coding/10049-reviews-of-categories?code_type=2

Reviews of Categories

Find the top business categories based on the total number of reviews. 
Output the category along with the total number of reviews. Order by total reviews in descending order.

<yelp_business> table

business_id: object
name: object
neighborhood: object
address: object
city: object
state: object
postal_code: object
latitude: float64
longitude: float64
stars: float64
review_count: int64
is_open: int64
categories: object

"""

# Import your libraries
import pandas as pd

# Start writing code
df = yelp_business
df['new_caregories'] = df['categories'].str.split(";")
df = df.explode('new_caregories')
df = df.groupby('new_caregories',as_index = False)['review_count'].sum()
df = df.sort_values('review_count', ascending = False)
