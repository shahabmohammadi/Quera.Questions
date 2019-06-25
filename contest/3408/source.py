input()
target = input().split(" ")
target = [target[i] for i in reversed(range(len(target)))]
target = " ".join(target)
print(target)
