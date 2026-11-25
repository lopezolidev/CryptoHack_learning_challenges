'''
Given an arbitrary integer set a_i, and a set of pairwise coprime integers n_i
( {n_1, n_2, ..., n_i}: gcd(n_i, n_j) = 1), the following set of linear 
congruences hold:
x ≡ a_1 mod n_1
x ≡ a_2 mod n_2
...
x ≡ a_n mod n_n

Exists an unique solution x ≡ a mod N, where N = n_1 * n_2 * ... * n_n

Therefore, given x ≡ a_i mod n_i for a certain congruence, 
N_j * y_j ≡ 1 mod n_j, where N_j = N / n_j

Finally, this solution is:
x ≡ (Sum, from i = 1, of: a_i * N_i * y_i) mod N
'''

# each congruence of the form:
# x ≡ 2 mod 5
# x ≡ 3 mod 11
# x ≡ 5 mod 17
set_of_congruences = [(2, 5),(3, 11),(5, 17)]


def sunzi_theorem(congruences):
    '''
    Process each congruence to obtain N, y_i and finally integer x that satisfies
    all the congruences
    input: list of tuples [(int, int)]
    output: integer
    '''
    # element to multiply each modulus to obtain N
    N = 1
    
    # iterate over each congruence to obtain modulus
    for pair in congruences:
        _, modulus = pair
        N *= modulus
    
    # value for making last multiplication and iteration    
    x = 0
    
    
    for pair in congruences:
        # now we have N_i = N / n_i
        remainder, modulus = pair
        factor = N // modulus
        
        # N_i mod n_i
        reduction = factor % modulus
        
        # this line has to change in order for scalability
        for i in range(1, modulus):
        # finding modular inverse of N_i
        # N_i * y_i ≡ 1 mod n_i
            full_product = (reduction * i) % modulus
    
            if full_product == 1:
                break


        # making the product of a_i * N_i * y_i
        x += (remainder * factor * i)
        
       

    x %= N
    # applying last modulo operation to find x

    return x

x = sunzi_theorem(set_of_congruences)

print(x)

    



        
        
    
