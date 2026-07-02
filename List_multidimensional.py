m=[[1,2,3,4],
   [4,5,6,7],
   [8]]
print(m)

matrix=[]
k=0
for i in range(5):
    row=[]
    for j in range(4):
        row.append(k)
    k+=1
    matrix.append(row)

print(matrix)


#print all the row
for row in matrix:
    print(row)

#pritn the whole matrix
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
    print()

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j],end=" ")
    print()

a=[[1,2,3],[4,5,6]]
a.append([7,8,9])
print(a)

a[0].extend([4,5,6,7])
print(a)

a.insert(1,[987,678])
print(a)

a[1].reverse()
print(a)

a.reverse()
print(a)

#list cpmprehensive
b=[[x*2 for x in row]for row in a]
print(b)