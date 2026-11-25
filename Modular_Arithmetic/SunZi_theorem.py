'''
Given an arbitrary integer set a^i, and a set of pairwise coprime integers n^i
( {n^1, n^2, ..., n^i}: gcd(n^i, n^j) = 1), the following set of linear 
congruences hold:
x ≡ a^1 mod n^1
x ≡ a^2 mod n^2
...
x ≡ a^n mod n^n

Exists an unique solution x ≡ a mod N, where N = n^1 * n^2 * ... * n^n

Therefore, given x ≡ a^i mod n^i for a certain congruence, 
N^j * y^j ≡ 1 mod n^j, where N^j = N / n^j

Finally, this solution is:
x ≡ (Sum, from i = 1, of: a^i * N^i * y^i) mod N
'''

set_of_congruences = [(2, 5),(3, 11),(5, 17)]
# each congruence of the form:
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17

def sunzi_theorem(congruences):
    '''
    Process each congruence to obtain N, y^i and finally integer x that satisfies
    all the congruences
    input: list of tuples [(int, int)]
    output: integer
    '''

    N = 1
    # element to multiply each modulus to obtain N
    
    for pair in congruences:
        _, modulus = pair
        N *= modulus
    # iterate over each congruence to obtain modulus

    x = 0
    # value for making last multiplication and iteration
    
    for pair in congruences:
        remainder, modulus = pair
        factor = N // modulus
        # now we have N^i = N / n^i

        reduction = factor % modulus
        # N^i mod n^i

        for i in range(1, modulus):
            full_product = (reduction * i) % modulus
    
            if full_product == 1:
                break
        # finding modular inverse of N^i
        # N^i * y^i ≡ 1 mod n^i

        x += (remainder * factor * i)
        # making the product of a^i * N^i * y^i
       

    x %= N
    # applying last modulo operation to find x

    return x

x = sunzi_theorem(set_of_congruences)

print(x)

    



        
        
    
