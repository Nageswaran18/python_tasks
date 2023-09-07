import pandas as pd
import os

dictionary = os.getcwd()
csv_file_path= dictionary+'\day_4\employee_task4.csv'

df=pd.read_csv(csv_file_path)

data_dict=df.to_dict(orient='list')
print(df)
print(data_dict)









