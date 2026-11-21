'''
Tonelli-Shanks is a solution to finding the square root modulo p in a general
case when p ≡ 1 (mod 4), where simple modular exponentiation fails.

Why simple quadratic manipulations fail when p ≡ 1 (mod 4):
-----------------------------------------------------------
When p ≡ 3 (mod 4), we have p = 4k + 3, so (p + 1) / 4 is an integer.
For any quadratic residue 'a', Euler's criterion gives:

    a^((p - 1) / 2) ≡ 1 (mod p)

Multiplying both sides by 'a' yields:

    a^((p + 1) / 2) ≡ a (mod p)  =>  (a^((p + 1) / 4))^2 ≡ a (mod p)

However, when p ≡ 1 (mod 4), we have p = 4k + 1, so (p + 1) / 4 is not an
integer. To force an exponent divisible by 4, we must use (p + 3) / 4
(since p + 3 = 4k + 4), which requires multiplying both sides by a^2:

    a^((p - 1) / 2) * a^2 ≡ 1 * a^2 (mod p)
    a^((p + 3) / 2)       ≡ a^2     (mod p)
    (a^((p + 3) / 4))^2   ≡ a^2     (mod p)

This reduces to x^2 ≡ a^2 (mod p), giving only the trivial solutions
x ≡ ±a (mod p) rather than √a. Because p - 1 is divisible by higher powers
of 2, a single exponentiation cannot isolate √a—requiring Tonelli-Shanks.

Algorithm Design & Step-by-Step Rationale:
------------------------------------------
1. Isolate the odd part from the 2-adic part of the group order:
   Factor p - 1 = Q * 2^S with Q odd and S >= 2.
   - Design decision: In the multiplicative group F_p^*, squaring is
     invertible on elements of odd order because gcd(2, Q) = 1. Separating Q
     lets us resolve the odd component in one exponentiation and reduce the
     problem strictly to the 2-Sylow subgroup (of order 2^S).

2. Construct an initial root candidate R and an error factor t:
   Set R ≡ a^((Q + 1) / 2) (mod p) and t ≡ a^Q (mod p).
   - Design decision: Because Q is odd, (Q + 1) / 2 is guaranteed to be an
     integer. This establishes the core loop invariant:
         R^2 ≡ a^(Q + 1) ≡ a * a^Q ≡ a * t (mod p)
   - If t ≡ 1 (mod p), the error factor vanishes and R is already √a.
   - Otherwise, since 'a' is a quadratic residue (a^((p - 1) / 2) ≡ 1):
         t^(2^(S - 1)) ≡ a^(Q * 2^(S - 1)) ≡ a^((p - 1) / 2) ≡ 1 (mod p)
     Thus, the multiplicative order of t is strictly a power of 2:
     ord(t) = 2^i for some 1 <= i <= S - 1.

3. Find a generator 'c' for the 2-Sylow subgroup:
   Search for any quadratic non-residue z (where z^((p - 1) / 2) ≡ -1 mod p)
   and set c ≡ z^Q (mod p).
   - Design decision: Because z is a non-residue, c^(2^(S - 1)) ≡ -1 (mod p),
     giving c an exact order of 2^S. Repeatedly squaring c produces elements
     of every exact order 2^k (1 <= k <= S), acting as a reference "ruler"
     to cancel out the 2-power order of t.

4. Iteratively reduce the order of t while preserving R^2 ≡ a * t:
   Initialize M = S (tracking ord(c) = 2^M) and loop while t != 1 (mod p):
   a) Find the smallest i (1 <= i < M) such that t^(2^i) ≡ 1 (mod p).
      This determines the exact order of t: ord(t) = 2^i.
   b) Compute b ≡ c^(2^(M - i - 1)) (mod p).
      - Design decision: Since ord(c) = 2^M, b has exact order 2^(i + 1),
        so b^2 has exact order 2^i—matching ord(t). In a cyclic 2-group, -1
        is the unique element of order 2, so multiplying two elements of
        exact order 2^i cancels their highest-order bit and strictly lowers
        the resulting order below 2^i.
   c) Update the state:
      R ← (R * b)   mod p
      t ← (t * b^2) mod p   # Preserves R^2 ≡ a * t and lowers ord(t) < 2^i
      c ← b^2       mod p   # Updates generator so ord(c) = 2^i
      M ← i                 # Tightens the order bound for the next iteration

5. Termination & Complexity:
   Since 1 <= i < M on each pass, M strictly decreases, guaranteeing
   convergence to t ≡ 1 (mod p) in at most S - 1 iterations (O(S^2) modular
   multiplications, or O(log^2 p) in the worst case), leaving R^2 ≡ a (mod p).
'''

