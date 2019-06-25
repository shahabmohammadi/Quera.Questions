import math


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


if __name__ == "__main__":
    target = list(str(input()))
    if int("".join(target)) == 1:
        print(2)
    elif int("".join(target)) == 2:
        print(7)
    elif int("".join(target)) == 3:
        print(11)
    else:
        total = 0
        counter = 0
        for digit in target:
            total += int(digit)
        target = int("".join(target))
        for i in range(target + 1, pow(target, 2)):
            if is_prime(i):
                counter += 1
            if counter == total:
                print(i)
                break
