target = int(input())

my_list = []

for i in range(1, target + 1):
    my_list.append([None for i in range(i)])

for i in range(target):
    my_list[i][0] = "1"
    my_list[i][len(my_list[i]) - 1] = "1"

for y in range(target):
    for x in range(len(my_list[y]) - 1):
        if my_list[y][x] is None:
            my_list[y][x] = str(int(my_list[y - 1][x - 1]) + int(my_list[y - 1][x]))

for nums in my_list:
    print(" ".join(nums))
