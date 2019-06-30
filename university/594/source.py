def t2b(my_list):
    a = my_list[0]
    b = my_list[1]
    c = []
    while not divmod(a, b) == (0, 0):
        c.append(str(divmod(a, b)[1]))
        a = divmod(a, b)[0]
    c.reverse()
    return str("".join(c))


a_b = [int(i) for i in input().split(" ")]
c = t2b(a_b)
first_sum = [int(c[i]) for i in range(0, len(list(c)), 2)]
second_sum = [int(c[i]) for i in range(1, len(list(c)), 2)]
if sum(first_sum) == sum(second_sum):
    print("Yes")
else:
    print("No")
