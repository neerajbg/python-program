''' program to write string to file '''
fileName = "file.txt"

# Open file in write mode
f = open(fileName, "w")

# Write some text
f.write("Some text here.\n")

# Close the file
f.close()
