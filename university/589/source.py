def factorial(digit):
    total = 1
    for i in range(1, (digit + 1)):
        total *= i
    return total


if __name__ == "__main__":
    target = int(input())
    print(factorial(target))
