# part one

point = 50
nb = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        number = int(line[1:])
        if line[0] == "R":
            point = (point+number)%100
        else:
            point = (point-number)%100
        if point == 0:
            nb += 1


print("\n",nb)

# my result : 1084

