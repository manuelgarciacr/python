num1 = 2
num2 = 3
total = 0

IVA = 21
pvp = 100
total = pvp * IVA / 100
num1 = num1 + 2
num1 += 2

print(total)
print(10 / 2)
print(f"the total is {total + pvp}")
"""
Precedence:
1	**
2	+x, -x, ~x
3	*, /, //, %, @
4	+, -
5	<<, >>
6	&
7	^
8	|
9	==, !=, <, >, <=, >=, is, in
10	not
11	and
12	or
13	:= (walrus)
"""
