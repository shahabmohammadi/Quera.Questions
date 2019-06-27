a = input()
b = input()
target_1 = list(a)
target_1.reverse()
target_1 = int("".join(target_1))
target_2 = list(b)
target_2.reverse()
target_2 = int("".join(target_2))
if target_1 < target_2:
    print(a, "<", b)
elif target_2 < target_1:
    print(b, "<", a)
else:
    print(a, "=", b)
