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


print("part one :",nb)

# part two

point = 50
nb = 0

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        number = int(line[1:])
        prev = point

        point += number * (-1 if line[0] == "L" else 1)

        if point == 0:
            nb += 1
        else:
            nb += abs(point)//100
            if point < 0 and prev != 0:
                nb += 1

        point = point%100

print("part two :",nb)