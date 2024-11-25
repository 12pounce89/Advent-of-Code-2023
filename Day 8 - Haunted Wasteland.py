# Part 1

steps = 0
current = "AAA"
order = ""
nodes = dict()

with open('data/day8.txt') as file:
    count = 0
    for line in file:
        count += 1
        if count == 1:
            order = line
        elif count >= 3:
            broken_line = line.split("=")
            nodes[broken_line[0].strip()] = [broken_line[1][2] + broken_line[1][3] + broken_line[1][4], broken_line[1][7] + broken_line[1][8] + broken_line[1][9]]

while True:
    if (current == "ZZZ"):
        break
    steps += 1
    if (order[steps % len(order)] == "L"):
        current = nodes[current][0]
    else:
        current = nodes[current][1]

print(steps)


# Part 2