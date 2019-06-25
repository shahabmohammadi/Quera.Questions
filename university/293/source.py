import math

start = int(input())
begin = int(input()) + 1


def is_prime(d):
    if d == 1:
        return False
    elif d == 2:
        return True
    elif d > 2 and d % 2 == 0:
        return False
    max_divisor = math.floor(math.sqrt(d))
    for i in range(3, 1 + max_divisor, 2):
        if d % i == 0:
            return False
    return True


for i in range(start, begin):
    if is_prime(i):
        print(i)
