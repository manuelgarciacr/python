name: str = "Manuel"
age: int = 57

# Remark

print("Hi classroom, my name is " + name + " and I'm " + str(age) + " years old.")
print(f"Hi classroom, my name is {name}" + f" and I'm {age + 1} years old.")
print("Hi classroom, my name is ", name)

"""
$ py exercici01.py
Hi classroom, my name is Manuel and I'm 57 years old.
Hi classroom, my name is Manuel and I'm 58 years old.
Hi classroom, my name is  Manuel
"""
