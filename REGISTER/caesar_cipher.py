'''
- We need to find the deciphered text from the ciphered text. Its ciphered using
  Caesar's cipher. 
- OBJECTIVE: We need a string composed of 4 clear english words.
- We don't know the k-shift.
- There're 26 letters in the alphabet.
- k = {1, 2, ..., 25} (a shift of 26 results in the same letter).
- when performing a shift > 26, modulo 26 is applied and we're left with the 
  above set.
- As the text is of length 26, a brute force approach will be enough.
'''
ciphered_phrase = "HMSPLCW DJCC BSRAF TCPQGML"


for key in range (1, 26):
    result = ''
    # for every k-shift we start with an empty array

    for symbol in ciphered_phrase:
        # we'll apply the deciphering for each letter

        if symbol == ' ':
            result += symbol
            continue
            # in case of empty space, we ignore it

        number = ord(symbol)
        # all the letters are uppercase, we'll deal with the numbers 65-90 (A-Z)

        number = number - ord('A')
        # normalizing the character to 0 - 25

        shifted_value = (number + key) % 26 
        # here we apply the shift
        # and modulo 26 when the number cannot be represented in the alphabet

        y = shifted_value + ord('A')
        # denormalizing -> going back to the original set of uppercase letters

        y = chr(y)
        # turning the ASCII code to a character

        result = result + y
        # appending the deciphered character to the result array

    print(f"For k = {key}, deciphered is: {result}")
    # displaying every single deciphered text 

# we're looking for a phrase composed of 4 clear english words
# For k = 2, deciphered is:  JOURNEY FLEE DUTCH VERSION


    