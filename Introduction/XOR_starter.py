'''
- XOR operation can be used to encode values by a bitwise operation 
- Converting the starting data types into strings is quite useful to achieve 
  XOR operation among them
- given a starting string, we need to XOR each character with 13 (1101)
- This will give us a new byte for each character, as each character is encoded
  in ASCII (0-127)
- Then concatenate each new character to form a new string
'''

string = "label"
number = 13

encoded_string = ''

for c in string:
    ascii_value = ord(c)
    # ascii value of character from string

    xored_val = ascii_value ^ number
    # applying XOR operation among each character of the label and the number

    xored_char = chr(xored_val)
    # turning the number into a character according to the ascii code

    encoded_string += xored_char
    # appending each encoded character to the encoded string
    
    print(f"ASCII value of {c} is {ascii_value}, xored value with {number} is:")
    print(xored_char)

    
print(encoded_string)
# displaying solution: aloha
