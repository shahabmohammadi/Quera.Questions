target = int(input())
for i in range(1, (target + 1)):
    for ii in range(1, target + 1):
        print(i * ii, end=" ")
    print()
