from toto import Toto


class Titi(object):
    def __init__(self, name="titi"):
        self.name = name
        self.toto = Toto(42)

    def __str__(self):
        return "{} {}".format(self.name, self.toto.value)

    def setName(self, name):
        self.name = name
        return self

    def getName(self):
        return self.name

    def getTotoValue(self):
        if isinstance(self.toto, Toto):
            return self.toto.value
