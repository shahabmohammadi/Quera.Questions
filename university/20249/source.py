targets = [int(i) for i in input().split(" ")]
amount = targets[0]
limit = targets[1]
targets = [int(i) for i in input().split(" ")]
if amount * limit == sum(targets):
    print(0)
else:
    extra = (amount * limit) - sum(targets)
    print(int(extra / limit))
