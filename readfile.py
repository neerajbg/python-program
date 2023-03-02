''' Program to read the file content '''

# Open file in read mode
f = open("file.txt", "r")

# Iterate through file object
for line in f:
    print(line)

f.close()
