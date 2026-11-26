
for i in range(10): print(i) # from 0 to 9
print()
for i in range(1,10): print(i) # from 1 to 9
print()
for i in range(1,10,2): print(i) # from 1 to 10 step 2
print()
for i in [4, 1, 8, 4, 9, 3]: print(i)
print()
for i in  [4, 1, 8, 4, 9, 3][3:5]: print(i)

text = "abracadabra"
for char in text: print(char)
print(text[::-1]) # arbadacarba
print(text[::2]) # arcdba
for char in reversed(text): print(char, end="")
print()
for i in range(len(text), 0, -1): print(text[i-1], end="")
output: str = ""
for i in range(len(text), 0, -1): output+=text[i-1]
print(f"\n",output, sep="")
print("END")