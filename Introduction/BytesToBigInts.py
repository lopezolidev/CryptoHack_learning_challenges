'''
- Given a long integer, that number must be converted back into a message
- bytes_to_long() and long_to_bytes() function will help us to achieve this task
- To use this functions we'll have to import the PyCryptodome library
'''

from Cryptodome.Util.number import *

very_long_number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# first we need to convert this long number into bytes

bytes_long_number = long_to_bytes(very_long_number)
# now we only need to encode it in utf-8

decoded = bytes_long_number.decode("utf-8")
# applying the decode function to convert it into utf-8 format

print(decoded)
# crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}