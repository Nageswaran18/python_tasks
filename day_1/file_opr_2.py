import os

input_path = input('Enter the folder path here: ')
files = []


if not os.path.exists(input_path):
    print("Invalid folder path.")
else:
    for input_txt in os.listdir(input_path):
        if input_txt.endswith('.txt'):
            files.append(input_txt)
    print(files)
    content = ''

    for j in files:
        f = open(os.path.join(input_path, j), 'r') 
        data = f.read()
        print(data)
        data = data + '\n'
        content += data
        f.close()  

    output_path = input("enter your output path:") 

    output_file = open(output_path, 'w')
    output_file.write(content)
    output_file.close()

  
    read_output = open(output_path, 'r')
    print(read_output.read())
    read_output.close()
