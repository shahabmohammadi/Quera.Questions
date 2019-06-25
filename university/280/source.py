pythagoras = []
for i in range(3):
    pythagoras.append(float(input()))
pythagoras.sort()
if pythagoras[0] * pythagoras[0] == pythagoras[1] * pythagoras[1] + pythagoras[2] * pythagoras[2]:
    print("YES")
elif pythagoras[1] * pythagoras[1] == pythagoras[0] * pythagoras[0] + pythagoras[2] * pythagoras[2]:
    print("YES")
elif pythagoras[2] * pythagoras[2] == pythagoras[1] * pythagoras[1] + pythagoras[0] * pythagoras[0]:
    print("YES")

else:
    print("NO")
