import random

numPc: int = 0
numUser: int = 0
count: int = 3
diff = 11

# while numPc != numUser and (count := count - 1) >= 0:
while diff > 10 and count > 0:
    count -= 1
    numPc = random.randint(1, 500)
    numUser = int(input("Integer between 1 and 500: "))
    diff = abs(numUser - numPc)

    if diff > 10: print(f"❌ Answer {numUser}: further from {numPc}")

print()
print("❌ No more intents" if diff > 10 else f"✅ Answer {numUser}: exact response" if numUser == numPc else f"✅ Answer {numUser}: close to {numPc}")
