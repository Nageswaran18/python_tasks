import csv
import json

def con_json(csv_path, json_path):
    data = []
    
    
    with open(csv_path, encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for rows in csv_reader:
            data.append(rows)
            
            # key = rows['name']
            # data[key] = rows
            
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(data, indent=4))
    print('Data conversion completed.')

csv_path = r'C:\\Naga\\day 2\\file.csv'
json_path = r'C:\\Naga\\day 2\\file.json'

con_json(csv_path, json_path)



            
            
            
            
            