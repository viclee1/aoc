
left, right = [], []
with open("C:/Users/vlee8/Documents/Advent of Code/day 1/input.txt") as file:
    for line in file:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))
print(sum(abs(l - r) for l, r in zip(sorted(left), sorted(right))))
print(sum(l * right.count(l) for l in left))