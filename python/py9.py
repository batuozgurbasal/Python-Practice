"""
https://platform.stratascratch.com/coding/9726-classify-business-type?code_type=2

Classify Business Type

Classify each business as either a restaurant, cafe, school, or other. 
A restaurant should have the word 'restaurant' in the business name. For cafes, either 'cafe', 'café', or 'coffee' can be in the business name. 
'School' should be in the business name for schools. All other businesses should be classified as 'other'. Output the business name and the calculated classification.

<sf_restaurant_health_violations> table
business_id: int64
business_name: object
business_address: object
business_city: object
business_state: object
business_postal_code: float64
business_latitude: float64
business_longitude: float64
business_location: object
business_phone_number: float64
inspection_id: object
inspection_date: datetime64[ns]
inspection_score: float64
inspection_type: object
violation_id: object
violation_description: object
risk_category: object

"""

# Import your libraries
import pandas as pd
# Start writing code
df = sf_restaurant_health_violations
df_other = df[~df['business_name'].str.contains("(?i)school|restaurant|cafe|café|coffee")]
df_other['business_type'] = 'other'
df_school = df[df["business_name"].str.contains("(?i)school")]
df_school['business_type'] = 'school'
df_rest = df[df["business_name"].str.contains("(?i)restaurant")]
df_rest['business_type'] = 'restaurant'
df_cafe = df[df["business_name"].str.contains('(?i)cafe|café|coffee')]
df_cafe['business_type'] = 'cafe'
df_comb1 = pd.merge(df_other,df_school, how = 'outer')
df_comb2 = pd.merge(df_rest,df_cafe, how = 'outer')
result = pd.merge(df_comb1, df_comb2, how= 'outer')
result.drop_duplicates()
result = result[['business_name','business_type']].drop_duplicates()
result
