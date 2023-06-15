from abc import abstractmethod, ABC
from builtins import print

# In the field of software engineering, the interface-segregation principle (ISP) states that no client should be
# forced to depend on methods it does not use. ISP splits interfaces that are very large into smaller and more
# specific ones so that clients will only have to know about the methods that are of interest to them. Such shrunken
# interfaces are also called role interfaces. ISP is intended to keep a system decoupled and thus easier to refactor,
# change, and redeploy.


class Birds(ABC):
    @abstractmethod
    def walk(self):
        pass

    def sing(self):
        pass

    def lay_eggs(self):
        pass


class FlyingBirds(Birds):
    def fly(self):
        pass


class Pigeon(FlyingBirds):
    def walk(self):
        print("Walking down the street")

    def sing(self):
        print("Gulu-Gulu")

    def lay_eggs(self):
        print("Laying eggs!")

    def fly(self):
        print("I am flying!!")


class Chicken(Birds):
    def walk(self):
        print("Walking down the street")

    def sing(self):
        print("Gıd-gıd-gıdaak")

    def lay_eggs(self):
        print("Laying eggs!")