from itertools import permutations
n=(input("enter the number"))
p=permutations(n)
for i in list(p):
    print(i)
