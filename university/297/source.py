x = int(input())
n = int(input())
total = fact = 1
for i in range(1, n):
    fact *= i
    total += (pow(x, i) / fact)
print("{:.3f}".format(total))
