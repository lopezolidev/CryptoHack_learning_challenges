'''
- A base64 character encodes 6 bits.
- 4 characters of base64 encode 24 bits
- 24 bits = three bytes
- given the hex string, we need to decode it into bytes, and then encode it
  into base64
- We'll use the library base64 to overcome this challenge
'''

import base64 as b64


hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

n = 6
# 6 hex digits is 3 bytes, which in turn is 4 base64 digits

out = []

for i in range(0, len(hex_string), n):
    out.append(hex_string[i: i+n])
    # picking every 6 characters from the original string

res_bytes = ''

for i in range(0, len(out)):
    bytes_val = bytes.fromhex(out[i])
    # converting the string hex value to bytes. These bytes are interpreted as 
    # characters

    encoded_byte = b64.b64encode(bytes_val)
    # encoding the bytes into base64 format

    decoded_byte = encoded_byte.decode("utf-8")
    # using the '.decode()' method to transform the bytes into legible text

    res_bytes += decoded_byte
    # appending to solution string
    
print(res_bytes)
# crypto/Base+64+Encoding+is+Web+Safe/