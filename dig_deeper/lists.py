# How to work with lists
# First init a list of students
students = ["Max", "Robert", "Anika", "Tanja"]

# Make a copy of the list but start from index 1 to 3
students_copy = students[1:3]

# Add something to the list
students = students + ["Oliver"]

print(students)

# Get the last item and remove it
last_student = students.pop()
print(last_student)
print(students)

# Remove an item from the list (by key)
del students[2]

# Anika is no more here
print(students)

# Remove by value
students.remove("Robert")

# And now Robert is no more in the list
print(students)

# Get the last index
print(students[-1])