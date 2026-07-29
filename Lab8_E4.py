#example 4
#method using super()

from abc import ABC

class R(ABC):
    def rk(self):
        print("Abstract Base class")

class K(R):
    def rk(self):
        super().rk()
        print("subclass")

#Driver code
r=K()
r.rk()
