input_len = int(input())
my_list = input()
my_list = my_list.split(" ")
sort_list = []
for i in my_list:
    sort_list.append(float(i))
sort_list.sort()
print(int(sort_list[-1]))
