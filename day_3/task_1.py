import pandas as pd

csv_file_details=pd.read_csv('C:\\Naga\\day_3\\employee_details.csv')
print(csv_file_details)

csv_file_exp=pd.read_csv('C:\\Naga\\day_3\\employee_experience.csv')
print(csv_file_exp)


csv_merge=pd.merge(
        csv_file_details,
        csv_file_exp, 
        
    )
print(csv_merge)

csv_merge.to_csv('C:\\Naga\\day_3\\csv_merge_data',index=False)



