age:int = 0

print("How old are you?")
age = int(input())
print(f"You are {age + 1} years old")

print("How old are you?")
age = input()
print(f"You are {age + 1} years old")

"""
How old are you?
22
Traceback (most recent call last):
  File "C:\\Users\\formacio\\Documents\\Manuel\\python\\exercise05.py", line 5, in <module>
    print(f"You are {age + 1} years old")
                     ~~~~^~~
TypeError: can only concatenate str (not "int") to str
"""

