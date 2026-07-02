class Parrot():
    name=""
    age=0


Parrot1=Parrot()
Parrot1.name="Blue"
Parrot1.age=10
print(Parrot1.name)
print(Parrot1.age)


Parrot2=Parrot()
Parrot2.name="Green"
Parrot2.age=5
print(Parrot2.name)
print(Parrot2.age)  

print(f"{Parrot1.name} is {Parrot2.age} years old")
print(f"{Parrot2.name} is {Parrot1.age} years old")