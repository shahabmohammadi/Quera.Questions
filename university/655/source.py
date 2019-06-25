target = int(input())
my_list = []


def engine():
    index = input()
    index = index.split(" ")
    for item in range(len(index)):
        index[item] = index[item].capitalize()
    return " ".join(index)


for i in range(target):
    my_list.append(engine())
for i in my_list:
    print(i)
