from re import I


N = int(input("Enter N"))   # Question no :- 4
i = 1
while i<=2*N:
    if i % 2 != 0:
        print(i,end = " ")
    i += 1
print()
print()