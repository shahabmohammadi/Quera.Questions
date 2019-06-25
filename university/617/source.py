target = str(input())
target = list(target)
my_list = []
for i in reversed(range(len(target))):
    my_list.append(target[i])
if int("".join(target)) == int("".join(my_list)):
    print("YES")
else:
    print("NO")
