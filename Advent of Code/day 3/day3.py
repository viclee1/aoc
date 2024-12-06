import re
with open("C:/Users/vlee8/Documents/Advent of Code/day 3/input.txt") as file:
    lines = file.read()

mul_arr = re.findall("mul\([0-9]+,[0-9]+\)", lines)
mult = []
for x in mul_arr :
    numbers = list(map(int, re.findall(r'\d+', x)))
    mult.append(numbers[0] * numbers[1])
print(sum(mult))
enabled = True
total = 0
for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", lines):
    if do or dont :
        enabled = bool(do)
    else :
        x = int(a) * int(b)
        total += x*enabled
print(total)
