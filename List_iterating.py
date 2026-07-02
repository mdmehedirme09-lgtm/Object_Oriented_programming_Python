a=['a',1,2,3,"apllo"]

for i in range(len(a)):
    print(i)

j=0
while j<len(a):
    print(a[j])
    j+=1

for item in a:
    print(item)

#using enumerate()to print bot index & values

for i,item in enumerate(a):
    print(i,item)

#shortest syntax for looping 

[print(val) for val in a]#similar to for loop


