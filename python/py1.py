"""
https://platform.stratascratch.com/coding/9894-employee-and-manager-salaries?code_type=2

Employee and Manager Salaries

Find employees who are earning more than their managers. Output the employee's first name along with the corresponding salary.

<employee> table

id: int64
first_name: object
last_name: object
age: int64
sex: object
employee_title: object
department: object
salary: int64
target: int64
bonus: int64
email: object
city: object
address: object
manager_id: int64

"""

# Import your libraries
import pandas as pd

# Start writing code
df = employee

df = pd.merge(employee, employee, left_on = 'manager_id',right_on = 'id')

df = df[df['salary_x']> df['salary_y']]

result = df[['first_name_x','salary_x']]
