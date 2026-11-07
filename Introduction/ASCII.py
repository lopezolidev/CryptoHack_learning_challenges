'''
Given a list of numbers, finding the character values of each will in return
output the flag I need
- ord() function turns the character symbol into its ASCII value
- chr() function does the opposite
'''

codes = [
    99, 114, 121, 112, 116, 
    111, 123, 65, 83, 67, 
    73, 73, 95, 112, 114, 
    49, 110, 116, 52, 98, 
    108, 51, 125]

result = ''

for number in codes:
    character = chr(number)
    # obtaining the character encoded by each number

    result += character
    # appending the character to the result string

print(f"The encoded string is: {result}")
