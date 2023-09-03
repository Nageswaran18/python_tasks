def read_and_write(source_file, target_file, source_encoding, target_encoding):
    with open(source_file, "r", encoding=source_encoding, errors='ignore') as source:
        content = source.read()
    
    with open(target_file, "w", encoding=target_encoding) as target:
        target.write(content)

def main():
    source_file = "C:\\Naga\\day_9\\en.txt"  # Modify this to the correct path if needed
    target_file = "es_translated_to_en.txt"  # Provide just the filename
    source_encoding = "iso-8859-1"  # Use the correct encoding for your file
    target_encoding = "utf-16"
    
    read_and_write(source_file, target_file, source_encoding, target_encoding)

if __name__ == '__main__':
    main()
