spaces = int(input())
diagonal = 2 * spaces + 1

space_list = [i for i in reversed(range(0, spaces + 1))]
star_list = [i for i in range(1, diagonal + 1, 2)]

for i in range(len(space_list)):
    print(" " * space_list[i] + "*" * star_list[i])

for i in reversed(range(len(space_list) - 1)):
    print(" " * space_list[i] + "*" * star_list[i])
