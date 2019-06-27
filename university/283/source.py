x = int(input())
y = int(input())

if x <= y:
    print("Wrong order!")
elif not (x + y) % 2 == 0:
    print("Wrong difference!")
else:
    for i in range(x):
        if i < (x - y) / 2:
            print("* " * x)
        elif ((x - y) / 2) + y <= i:
            print("* " * x)
        else:
            print("* " * int((x - y) / 2) + "  " * y + "* " * int((x - y) / 2))
