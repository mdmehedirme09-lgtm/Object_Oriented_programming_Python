def extra(x,y):
    x=list(x)
    for ch in y:
        if ch in x:
            x.remove(ch)
        else:
            return ch
        
x=input("Enter the first string: ")
y=input("Enter the second string: ")

print(extra(x,y))