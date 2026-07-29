def difference(x):
    x=list(x)
    x.sort()
    min="".join(x)
    x.sort(reverse=True)
    max="".join(x)
    result=int(max)-int(min)
    return result
x=input('Enter your number: ')
r=difference(x)
print(r)
