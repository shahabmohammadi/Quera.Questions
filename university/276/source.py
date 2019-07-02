target = int(input())
if target == 3:
    print("###\n###\n###")
else:
    mid = sum(divmod(target, 2))
    display = ["#" * target]
    a = 0
    b = target - 4
    c = 2
    while 0 <= b:
        display.append("#" + " " * a + "#" + " " * b + "#" * c)
        a += 1
        b -= 2
        c += 1
        if b == -1:
            b = 0
            c -= 1
    for row in range(len(display)):
        print(display[row])
    for row in reversed(range(len(display) - 1)):
        print(display[row])
