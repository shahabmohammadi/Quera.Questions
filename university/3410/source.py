def engine(row_num):
    for item in range(1, len(my_list[row_num]) - 1):
        my_list[row_num][item] = str(int(my_list[row_num - 1][item - 1]) + int(my_list[row_num - 1][item]))


target = int(input()) + 1
my_list = []
for i in range(1, target):
    my_list.append(["1" for i in range(i)])
for row in range(2, len(my_list)):
    engine(row)
for i in my_list:
    print(" ".join(i))
