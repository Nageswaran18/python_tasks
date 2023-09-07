import pandas as pd

csv_file_detail=pd.read_csv('D:\\Naga\\python_tasks\\day_3\\employee_details.csv')

csv_file_monthly_performance=pd.read_csv('D:\\Naga\\python_tasks\\day_3\\employee_monthly_performance.csv')

csv_merger=pd.merge(
    csv_file_detail,
    csv_file_monthly_performance,
)
print(csv_merger)


df=pd.DataFrame(csv_merger,columns=['id','name','age','jan','feb','mar'])
print(df)

new_df=df.groupby('name').agg({'jan':'mean','feb':'mean','mar':'mean'}).reset_index()

print(new_df)

# var=new_df.loc['id']
# print(var)


