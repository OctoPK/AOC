# part one

total = 0

def is_invalid_id_part_one(n):
    s = str(n)
    if len(s)%2 != 0:
        return False
    mid = len(s)//2
    return s[:mid] == s[mid:]

with open("input.txt") as f:
    ranges = f.readline().strip().split(",")
    for r in ranges:
        start, end = map(int, r.split("-"))
        for i in range(start, end+1):
            if is_invalid_id_part_one(i):
                total += i

print("part one :",total)