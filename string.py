s="""Wee are Bangladeshi
     We live here
    our country"""

print(s)
s1="thequickbrownfox"
print(s1[:5])
print(s1[5:])
print(s1[9:4:-1])
print(s1[4:9:1])
print(s1[9:2:-1])
print(s1[2:9:1])


s2='I am Mehedi'
s3='am'
print(s3 in s2)
s4='Am'
print(s4 in s2)# case sensitive
print(s3+s4)
print(s3*4)
#multiple print of string
print("Hi\n"*4)
#format()
s5="Hello {},I am {}".format("Bob",'Mehedi')
print(s5)
s6="Hello {0},I am {1}".format("Bob",'Mehedi')
print(s6)
s7=s6="Hello {1},I am {0}".format("Bob",'Mehedi')
print(s7)
s8="I a {0},{1}.I have only {2:0.2f}".format("sorry","bob",45.67890)
print(s8)

#ASCII value of character
v1=ord("A")
print(v1)
v2=chr(65)
print(v2)


#string Function
s9="Mehedi"
print(s9.lower())
s10="mehedi"
print(s10.upper())

s11=" I am Mehedi hasan "
print(s11)
print(s11.strip())

s12="I am mehedi hasan.i am mehedi.i am mehedi"
print(s12.count('am'))

print(s12.startswith('I'))
print(s12.endswith("he"))
print(s12.find('mehedi'))
print(s12.replace('am','was'))