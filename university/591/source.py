target = int(input())
for y in range(target):
    if y == 0 or y == (target - 1):
        print("*" * target)
    else:
        print("*" + " " * (target - 2) + "*")
