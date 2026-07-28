s = input()

pos = []

for i in range(len(s)):
    if s[i].isupper():
        pos.append(i)
        


ans = s[pos[0]+1:pos[1]]

if ans == "":
    print("BLANK")
else:
    print(ans)