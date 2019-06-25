target = list(input())


def display(red, green, yellow):
    if green == 0:
        print("nakhor lite")
    elif 3 <= red:
        print("nakhor lite")
    elif 2 <= red and 2 <= yellow:
        print("nakhor lite")
    else:
        print("rahat baash")


def engine(target_list):
    red = 0
    green = 0
    yellow = 0
    for i in target_list:
        if i is "R":
            red += 1
        elif i is "G":
            green += 1
        else:
            yellow += 1
    display(red, green, yellow)


engine(target)
