class Palindrome:
    def __init__(self):
        self.target = input()
        self.target = int(self.target, int(input()))
        self.base = int(input())

    @staticmethod
    def t2b(a, b):
        c = []
        while not divmod(a, b) == (0, 0):
            c.append(str(divmod(a, b)[1]))
            a = divmod(a, b)[0]
        c.reverse()
        return str("".join(c))

    @staticmethod
    def engine(target):
        x = list(target)
        y = reversed(x)
        if "".join(x) == "".join(y):
            return True
        else:
            return False


if __name__ == "__main__":
    obj = Palindrome()
    if obj.engine(obj.t2b(obj.target, obj.base)):
        print("YES")
    else:
        print("NO")
