target = [int(i) for i in input().split(" ")]
my_list = [1, 1, 2, 2, 2, 8]
answer = []
for i in range(len(my_list)):
    if target[i] == my_list[i]:
        answer.append('0')
    elif target[i] < my_list[i]:
        answer.append(str(my_list[i] - target[i]))
    else:
        answer.append("-" + str(target[i] - my_list[i]))
print(" ".join(answer))
