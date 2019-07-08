target = [input() for i in range(int(input().split(" ")[0]))]
target = "".join(target)
target = target.split(".")
target = "".join(target)
target = target.split("o")
target = "".join(target)
print(len(target))
