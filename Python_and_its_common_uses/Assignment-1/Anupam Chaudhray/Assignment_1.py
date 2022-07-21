#Multiplication
Matrix_A = [[1,2],
            [4,5],
            [7,8]]
Matrix_B = [[9,8],
            [6,5]]
Matrix_C = [[0,0],
            [0,0],
            [0,0]]
for i in range(0,len(Matrix_A)):
    for j in range(0,len(Matrix_B[0])):
        for k in range(0,len(Matrix_B)):
            Matrix_C[i][j] += Matrix_A[i][k] * Matrix_B[k][j]
for output in Matrix_C:
    print(output)

#multiplication using numpy

import numpy as np
Matrix_A = [[1,2],
            [4,5],
            [7,8]]
Matrix_B = [[9,8],
            [6,5]]
print(np.dot(Matrix_A,Matrix_B))



#Addition
Matrix_A = [[1,2],
            [4,5],
            [7,8]]
Matrix_B = [[9,8],
            [6,5],
            [3,2]]
Matrix_C = [[0,0],
            [0,0],
            [0,0]]
for i in range(0,len(Matrix_C)):
    for j in range(0,len(Matrix_C[0])):
        Matrix_C[i][j] = Matrix_A[i][j] + Matrix_B[i][j]
for output in Matrix_C:
    print(output)

#addition using numpy

import numpy as np
Matrix_A = [[1,2],
            [4,5],
            [7,8]]
Matrix_B = [[9,8],
            [6,5],
            [3,2]]
print(np.add(Matrix_A,Matrix_B))

#time taken in execution of code
import time
start= time.time()
a = 0
for i in range(1000):
    a += (i**100)
end = time.time()
print("The time of execution of above program is:", end-start)


