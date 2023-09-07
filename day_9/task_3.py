def read_and_write(source_file, target_file, source_encoding, target_encoding):
    with open(source_file, "r", encoding=source_encoding, errors='ignore') as source:
        content = source.read()
    
    with open(target_file, "w", encoding=target_encoding) as target:
        target.write(content)


def main():
    source_file = "D:\\Naga\\python_tasks\\day_9\\en.txt"  
    target_file = "es_translated_to_en.txt"  
    source_encoding = "iso-8859-1" 
    target_encoding = "utf-16"
    
    read_and_write(source_file, target_file, source_encoding, target_encoding)

if __name__ == '__main__':
    main()
