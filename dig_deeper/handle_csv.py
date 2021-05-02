import matplotlib.pyplot as plt

xs = []
ys = []

name = "Max"
gender = "M"
state = "CA"

with open('../data/names.csv', 'r') as file:
    counter = 0

    for line in file:
        counter = counter + 1

        line_splitted = line.strip().split(',')
        if line_splitted[1] == name and line_splitted[3] == gender and line_splitted[4] == state and int(line_splitted[2]) < 1940:
            xs.append(line_splitted[2])
            ys.append(line_splitted[5])

plt.plot(xs, ys)
plt.show()
