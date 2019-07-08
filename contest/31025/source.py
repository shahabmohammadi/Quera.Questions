import math

target = [float(i) for i in input().split(" ")]
# target = [-7, 1]
# target = [7, 2]
for i in range(int(target[1])):
    target[0] /= 2
print(math.floor(target[0]))