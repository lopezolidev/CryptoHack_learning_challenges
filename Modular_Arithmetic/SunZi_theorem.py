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

def extended_gcd(a, b):
    '''
    Using extended Euclids algorithm, we will find the (x,y) coefficients that
    accompany 'a' and 'b' in the Bézout's identity:
    
    ax + by = d
    '''
    a_copy = a
    b_copy = b

    if a < b:
        t = a
        a = b
        b = t
        # swapping values


    # initial state
    x_a , y_a = (1 , 0)
    a = x_a * a + y_a * b

    x_b , y_b = (0 , 1)
    b = x_b * a + y_b * b
    # Dividend (a) and divisor (b) are a linear combination of both of them

    while b != 0:
        q = a // b
        # quotient

        r = a - q * b
        # residue calculation

        x_r = x_a - q * x_b
        # calculating coefficients of 'a' component

        y_r = y_a - q * y_b
        # calculating coefficients of 'b' component

        if r == 0:
            if a_copy < b_copy:
                return (b, y_b, x_b)
            return (b, x_b, y_b)            
        # 'b' became 'a' (dividend), which in this point is the GCD
        # x_b is the x's component of 'a', the current coefficient when that happened
        # y_b is the y's component of 'b', the current coefficient when that happened
            
        a = b
        b = r
        # updating divisor and dividend

        x_a = x_b
        x_b = x_r
        # updating x component for 'a' and 'b'

        y_a = y_b
        y_b = y_r
        # updating y component for 'a' and 'b'

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
        
        '''
Using extended GCD, we can formulate the missing factor to find y_i in O(logn). 
This is because we can rewrite the problem like so:

N_i * y_i ≡ 1 mod n_i
N_i * y_i + n_i * k_i = 1 (as the reduction N_i and n_i are coprime always)

As n_i*k_i is divisible by n_i, n_i*k_i = 0, therefore:

N_i * y_i = 1
leaving only the first coefficient as the one that matters in the operation and 
the one we're looking for
        '''
        _, u, _ = extended_gcd(reduction, modulus)    
        # as Euclids may return this value negative
        u %= modulus

        # making the product of a_i * N_i * y_i
        x += (remainder * factor * u)
        
       

    x %= N
    # applying last modulo operation to find x

    return x

x = sunzi_theorem(set_of_congruences)

print(x)

    



        
        
    
