# How to open a file an read the file out
file_read = open('../data/text_file_handler.txt', 'r')

# Now loop through the file
for line in file_read:
    print(line.strip())

# Close the file otherwise the file is blocked
file_read.close()

# Now write content in a file
file_write = open('../data/write_file_handler.txt', 'w')

# w | Create the file if not exists and delete the content of the file
# x | Create the file and if the file exists it will return an error
# a | Append the content and if the file not exists it will create the file

file_write.write('Lorem ipsum dolor sit amet')

# Close file
file_write.close()

# If now an error occurs in between from open and close it will not close the file automatically
# But for this we can use with
with open('../data/write_file_handler.txt', 'r') as file:
    for l in file:
        print(l.strip())

# Now the file will close automatically and exists only in the with scope
