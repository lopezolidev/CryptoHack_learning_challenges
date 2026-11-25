'''
Given the code from adriens_encryption.py we can decode such secret message
by understanding the math behind the conversions.

- The original message was treated as a byte stream
- Then the encoding function creates the variable 'plaintext'
- This variable is made up of the following:
    - Each byte (character) of the flag is converted to bits, the minimum number
    - Then each bit sequence gets truncated the first 2 characters ('0b') 
    - Finally filling up to 8 digits with 0's
    - And is joined with an empty string to make a bit stream

This bit stream is used to guide an encoding.
- For every bit in the bitstream, a randonm exponent is calculated in the range
from 1 to the prime number.
- An 'a' (an arbitrary integer) to the power of 'e' (previous exponent)
modularly divided by prime 'p', resulting in 'n'.
- If the bit is 1:
    - the ciphertext gets appended 'n'.
- If the bit is 0:
    - the ciphertext gets appended p - n.

Lastly this ciphertext is returned.

The trick here is the Legendre Symbol and the prime number.

If we take a look at the prime number,

p = 1007621497415251

it end with ...51. This means that this prime obeys the case of:

p ≡ 3 mod 4 -> p = 4k + 3

So therefore, for roughly half 'a' 's that belong to the field F_p^*, it follows that:

x^2 ≡ a mod p

x = a^( (p + 1) / 4 )

That is, 'a' is a quadratic residue.

Where (p + 1) / 4 will always be an Integer.

This means that if 'a' is a quadratic residue and p ≡ 3 mod 4, and the following:

a ≡ r^2 mod p

a^e ≡ (r^2)^e mod p ('e' is the secret random exponent used to calculate 'n')

n ≡ (r^2)^e mod p

n ≡ (r^e)^2 mod p

'n' is always a perfect square in F_p^*.

For a prime such that p ≡ 3 mod 4, it means that the Legendre Symbol from 
first element of F_p^* is +1, and element p-1 of F_p^* is -1. This is derived from
p ≡ 3 mod 4 -> p -1 ≡ -1 mod p,  This means that the last element is a
non-quadratic residue.

Demonstrating the usefulness of Legendre Symbol:

(-n / p) = (-1 / p) * (n / p) = (-1) * (+1) = -1

If Legendre Symbol is 1, it's always the first, and if it's
-1 it's p - n or -n, due to the fact previously mentioned of p ≡ 3 mod 4.  

If Legendre Symbol of the encoded bit 'm' from ciphertext is 1, it means 
that it was 'n' appended to the ciphertext. 1 encoded.
And if it was -1, it was 'p - n'. 0 encoded.

This solves the mystery for which was the encoded character. And like so, the
original flag.
'''
import ast
# standard library component to read files and treat the integer list 

a = 288260533169915
p = 1007621497415251
# arbitrary int 'a' and 'p'

with open("adriens_output.txt", "r") as f:
    ciphertext = ast.literal_eval(f.read().strip())
# now we have the ciphertext

def decoding_adriens_signs(cipher):
    '''
    We'll use mathematical properties previously described to solve this encoding.
    - Euler's test for quadratic residues.
    Input: cipher ([int])
    Output: flag (string) 
    '''

    flag = ''


    for i in range(0, len(cipher), 8):
        # jumping in ranges of 8 bits from 8 bits to decode each character

        encoded_byte = cipher[i:i+8]

        decoded_bit_stream = []
        # temporal list to store bits of each decoding of 'n'

        for n in encoded_byte:
            # here we'll make the Euler's test

            legendre_symbol = pow(n, (p-1)//2, p) 

            if legendre_symbol == 1:
                decoded_bit_stream.append(1)
            elif legendre_symbol == (p - 1):
                decoded_bit_stream.append(0)

        # now its time to cast this bit list into a bit representation
        # we'll use bitwise operations

        binary_number = 0

        for bit in decoded_bit_stream:
            binary_number = (binary_number << 1) | bit

        binary_number = bin(binary_number)
        # now that we have the binary number, we're going to cast it into an integer

        # using base-2 as second argument will cast into an integer from 0 to 255
        # due to that fact that it was a previously a binary number
        decoded_byte = int(binary_number, 2)

        # casting into character the decoded byte
        decoded_character = chr(decoded_byte)

        # appending the decoded character into the solution string
        flag += decoded_character

    print(flag)
    return flag


decoding_adriens_signs(ciphertext)
