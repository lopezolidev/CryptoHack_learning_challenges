'''
Given an unknown key, we must crack the following code.

The only hint to help us is the flag style and the format of the ciphered text

- flag format: crypto{ <- its at most how we can be sure of the content of the flag
- ciphered text format: hexadecimal
- key: unknown 
'''

ciphered_text = '0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104'
# print(len(ciphered_text)) # 84 -> 12 * 7 -> 2 hex digits XOR with each decoded from key 

mssg_prime = 'crypto{'
# first 7 characters of the original message

ciphered_ints = []
# list of ints from the ciphered text

for i in range(0, len(ciphered_text), 2):
    bytes_of_hex = bytes.fromhex(ciphered_text[i:i+2])
    # first extracting the byte represented by 2 hex digits

    clean_bytes = ord(bytes_of_hex)
    # interpreting as integers each byte

    ciphered_ints.append(clean_bytes)
    # appending the ints from hex pair to list of integers from ciphered text

ciphered_ints_short = ciphered_ints[0:7]
# first seven characters of ciphered text so as
# C = M ⊕ K -> c_1 = m_1 ⊕ k_1 ; c_2 = m_2 ⊕ k_2 ; c_3 = m_3 ⊕ k_3 ...
# therefore: 
#     m_1 ⊕ c_1 = m_1 ⊕ m_1 ⊕ k_1 => m_1 ⊕ c_1 = 0 ⊕ k_1 (Self-Inverse)
#     m_1 ⊕ c_1 = 0 ⊕ k_1 => m_1 ⊕ c_1 = k_1 (Identity)
# Subsequently we'll obtain: 
#   m_2 ⊕ c_2 = k_2
#   m_3 ⊕ c_3 = k_3
#   m_4 ⊕ c_4 = k_4
#   m_5 ⊕ c_5 = k_5
#   m_6 ⊕ c_6 = k_6
#   m_7 ⊕ c_7 = k_7


# now we convert the first 7 character of original message (hint) in ints
mssg_prime_int = []

for i in range(0, len(mssg_prime)):
    character_value = ord(mssg_prime[i])
    # ascii value of each character from hint

    mssg_prime_int.append(character_value)
    # appending the int value of each character from int to a list


# unlocking the key from first characters from ciphered message

key = []
# list to store the key

for j in range(0, 7):
    k_temp = ciphered_ints_short[j] ^ mssg_prime_int[j]
    # XOR'ing c_1 and m_1 -> m_1 ⊕ m_1 ⊕ k_1 = k_1

    key.append(k_temp)
    # appending each character of the key to the list

# displaying the key as characters

key_string = ''

for k in range(0,7):
    k_temp_ascii = chr(key[k])
    # obtaining char value according to ASCII code for that character

    key_string += k_temp_ascii
    # appending that character of key into the string

print(key_string)
# myXORke -> clearly, the completed text is: myXORkey (missing y)

y_value = ord('y')
# ascii code value of 'y' character

key.append(y_value)
# appending missing value to the key -> now with length 8

# now it's time to unlock the entire ciphered text

original_mssg = ''

for i in range(0, len(ciphered_ints), len(key)):
    ciphered_substring = ciphered_ints[i: i+len(key)]
    # chunking a substring from ciphered int list to unlock it with key list

    for c, k in zip(ciphered_substring, key):
        unlocked_int = c ^ k
        # XOR'in each ciphered substrind character with each character from key

        unlocked_character = chr(unlocked_int)
        # turning into character the unlocked int

        original_mssg += unlocked_character
        # appending the unlocked character to original message solution

# printing the flag
print(original_mssg)
# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}-
