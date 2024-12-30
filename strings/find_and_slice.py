str = 'X-DSPAM-COnfidence:0.8475'

colpos = str.find(':') # index 18
num = str[colpos+1:] # 0.8475
result = float(num)
print(result)
print(type(result))

# # Original string
# text = "Hello, world! 😊"

# # Encoding the string to bytes
# encoded_text = text.encode('utf-8')

# # Output the encoded bytes
# print("Encoded bytes:", encoded_text)

# # Decoding back to string
# decoded_text = encoded_text.decode('utf-8')
# print("Decoded string:", decoded_text)