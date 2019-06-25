target = input()
target = target.split(" ")
x1, y1, x2, y2 = target[0], target[1], target[2], target[3]
if y1 == y2:
    print("Horizontal")
elif x1 == x2:
    print("Vertical")
else:
    print("Try again")
