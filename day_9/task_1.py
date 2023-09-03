import base64

# sample_text='Nageswaran'
# sample_text_bytes=sample_text.encode('ascii')

# base64_bytes = base64.b64encode(sample_text_bytes)
# base64_string = base64_bytes.decode('ascii')

# print(f'{base64_string}')

# text = 'naga'
# text_bytes = text.encode('ascii')

# convertion_bytes = base64.b64encode(text_bytes)
# convertion_string = convertion_bytes.decode('ascii')

# print(convertion_string) 



# name_string = 'abitha shree'
# name_bytes = name_string.encode('ascii')

# base64_byte = base64.b64encode(name_bytes)
# base64_str = base64_byte.decode('ascii')
# print(base64_str)

# decode_str = 'YWJpdGhhIHNocmVl'
# decode_bytes = decode_str.encode('ascii')

# base_byte = base64.b64decode(decode_bytes)
# base_str = base_byte.decode('ascii')
# print(base_str)


text = 'sweetha'
text_bytes = text.encode('ascii')
base64_bytes = base64.b64encode(text_bytes)
base64_str = base64_bytes.decode('ascii')
print(f'{text}' ':' ''f'{base64_str}')

doc_text = base64_str
doc_text_bytes = doc_text.encode('ascii')
base64_doc_bytes = base64.b64decode(doc_text_bytes)
base64_doc_str = base64_doc_bytes.decode('ascii')
print(f'{base64_str}' ':' ''f'{base64_doc_str}')










