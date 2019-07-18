len_targets = int(input())
targets = []
for i in range(len_targets):
    target = input().split(" ")
    target = [int(target[0]), int(target[1])]
    if not (target[0] - 2) == target[1] and not target[0] == target[1]:
        targets.append([-1, "False"])
    else:
        if target[0] == target[1]:
            targets.append([target[0], "list_one"])
        else:
            targets.append([target[0], "list_two"])

len_targets = list(targets)
len_targets.sort()
len_targets = len_targets[-1][0]

list_1 = [0, 1]
list_2 = [2]

for i in range(len_targets):
    if list_1[-1] % 2 == 0:
        list_1.append(list_1[-1] + 1)
    else:
        list_1.append(list_1[-1] + 3)
    if list_2[-1] % 2 == 0:
        list_2.append(list_2[-1] + 1)
    else:
        list_2.append(list_2[-1] + 3)
for target in targets:
    if target[0] == -1:
        print(-1)
    else:
        if target[1] == "list_one":
            print(list_1[target[0]])
        else:
            print(list_2[target[0] - 2])
