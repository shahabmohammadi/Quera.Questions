input()
sample = list(input())
answer = list(input())
passed = 0

for i in range(len(sample)):
    if not sample[i] == answer[i]:
        passed += 1
print(passed)
