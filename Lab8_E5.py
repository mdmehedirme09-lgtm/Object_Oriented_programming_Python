#Example 5

#abstract proprties

from abc import ABC

class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"

class child(parent):
    @property
    def geeks(self):
        return "child class"

try:
    r=parent()
    print(r.geeks)

except Exception as err:
    print(err)

r=child()
print(r.geeks)