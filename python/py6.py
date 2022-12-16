"""
https://platform.stratascratch.com/coding/10322-finding-user-purchases?code_type=2

Finding User Purchases

Write a query that'll identify returning active users. A returning active user is a user that has made a second purchase within 7 days of any other of their purchases. 
Output a list of user_ids of these returning active users.

<amazon_transactions> table

id: int64
user_id: int64
item: object
created_at: datetime64[ns]
revenue: int64

"""

# Import your libraries
import pandas as pd

# Start writing code
df = amazon_transactions.sort_values(['user_id','created_at'])
df['diff'] = df.groupby('user_id')['created_at'].diff()
df[df['diff']  <= pd.Timedelta(days=7)]['user_id'].unique()
