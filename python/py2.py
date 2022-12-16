"""
https://platform.stratascratch.com/coding/10077-income-by-title-and-gender?code_type=2

Income By Title and Gender

Find the average total compensation based on employee titles and gender. Total compensation is calculated by adding both the salary and bonus of each employee. 
However, not every employee receives a bonus so disregard employees without bonuses in your calculation. Employee can receive more than one bonus.
Output the employee title, gender (i.e., sex), along with the average total compensation.

<sf_employee> table

id: int64
first_name: object
last_name: object
age: int64
sex: object
employee_title: object
department: object
salary: int64
target: int64
email: object
city: object
address: object
manager_id: int64

<sf_bonus> table

worker_ref_id: int64
bonus: int64

"""
# Import your libraries
import pandas as pd

# Start writing code
sf_bonus = sf_bonus.groupby('worker_ref_id',as_index = False).sum()
df = pd.merge(sf_employee,sf_bonus, left_on = 'id',right_on = 'worker_ref_id', how = 'inner')
df = df.groupby(['employee_title','sex'],as_index =False).mean()
df = df.dropna()
df['avg_total_comp'] = df['salary'] + df['bonus']
result = df[['employee_title','sex','avg_total_comp']]

result
