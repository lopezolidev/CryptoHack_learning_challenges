'''
Given the Bézout's identity:

 ax + by = d

Where a, b, d, x, y are integers, and this identity displays the property where
two integers from which a gcd is obtained ( gcd(a,b) ), the gcd is a result of 
a linear combination of 'a' and 'b'.

This is an extension of Euclids algorithm. Where the coeficients of 'a' and 'b'
are tracked on every step of the residue calculation.

These coeficients will change during the algorithm until the residue holds the 
coeficients for 'a' and 'b'

Initial state: 
a = x_a * a + y_a * b -> x_a = 1, y_a = 0 -> (1, 0)
b = x_b * a + y_b * b -> x_b = 0, y_b = 1 -> (0, 1)

r = a - q*b -> 

where: 
r (x_r, y_r) = (x_a * a + y_a * b) - q (x_b * a + y_b * b)

Reorganizing:
r (x_r, y_r) = a (x_a - q*x_b) + b (y_a - q*y_b)

x_r = x_a - q*x_b
y_r = y_a - q*y_b

That is
x_(k+1) = x_(k-1) - q * x_k 
or
x_new = x_old - q * x_current

When the residue is == 0, that divisor's coefficient is the actual gcd, that means
we have to return the coefficients x_current and y_current, which in turn will be:

a*x_current + b*y_current = gcd(a,b)
'''

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

a = 26513
b = 32321

gcd, x, y = extended_gcd(a, b)

print(f"The GCD of {a} and {b}, is: {gcd}, in Bezouts identity \n {a} * {x} + {b} * {y} = {a * x + b * y}")
print(f"That is: \nx = {x}\n y = {y}")