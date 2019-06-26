target = int(input())
name_list = []
for _ in range(target):
    name_list.append(len(list(dict.fromkeys(list(input())))))
name_list.sort()
print(name_list[-1])
