target = int(input())
my_list = []
for i in range(1, target):
    if target % i == 0:
        my_list.append(i)
if sum(my_list) == target:
    print("YES")
else:
    print("NO")
