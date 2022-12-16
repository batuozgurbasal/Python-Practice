"""
https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2

Workers With The Highest Salaries

Find the titles of workers that earn the highest salary. Output the highest-paid title or multiple titles that share the highest salary.

<worker> table

worker_id: int64
first_name: object
last_name: object
salary: int64
joining_date: datetime64[ns]
department: object

<title> table

worker_ref_id: int64
worker_title: object
affected_from: datetime64[ns]

"""
# Import your libraries
import pandas as pd

# Start writing code
df = pd.merge(worker,title,left_on = 'worker_id',right_on = 'worker_ref_id', how = 'inner')
df = df.sort_values('salary',ascending = False)
df = df[df['salary']== df['salary'].max()]
df['best_paid_title'] = df['worker_title']

result = df['best_paid_title']
