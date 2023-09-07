import pandas as pd
import numpy as np

data= pd.read_csv('D:\\Naga\\python_tasks\\day_4\\emp.csv',delimiter=',')
# print('original dataframe')
# print(detail)
# print()


all=pd.DataFrame(data)
print('total dataframe')
print(all)
print()

#rows and colums count
print("No of rows and colum present in the csv file")
print(all.shape)
print()

#sum of the salary in the csv file
print('salary in the given data')
emp_salary=all['Salary'].sum()
print(emp_salary)
print()

#mean of age and salary...
grouped=all.groupby('Name').agg({'Age':'mean','Salary':'sum'})
print(grouped)
print()

#Distint...
Distint_state=all['State'].unique()
print(Distint_state)
print()

#filter rows....
filter_rows=all[all['Age']>22]
print(filter_rows)
print()

#filter colums...
filter_colums=all[['Name','Salary']]
print(filter_colums)
print()

#checking null....
check_null=all['Salary'].isnull().sum()
print(check_null)
print()

#range....
range_number=all[(all['Salary']>11000)] 
print(range_number)

#regex...
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
valid_emails = all[all['Email'].str.match(email_pattern)]
print("Valid Email IDs:")
print(valid_emails)
































