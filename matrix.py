import numpy as np
r=int(input("enter the num of rows:"))
c=int(input("enter the num of cols:"))
values=list(map(int,input("enter the values:").split()))
if r*c!=len(values):
    print("wrong number of values:")
    exit()
matrix=np.array(values).reshape(r,c)

print("matrix:",matrix)
print("maximum value is:",np.max(matrix))
print("minimum value is:",np.min(matrix))

i=int(input("enter the row position:"))
j=int(input("enter the col position:"))
if i>=r or j>=c:
    print("array index not within array range.")
    exit()
else:
    print(f"value at {i},{j} is: {matrix[i][j]}" )

trans=matrix.T
print("transposed matrix is:",trans)

print("sum of the values is:",np.sum(matrix))

print("addition of 2 matrices is:",matrix+matrix)
print("subtraction of 2 matrices is:",matrix-matrix)
print("multiplication of 2 matrices elements is:",matrix*matrix)
print("multiplication of 2 matrices is:",matrix@matrix)




