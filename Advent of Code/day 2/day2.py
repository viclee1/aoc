with open("C:/Users/vlee8/Documents/Advent of Code/day 2/input.txt") as file:
    lines = file.readlines()
arrays = [list(map(int, line.split())) for line in lines]

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

safe_count = sum([is_safe(row) for row in arrays])
print(safe_count)

safe_count = sum([any([is_safe(row[:i] + row[i + 1:]) for i in range(len(row))]) for row in arrays])
print(safe_count)