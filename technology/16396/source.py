class Foo:
    def __init__(self):
        self.__x = 0

    @property
    def x(self):
        pass

    @x.getter
    def x(self):
        return self.__x

    @x.setter
    def x(self, target=None):
        if target is abs(target):
            digits = list(str(target))
            self.__x = int("".join(digits[-2:]))
        else:
            self.__x = -1
