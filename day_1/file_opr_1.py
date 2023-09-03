file_name=input('Enter the path:')
with open(file_name,'w')as f:
    f.write(input())

with open(file_name,'r')as f:
    print(f.read())