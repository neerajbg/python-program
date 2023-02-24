# Program to generate fibonacci numbers

# Initialize first and second number
firstNumber, secondNumber = 0, 1

# User input for number of terms.
howManyTerm = input("Please provide the term for fibonacci sequence ... ")

# Validate for the positive integer value
while not howManyTerm.isdigit():
    howManyTerm = input("Please provide a valid numeric value ... ")


# Loop upto howManyTerm
i = 0

print("Fibonacci sequence of \"" + howManyTerm + "\" term")
while i < int(howManyTerm):
    i = i+1

    print(firstNumber)
    result = firstNumber + secondNumber

    firstNumber = secondNumber
    secondNumber = result
