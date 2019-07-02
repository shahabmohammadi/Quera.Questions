target = input().lower()
target = [i for i in target if i.isalnum()]
target = "".join(target)
if target == target[::-1]:
    print("YES")
else:
    print("NO")
