''' Program to append some text '''
import sys

# Get text from command line argument
fileStr = sys.argv[1]

# Open file in append mode
f = open("file.txt", "a")

# Write to file
f.write(fileStr + "\n")

# Close the file
f.close()
