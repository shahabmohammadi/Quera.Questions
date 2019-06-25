target = input()
target = target.split(" ")
y = int(target[0])
x = int(target[1])
if x <= 10:
    print("Right", (11 - y), x)
else:
    print("Left", (11 - y), (21 - x))
