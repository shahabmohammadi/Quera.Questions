keys = ["MOLANA", "HAFEZ"]
targets = [input() for i in range(5)]
row_numbers = []
for target in range(len(targets)):
    if keys[0] in targets[target] or keys[1] in targets[target]:
        row_numbers.append(str(target + 1))
if len(row_numbers) == 0:
    print("NOT FOUND!")
else:
    print(" ".join(row_numbers))
