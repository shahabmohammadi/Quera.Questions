target = int(input()) + 1


def display(**kwargs):
    print(" " * kwargs["space"] +
          "*" * kwargs["stars"] +
          " " * (kwargs["space"] * 2) +
          "*" * kwargs["stars"])


stars = [stars for stars in range(1, (target + 1), 2)]
space = [space for space in reversed(range(round(target / 2)))]
for i in range(len(space) - 1):
    display(space=space[i], stars=stars[i])
for i in reversed(range(len(space))):
    display(space=space[i], stars=stars[i])
