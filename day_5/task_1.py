import requests
import csv
import json

baseurl = 'https://api.github.com/users/naveenkrnl/repos'
# endpoint = 'characters'

a = requests.get(baseurl)
# data = a.content
data = a.json()
# print(data)

# print(type(data))
# data = json.loads(data)
# print(type(data))

csv_path = 'C:\\Naga\\day_5\\api_form.csv'

with open(csv_path, mode='w', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['name','description'])  
    for i in data:
        value = [i['name'],i['description']]
        csv_writer.writerow(value)
        print(value)
        
    
    
    
    
    
    



