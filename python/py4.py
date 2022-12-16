"""
https://platform.stratascratch.com/coding/9915-highest-cost-orders?code_type=2

Highest Cost Orders

Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. 
If customer had more than one order on a certain day, sum the order costs on daily basis. Output customer's first name, total cost of their items, and the date.
For simplicity, you can assume that every first name in the dataset is unique.

<customers> table

id: int64
first_name: object
last_name: object
city: object
address: object
phone_number: object

<orders> table

id: int64
cust_id: int64
order_date: datetime64[ns]
order_details: object
total_order_cost: int64

"""

# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(customers, orders, left_on = 'id',right_on = 'cust_id', how = 'left')
df['order_date'] = pd.to_datetime(df['order_date']).dt.date
df = df.groupby(['first_name','order_date'],as_index = False)['total_order_cost'].sum()
df.sort_values('total_order_cost', ascending = False)
df.loc['2019-02-01':'2019-05-01']
df['order_date'] = pd.to_datetime(df['order_date'], format='%Y-%m-%d')
df = df.loc[(df['order_date'] >= '2019-02-01') & (df['order_date'] <= '2019-05-01')]
df = df[df['total_order_cost'] == df['total_order_cost'].max()]
df['order_date'] = pd.to_datetime(df['order_date']).dt.date

df
