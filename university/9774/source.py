target = str(input())
for i in target:
    print(i + ": ", end="")
    for ii in range(int(i)):
        print(int(i), end="")
    print()