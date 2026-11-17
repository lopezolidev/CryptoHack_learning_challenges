'''
Let's work with modulo p = 29
We can take the integer a = 11 and calculate a^(2) = 5 mod 29.
As a = 11, a^(2) = 5, we say the square root of 5 is 11.

If we try to find the square root of 18, we need to find some integer a such 
that a^(2) = 18.

Our first idea might be to start with a = 1 and loop to a = p − 1. 

As 'p' in this case isn't too large and we can quickly check all options.

We have found that for all a ∈ F, we'll never find an a such that a^2 = 18.

What we are seeing, is that for the elements of F, not every element has a square root. In fact, what we find is that for roughly one half of the elements of F, there is no square root.

We say that an integer x is a Quadratic Residue if there exists an 'a' such that 
a^(2) ≡ x mod. 

If there is no such solution, then the integer is a Quadratic Non-Residue.

In other words, x is a quadratic residue when it is possible to take the square root of x
modulo an integer p.

If a^(2) = x then (−a)^(2) = x. So if x is a quadratic residue in some finite field, 
then there are always two solutions for a.
'''

def quad_calc(p, list_of_quads):
    '''
    Function that iterates over the elements of F_p until it finds all quadratic
    residues
    '''
    quad_res = []
    # list to store quadratic residues

    for i in range(1, p):
        # iterate over all the elements of the field P
        i_sqr_mod = pow(i, 2, p)
        # elevating the base (each value of the field) to the power of 2
        # and then dividing modulo p

        print(f"this is a residue: {i_sqr_mod}")

        if i_sqr_mod in list_of_quads:
            quad_res.append(i)
            # appending the solution to list of quadratic residues

    return quad_res

p = 29
list_of_quad_and_non_quads = [14, 6, 11]
# for this given list, we have to find the square root (if there is) in the field
# and return the smallest

result = quad_calc(p, list_of_quad_and_non_quads)

print(result)

