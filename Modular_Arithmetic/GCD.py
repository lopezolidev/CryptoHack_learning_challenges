'''
- In this exercise, we must develop the solution of GCD(a,b), being 'a' and 'b'
integers.
- We'll achieve this making use of Euclid's algorithm, that is by succesive divisions
'''

def gcd(a, b):
    '''
    GCD function using Euclids algorithm between 2 numbers
    - a : integer
    - b : integer
    '''
    if a < b:
        t = a
        a = b
        b = t
        # swapping values

    c = a - b
    # in case that are equal, any of them
    while b != 0:
        c , a = a % b , b
        if c == 0:
            return b 
        b = c

    return b

gcd_res = gcd(66528, 52920)

print(gcd_res)