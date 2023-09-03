import pandas as pd


csv_file_path='C:\\Naga\\day_4\\employee_task4.csv'

df=pd.read_csv(csv_file_path)

data_dict=df.to_dict(orient='list')
print(df)
print(data_dict)









