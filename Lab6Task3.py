s1=input("Enter the first string: ")
s2=input("Enter the second string: ")

result= " "


for ch in s1:
    if ch in s2:
        if ch not in result:
            result+=ch

print(result)