age = int(input("How old are you? "))
dow = input("What day is it? ")

if (age >= 18) | (dow == "thursday") & (age >= 16):
      print("You can pass")
elif age == 0  :
        print("Invalid age")
else:
  print("You can't pass")
  print("Sorry")
print("Next command")

'''
if (age >= 18) or (dow == "thursday") and (age >= 16):
it's the same as:
if (age >= 18) | (dow == "thursday") & (age >= 16):
'''
