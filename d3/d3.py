# part one

total = 0

with open("input.txt") as f:
    for line in f:
        digits = [int(c) for c in line if c.isdigit()]

        best = 0
        for i in range(len(digits) - 1):
            for j in range(i + 1, len(digits)):
                value = 10 * digits[i] + digits[j]
                if value > best:
                    best = value
        total += best

print("part one :",total)

# part two

def best_n_digits(digits, n):
    drop = len(digits) - n
    stack = []

    for d in digits:
        while drop > 0 and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)
    return stack[:n]

total = 0

with open("input.txt") as f:
    for line in f:
        digits = [int(c) for c in line if c.isdigit()]
        best = best_n_digits(digits, 12)

        value = 0
        for d in best:
            value = 10 * value + d

        total += value

print("part two :",total)
