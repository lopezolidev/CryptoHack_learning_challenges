'''
Given an unknown key, we must crack the following code.

The only hint to help us is the flag style and the format of the ciphered text

- flag format: crypto{ <- its at most how we can be sure of the content of the flag
- ciphered text format: hexadecimal
- key: unknown -> 'crypto{' is the format of the key needed to unlock the message
'''

ciphered_text = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
# print(len(ciphered_text)) # 84 -> 12 * 7 -> 2 hex digits XOR with each decoded from key 

hint = 'crypto{'# has 7 characters 
# -> the fact is that the original key uses a letter additional to { denotes the '+' character
# before the 'y' in the partial solution  

pairs_ints = []
# here the integervalues from decoded hex will appear

for i in range(0, len(ciphered_text), 2):
    # iterate among the list of ciphered hex in pairs
    x = ciphered_text[i:i+2]
    # taking up a byte (two nibbles = two hex digits)
    
    x = int(x, 16)
    # turning into decimal from base 16

    pairs_ints.append(x)
    # appending the integer value to the pairs array

numeric_hint = []

for char in hint:
    num = ord(char)
    # numeric value of each character of the hint

    numeric_hint.append(num)
    # attaching each numeric value of hint into an array

decoded_string = ''
# string to store decoded solution

for encoded in range(0, len(pairs_ints), 7):
    temp = pairs_ints[encoded: encoded + 7]
    # temporal value of 7-integer chunks to decode using hint by XOR property of Self-inverse

    for num, key in zip(temp, numeric_hint):
        xored_value = num ^ key
        # xoring each numeric character with the corresponding character of numeric hint

        converted_xored_value = chr(xored_value)
        # turning into string the xored value 

        decoded_string += converted_xored_value
        # appending solution to decoded_string solution

print(decoded_string)
'''
Discovered that:

myXORke+y_Q
           HOMe$~seG8bGURNDFWg)a|TM!an
'''

# now then we need to apply this partial key (myXORkey) to find the actual flag

partial_key = 'myXORkey'
# length of 8

decoded_string = ''
# restarting decoded string

numeric_key = []
# array of numeric representation of partial key

for c in partial_key:
    num = ord(c)

    numeric_key.append(num)
# now we have the integer representation of the partial key

for encoded in range(0, len(pairs_ints), 8):
    temp = pairs_ints[encoded: encoded + 8]
    # temporal value of 8-integer chunks to decode using hint by XOR property of Self-inverse

    for num, key in zip(temp, numeric_key):
        xored_value = num ^ key
        # xoring each numeric character with the corresponding character of numeric hint

        converted_xored_value = chr(xored_value)
        # turning into string the xored value 

        decoded_string += converted_xored_value
        # appending solution to decoded_string solution

print(decoded_string)
# voila! crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}