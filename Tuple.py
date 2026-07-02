a="apple"
print(tuple(a))


b=(1,2,3,"a","apple")
print(b)

c=[1,2,3,4,"s"]
tup=tuple(c)
print(c)


tupp=(1,2,3,"a",True,[1,2,3,4],{"key":'Mehedi'})
print(tupp)


x=tuple("geeks")
print(x[0])
print(x[:1])
print(x[-1])
print(x[::-1])#reverse
print(x[1:4])
print(x[:3])
print(x[3:])
print(x[1:4:1])

tup=("apple","orange","mango")
a,b,c=tup
print(a)
print(b)
print(c)


#concatanation
tup1=(1,2,3)
tup2=("a","b")
tup3=tup1+tup2
print(tup3)

# del tup3
# print(tup3)

#using asterick

tup4=(1,2,3,4,5,)
a,*b,c=tup4
print(a)
print(b)
print(c)

#reverse
rev=tuple(reversed(tup4))
print(rev)