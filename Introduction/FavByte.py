'''
- Given a hex string, we must find the flag XOR'ed with a secret byte.
- Given the space of tests (66, 33 possible bytes), and the size of the key (255 different numbers, 0 doesn't count)
  the possible solutions may be found using a brute-force approach 
- We must try all the 255 possible values to decode the string
'''


hex_string = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

for k in range(1, 256):
    res = ''
    # result string started empty

    hex_array = []
    for i in range(0, len(hex_string), 2):
        hex_array.append(hex_string[i:i+2])
        # appending pairs of hex digits

    decoded_result = ''

    for pair in hex_array:
        int_val = int(pair, 16)
        # converting into integer the hex string

        xored_val = int_val ^ k
        # applying XOR with byte value, applying Self-Inverse property

        character_decoded = chr(xored_val)
        # converting back to ASCII character the xored int value

        decoded_result += character_decoded
        # appending solution to result string

    print(decoded_result)