a = 8479994658316772151941616510097127087554541274812435112009425778595495359700244470400642403747058566807127814165396640215844192327900454116257979487432016769329970767046735091249898678088061634796559556704959846424131820416048436501387617211770124292793308079214153179977624440438616958575058361193975686620046439877308339989295604537867493683872778843921771307305602776398786978353866231661453376056771972069776398999013769588936194859344941268223184197231368887060609212875507518936172060702209557124430477137421847130682601666968691651447236917018634902407704797328509461854842432015009878011354022108661461024768

p = 30531851861994333252675935111487950694414332763909083514133769861350960895076504687261369815735742549428789138300843082086550059082835141454526618160634109969195486322015775943030060449557090064811940139431735209185996454739163555910726493597222646855506445602953689527405362207926990442391705014604777038685880527537489845359101552442292804398472642356609304810680731556542002301547846635101455995732584071355903010856718680732337369128498655255277003643669031694516851390505923416710601212618443109844041514942401969629158975457079026906304328749039997262960301209158175920051890620947063936347307238412281568760161

def find_sylow(prime):
    '''
    This function serves the purpose to modularly isolate the odd part 
    from the 2-adic part of the group order: 
    Factor p - 1 = Q * 2^S with Q odd and S >= 2.
    '''
    order = prime - 1
    # substracting 1 from prime to obtain the order

    s = 0
    # S exponent

    while (order & 1) == 0:
        ''' 
        all even numbers binary representation has 0 at the end.
        Masking it with 1 at the end should return 0 and keep in the loop.
        If that masking results in 1, it'll return 1 and won't = 0, breaking
        '''
        order >>= 1
        # shifting by 1 = dividing by 2
        s += 1
        # adding 1 to S exponent

    return (order, s)
    # returning the odd part of the order of the field F_p^*
    # and returning the S exponent
    

def min(a, b):
    '''
    A function that returns the minimum from two values
    '''
    
    if a < b:
        return a
    return b


def mod_square_root(a, prime):
    '''
    calculates modular square root from an integer, first discovering if its
    actually a quadratic residue and then applying tonelli shanks. 
    It returns the lowest root.
    input: a (int), prime (int)
    output: root (int)
    '''

    # is 'a' a quadratic residue?
    legendre = pow(a,(prime - 1)//2, prime)
    # calculating legendre symbol for 'a' and prime given

    if legendre != 1:
        print(f"{a} is not a quadratic residue modulo {prime}")
        return
    # condition to exit if 'a' is not a quadratic residue

    # now let's find 'q' and 's'
    q, s = find_sylow(prime)

    for z in range(2, prime):
        z_legendre = pow(z, (prime - 1)//2, prime)
        if z_legendre == (prime -1) :
            break
        # finding the lowest z in the field that satisfies: (z / p) ≡ -1

    c = pow(z, q, prime)
    # c ≡ z^q mod p

    r = pow(a, (q + 1)//2, prime)
    # r ≡ a^((q + 1)/2)

    m = s % prime
    # m ≡ s 

    t = pow(a, q, prime)
    # t ≡ a^q mod p


    while t != 1:

        for i in range(1, m):
            if pow(t, pow(2, i), prime) == 1:
                break
        # finding the lowest i such that: t ^ (2 ^ i) ≡ 1

        exponent_of_c = pow(2, m - i - 1)

        b = pow(c, exponent_of_c, prime)
        # c ≡ c ^ (2 ^ (m - i - 1))

        r = (r * b) % prime
        # r ≡ r * b

        t = (t * pow(b, 2, prime)) % prime
        # t ≡ t * b^2

        c = pow(b, 2, prime)
        # c ≡ b^2

        m = i
        # m ≡ i
    
    return min(r, prime - r)
    # returning the minimum root among r and p-r 

min_root = mod_square_root(a, p)

print(f"The square root of {a} is: {min_root}")





        
