target = input()
target = target.split(" ")
target = [int(i) for i in target]
sum = 0
for i in target:
    sum += i
if sum == 180 and not target[2] == 0 and not target[1] == 0 and not target[0] == 0:
    print("Yes")
else:
    print("No")
