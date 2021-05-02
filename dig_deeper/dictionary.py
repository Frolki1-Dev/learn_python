dictionary = {}

with open('../data/names.csv', 'r') as file:
    title = 0
    for line in file:
        if title == 0:
            title = 1
            continue

        identifier, name, year, gender, state, total = line.strip().split(',')
        # Check if the name is in the dictionary
        if name in dictionary:
            # Add one to the value
            dictionary[name] = int(dictionary[name]) + int(total)
        else:
            dictionary[name] = int(total)

max_occurrences = 0
dic_key = ''

# Find out which name is most given
for key, value in dictionary.items():
    if max_occurrences < value:
        max_occurrences = int(value)
        dic_key = key

print(str(dic_key) + " with " + str(max_occurrences))
