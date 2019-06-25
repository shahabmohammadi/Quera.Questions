a = int(input())
b = int(input())
my_list = []


def fib(n):
    a, b = 0, 1
    while a < n:
        my_list.append(a)
        a, b = b, a + b


fib(b)
for i in reversed(range(1, len(my_list))):
    print(my_list[i])
if a == b == 1:
    print(1)
