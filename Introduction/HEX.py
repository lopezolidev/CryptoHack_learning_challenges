'''
- Hexadecimal format is used as a portable / user-friendly format, due to the 
  fact that many encoded characters are not represented by the ASCII format
- Given a hexadecimal list of numbers, we have to obtain the flag 
- bytes.fromhex() function can be used to convert hex to bytes. 
- .hex() instance method can be called on byte strings to get the hex representation. 
'''

hex_string = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

n = 2 
# a hex number is represented by 2 characters

out = []

for i in range(0, len(hex_string), n):
    out.append(hex_string[i: i+n])
    # picking every 2 characters from the original string

res_bytes = ''

for i in range(0, len(out)):
    bytes_val = bytes.fromhex(out[i])
    # converting the string hex value to bytes. These bytes are interpreted as 
    # characters

    int_val = ord(bytes_val)
    # turning byte value to a base-128 value

    char_value = chr(int_val)
    # obtaining ASCII code of such value
    
    res_bytes += char_value


print(res_bytes)





