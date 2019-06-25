target = list(input())
total = 0
while not len(target) == 1:
    for i in target:
        total += int(i)
    target = list(str(total))
    total = 0
print("".join(target))
