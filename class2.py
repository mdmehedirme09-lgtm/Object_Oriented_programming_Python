class Dog:
    species="mammal"#class intances

    def __init__(self,name,age):
        self.name=name #intance attribute
        self.age=age


dog1=Dog("Tommy",3)
print(dog1.name)
print(dog1.age)
#accesing the class instance
print("{} is a {}".format(dog1.name,dog1.species))
#accesing the instance attribute
print("My name is {}".format(dog1.name))

dog2=Dog("Corporal",5)
print(dog2.age)
print("{} is {} years old".format(dog2.name,dog2.age))
print("{} is the dog name".format(dog2.name))

