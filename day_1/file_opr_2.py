import os

input_path = input('Enter the folder path here: ')
files = []

 #check the path is exit or not..
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
        f.close()  # closing the file 

    output_path = 'C:\\Naga\\day 1\\all_files.txt' 

    output_file = open(output_path, 'w')
    output_file.write(content)
    output_file.close()

    # Reopen and read the output file
    read_output = open(output_path, 'r')
    print(read_output.read())
    read_output.close()
