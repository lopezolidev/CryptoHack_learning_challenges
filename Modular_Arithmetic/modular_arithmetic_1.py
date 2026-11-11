'''
Learning about modular arithmetic is a fundamental knowledge in cryptography

We say that two integers are congruent modulo m if a ≡ b mod m.
Another way of saying this, is that when we divide the integer a by m the remainder is b.
This tells you that if m divides a (this can be written as m∣a) then a ≡ 0 mod m.

Considering the following:
11 ≡ x mod 6
8146798528947 ≡ y mod 17

The solution is the smaller of the two integers,
(x,y), we obtained after reducing by the modulus.
'''

def modulus(a, mod_n):
    '''
    The goal of this function is to show which of both integers is the lowest mod n
    '''

    z = a % mod_n
    # this is a native operation in Python

    return z

a = 11
mod_n = 6

b = 8146798528947
mod_m = 17

short_number = modulus(a, mod_n)
long_number = modulus(b, mod_m)

print(f"Short number ({a}) mod {mod_n} is: {short_number}")
print(f"Long number ({b}) mod {mod_m} is: {long_number}")
