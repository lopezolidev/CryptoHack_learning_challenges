'''
- given a ciphered text and an unknown key, find the original message
- hint: all the flags start by the same string of characters: crypto{
'''

ciphered_message = '10070915061c1e18511108460218'

hint = 'crypto{'


ciphered_ints = []
# list of ints from the ciphered text

for i in range(0, len(ciphered_message), 2):
    bytes_of_hex = bytes.fromhex(ciphered_message[i:i+2])
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

for i in range(0, len(hint)):
    character_value = ord(hint[i])
    # ascii value of each character from hint

    mssg_prime_int.append(character_value)
    # appending the int value of each character from int to a list


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
# crypto{k$am4q}