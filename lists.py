cities: list[str] = ["aaa", "ggg", "bbb"]
print(cities[0], cities[2])
cities.append("tttt")
cities.pop() # removes and return last
cities[2] = "qqq"
print(cities)
cities.insert(1, 3)
print(cities)
cities.remove(3) # remove by value
print(cities)
cities.pop(1) # removes by possition
print(cities)
print(cities.index("qqq"))
print(cities.__len__())
