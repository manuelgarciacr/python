# numbers: list[int] = [6, 19, 3]
numbers: list[int] = []

print(max(numbers, default=None))
print(min(numbers, default=None), "\n")

max: int = None
min: int = None

for num in numbers:
    if max == None or num > max: max = num
    if min == None or num < min: min = num

print(f"The maximum is {max} and the minimum is {min}")