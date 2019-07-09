def engine(target):
    if target[0] == target[1] == 0:
        return "00:00"

    else:
        target[0] = str(12 - target[0])
        target[1] = str(60 - target[1])
        for i in range(len(target)):
            if len(target[i]) == 1:
                target[i] = list(target[i])
                target[i].insert(0, "0")
                target[i] = "".join(target[i])
    if target[1] == "60":
        target[1] = "00"
    if "12" in target[0]:
        target[0] = "00"
    return ":".join(target)


if __name__ == '__main__':
    print(engine([int(i) for i in input().split(" ")]))
