'''
Reverse a string provided by user
'''

# Take user input
userInput = input("Please enter string to reverse\n")

''' Reverse String using For Loop '''

# Initialize the reversed string
revStr = ""

print("Reverse String using For Loop\n")
for i in userInput:
    revStr = i + revStr

print("Original String was ", userInput)
print("Reversed String is - ", revStr)

'''  WHILE LOOP '''

print("\nReverse string using While Loop\n")

revStr = ""
length = len(userInput)

while length > 0:
    length = length - 1
    revStr = revStr + userInput[length]

print("Original String was ", userInput)
print("Reversed String is - ", revStr)
