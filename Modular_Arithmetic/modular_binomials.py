'''
We have to find primes 'p' and 'q', rearranging the following equations

1) N   = p * q

2) c_1 = (2*p + 3*q)^(e_1) mod N

3) c_2 = (5*p + 7*q)^(e_2) mod N

As any product k*p^(i)*q^(j) ≡ 0 mod N, where (i, j >= 1)
This simplifies the equations 2) and 3). Following:

(2*p + 3*q)^(e_1) ≡ (2*p)^(e_1) + (2*p)^(e_1 -1)*(3*q) + ... + (2*p)*(3*q)^(e_1 -1) + (3*q)^(e_1) mod N

(2*p + 3*q)^(e_1) ≡ (2*p)^(e_1) + (3*q)^(e_1) mod N

The same happens with c_2:

(5*p + 7*q)^(e_2) ≡ (5*p)^(e_2) + (7*q)^(e_2) mod N

Now we have the following:
 
 c_1 = (2*p)^(e_1) + (3*q)^(e_1) mod N

 c_2 = (5*p)^(e_2) + (7*q)^(e_2) mod N

We'll use the exponent of e_1 for c_2 and e_2 for c_1:

(c_1)^(e_2) = ((2*p)^(e_1) + (3*q)^(e_1))^(e_2) mod N

((2*p)^(e_1) + (3*q)^(e_1))^(e_2) mod N = 

(2*p)^(e_1 * e_2) + (2*p)^(e_1 * (e_2 - 1))*(3*q)^(e_1) + ... + (2*p)^(e_1)*(3*q)^(e_1 * (e_2 - 1) + (3*q)^(e_1 * e_2)

As we noted previously about any product k*p^(i)*q^(j) ≡ 0 mod N, it results as:

((2*p)^(e_1) + (3*q)^(e_1))^(e_2) mod N ≡ (2*p)^(e_1 * e_2) + (3*q)^(e_1 * e_2) mod N

Therefore:
(c_1)^(e_2) = (2*p)^(e_1 * e_2) + (3*q)^(e_1 * e_2) mod N

And like so for (c_2)^(e_1).

(c_2)^(e_1) = (5*p)^(e_2 * e_1) + (7*q)^(e_2 * e_1) mod N

Lets rewrite E = e_1 * e_2

So we have:
(c_1)^(e_2) = (2*p)^E + (3*q)^E mod N
(c_2)^(e_1) = (5*p)^E + (7*q)^E mod N

As a system of equations:
A = 2p + 3q
B = 5p + 7q

We multiply for one of the factor each to eliminate one factor

3B - 7A = (15p + 21q) - (14p + 21q) = 15p - 14p

So in the same manner, we'll multiply by 3^E and 7^E each equation to obtain 'p'and delete 'q'

3^E*(c_2)^(e_1) - 7^E*(c_1)^(e_2) = (15p)^E + (21q)^E - (14p)^E - (21q)^E

= (15^E - 14^E)*p^E mod N

let's call X = 3^E*(c_2)^(e_1) - 7^E*(c_1)^(e_2) 

So:
 X ≡ (15^E - 14^E)*p^E mod N

This congruence means:

X = (15^E - 14^E)*p^E + kN

That means that as (15^E - 14^E)*p^E contains 'p' and kN contains 'p', X is 
divisible by 'p'.

That also means that among X and N, there must be a number that divides both, 
and at the same time, is the greates among both. 

Such value is 'p'.

This results in: GCD(X, N) = p

Finally q = N // p

the flag will be: 'crypto{p,q}'
'''

N = 14905562257842714057932724129575002825405393502650869767115942606408600343380327866258982402447992564988466588305174271674657844352454543958847568190372446723549627752274442789184236490768272313187410077124234699854724907039770193680822495470532218905083459730998003622926152590597710213127952141056029516116785229504645179830037937222022291571738973603920664929150436463632305664687903244972880062028301085749434688159905768052041207513149370212313943117665914802379158613359049957688563885391972151218676545972118494969247440489763431359679770422939441710783575668679693678435669541781490217731619224470152467768073
e1 = 12886657667389660800780796462970504910193928992888518978200029826975978624718627799215564700096007849924866627154987365059524315097631111242449314835868137
e2 = 12110586673991788415780355139635579057920926864887110308343229256046868242179445444897790171351302575188607117081580121488253540215781625598048021161675697
c1 = 14010729418703228234352465883041270611113735889838753433295478495763409056136734155612156934673988344882629541204985909650433819205298939877837314145082403528055884752079219150739849992921393509593620449489882380176216648401057401569934043087087362272303101549800941212057354903559653373299153430753882035233354304783275982332995766778499425529570008008029401325668301144188970480975565215953953985078281395545902102245755862663621187438677596628109967066418993851632543137353041712721919291521767262678140115188735994447949166616101182806820741928292882642234238450207472914232596747755261325098225968268926580993051
c2 = 14386997138637978860748278986945098648507142864584111124202580365103793165811666987664851210230009375267398957979494066880296418013345006977654742303441030008490816239306394492168516278328851513359596253775965916326353050138738183351643338294802012193721879700283088378587949921991198231956871429805847767716137817313612304833733918657887480468724409753522369325138502059408241232155633806496752350562284794715321835226991147547651155287812485862794935695241612676255374480132722940682140395725089329445356434489384831036205387293760789976615210310436732813848937666608611803196199865435145094486231635966885932646519

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

    while b != 0:
        c , a = a % b , b
        if c == 0:
            return b 
        b = c

    return a

def mod_binom(N, e1, e2, c1, c2):
    '''
    Calculate the factor of X, using modular exponentiation and then the greates
    common divisor, using Euclids algorithm
    input: N (int), e1 (int), e2 (int), c1 (int), c2 (int)
    output: p, q ((int))
    '''

    # calculating the product of exponents
    E = e1 * e2

    # this is the factor where: X = (15^E - 14^E)*p^E + kN
    X = (pow(3,E,N) * pow(c2,e1,N) - pow(7, E, N) * pow(c1, e2,N)) % N 

    # applying GCD to find 'p'
    # as X already has mod N, is not needed to call inside the gcd function
    p = gcd(X, N)

    q = N // p

    return p, q

p, q = mod_binom(N, e1, e2, c1, c2) 

print("crypto{"f"{p},"f"{q}""}")