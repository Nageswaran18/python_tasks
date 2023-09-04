import pandas as pd
import os

class Employee:
    def __init__(self,id,name,age,phone_number):
        self.id=id
        self.name=name
        self.age=age
        self.phone_number=phone_number
        

directory = os.getcwd()
print(directory)
csv_path=directory+"\day_4\emp_details.csv"

df=pd.read_csv(csv_path)

print(df)


employee_list=[]

for index,row in df.iterrows():
    employee=Employee(
        id=row['id'],
        name=row['name'],
        age=row['age'],
        phone_number=row['phone_number']
        
    )
    employee_list.append(employee)
    
    
for emp in employee_list:
    print(vars(emp))









