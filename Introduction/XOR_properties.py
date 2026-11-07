'''
XOR properties are
Commutative: A ⊕ B = B ⊕ A
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

Given the following

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

Utilize XOR properties to decode the flag
'''

k1 = 'a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313'

k2_XOR_k1 = '37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e'

k2_XOR_k3 = 'c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1'

flag_XOR_k1_XOR_k3_XOR_k2 = '04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf'

def from_hex_to_bytes(hex_number):
    res = int(hex_number, 16)
    # converting the hex number into an integer, specifying the base (16)

    return res


k1_int = from_hex_to_bytes(k1)

k2_XOR_k1_int = from_hex_to_bytes(k2_XOR_k1)

k2_XOR_k3_int = from_hex_to_bytes(k2_XOR_k3)

flag_XOR_k1_XOR_k3_XOR_k2_int = from_hex_to_bytes(flag_XOR_k1_XOR_k3_XOR_k2)

# now we proceed with XOR operations

flag_XOR_k1 = flag_XOR_k1_XOR_k3_XOR_k2_int ^ k2_XOR_k3_int
# applying Associative, Commutative and Identity properties

flag_dec = flag_XOR_k1 ^ k1_int
# using Self-Inverse property

flag_hex = hex(flag_dec)
# transforming the flag decimal string into hexadecimal string

decoded_flag = ''

for i in range(0, len(flag_hex), 2):
    chunk = flag_hex[i:i+2]
    # chunking the original hex string into 2 character strings

    if chunk == '0x':
        decoded_flag += ''
        continue
    # ignoring the first '0x' string

    integer_nibble = int(chunk, 16)
    # obtaining the integer nibble from hex chunk

    character_nibble = chr(integer_nibble)
    # converting the integer value into the ASCII character

    decoded_flag += character_nibble
    # appending string to solution

print(decoded_flag)
# crypto{x0r_i5_ass0c1at1v3}



