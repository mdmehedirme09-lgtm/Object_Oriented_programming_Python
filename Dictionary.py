my_dict={"name":"mehedi","age":21}
print(my_dict)

a={"name":"Mehedi","age":21}
print(a["name"])
print(a["age"])

print(a.get("age"))
print(a.get("name"))

#adding & updating
x={"name":"Ratul"}
x["age"]=21
x["name"]="Emon"
print(x)

#remove an item
del x["name"]
print(x)
del x["age"]
print(x)

#using pop()
x={'name':"Abdullah","age":25}
val=x.pop("name")
print(val)
print(x)

#using popitem
d={"a":1,"b":34}
print(d.popitem())
print(d)


#remove all the items
d.clear()
print(d)


#iteratio
z={"name":"Hanif","age":34,"color":"red"}
for key in z:
    print(key)
    print(z[key])

for values in z.values():
    print(values)
    
for key,value in z.items():
    print(key,value)

#nested dictionary
s={"student1":{"name":"Mehedi","age":21},"student2":{"name":"Ratul","age":34}}
print(s)
print(s["student1"])
print(s["student1"]["name"])

