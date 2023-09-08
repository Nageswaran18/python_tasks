def write_and_read(encoding):
    text = "Hello, 世界!" 
    
   
    with open(f"encoded_text_{encoding}.txt", "w", encoding=encoding) as file:
        file.write(text)
    
    
    with open(f"encoded_text_{encoding}.txt", "r", encoding=encoding) as file:
        content = file.read()
        print(f"Content using {encoding}: {content}")

if __name__ == '__main__':
    encodings = ["utf-8", "utf-16", "utf-32", "utf-8-sig"]  
    for encoding in encodings:
        write_and_read(encoding)




# s = " 世界!" 
# t = s.encode('utf-8')
# print(t)
# print(type(t))
# d = t.decode("utf-8")
# print(d)
# print(type(d))






