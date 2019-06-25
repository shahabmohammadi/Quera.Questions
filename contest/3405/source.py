my_list = []
while True:
    target = input()
    if target == "0":
        break
    else:
        my_list.append(target)
for i in reversed(range(len(my_list))):
    print(my_list[i])
