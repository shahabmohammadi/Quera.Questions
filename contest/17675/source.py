target = [i for i in range(1, (int(input()) + 1))]
fib_list = [1, 1]


def fib():
    fib_list.append(fib_list[-2] + fib_list[-1])


while fib_list[-1] < len(target):
    fib()

display = []
for i in target:
    if i in fib_list:
        display.append("+")
    else:
        display.append("-")
print("".join(display))
