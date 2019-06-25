target = int(input())
for i in range(target):
    if target < pow(2, i):
        print(pow(2, i))
        break
