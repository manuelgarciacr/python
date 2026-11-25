invoicing: list[int] = [23491, 53921, 108372, 43593, 31634, 43291, 56218, 45829, 66324, 21356, 39736, 74321]
total = 0

for n in invoicing: total += n
    
print(total)
print(sum(invoicing))
print("Average:", sum(invoicing)/invoicing.__len__())
print("Average:", round(sum(invoicing) / len(invoicing), 2))
print("Average:", round(sum(invoicing) / len(invoicing)))

firstQuarter: list[int] = invoicing[0:3]

print("First quarter average:", round(sum(firstQuarter) / len(firstQuarter)))
