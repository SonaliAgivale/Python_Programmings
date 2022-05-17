import numpy as np
matrix=[]
row=int(input("Enter the number of rows:"))
col=int(input("Enter the number of column:"))
for i in range(row):
    a=[]
    for j in range(col):
        val=int(input("Enter the numbers:"))
        a.append(val)
    matrix.append(a)
arr=np.array(matrix)
for i in range(row):
    for j in range(col):
        print(arr[i][j],end=" ")
    print()
print(type(arr))