import time
import numpy as np
import random
r1 = random.randint(1, 10)
mx1 =np.random.rand(r1, r1)
mx2=np.random.rand(r1, r1)
print(mx1) 
print(mx2)
mx3 = np.zeros((r1,r1))
#addition
for i in range(0,r1):
     for j in range(0,r1):
         mx3[i][j]=mx1[i][j]+mx2[i][j]

for r in mx3:
    print(r)
    

print(time.time())
#using numpy
import numpy as geek
print(geek.add(mx1,mx2))
mx3 = np.zeros((r1,r1))

print(time.time())
#multiplication
for i in range(0,r1):
     for j in range(0,r1):
         for k in range (0,r1):
           mx3[i][j] += mx1[i][k] * mx2[k][j]

print(mx3)

print(time.time())
mx3 = np.zeros((r1,r1))
#using numpy
import numpy as np
mx3=np.dot(mx1,mx2)
print(mx3)


print(time.time())

#matrix inverse


def nx2n(n_Rows, n_Columns):
    Zeros = []
    for i in range(n_Rows):
        Zeros.append([])
        for j in range(n_Columns*2):
            Zeros[i].append(0)
    return Zeros


def update(inputs, n_Rows, n_Columns, Zero):
    for i in range(n_Rows):
        for j in range(n_Columns):
            Zero[i][j] = inputs[i][j]
    return Zero


def identity(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
        for j in range(n_Columns):
            if i == j:
                Matrix[i][j+n_Columns] = 1
    return Matrix

def GAUSS(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
      
    
        for j in range(n_Columns):
            if i != j:
                ratio = Matrix[j][i]/Matrix[i][i]

                for k in range(2*n_Columns):
                    Matrix[j][k] = Matrix[j][k] - ratio * Matrix[i][k]
    return Matrix


def row_op(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
        divide = Matrix[i][i]
        for j in range(2*n_Columns):
            Matrix[i][j] = Matrix[i][j]/divide
    return Matrix

def Inverse(Matrix):
    returnable = []
    number_Rows = int(len(Matrix))
    number_Columns = int(len(Matrix[0]))
    Inversed_Matrix = (row_op(number_Rows, number_Columns, 
        GAUSS(number_Rows, number_Columns, 
        identity(number_Rows, number_Columns, 
        update(Matrix, number_Rows, number_Columns, 
        nx2n(number_Rows, number_Columns))))))

    for i in range(number_Rows):
        returnable.append([])
        for j in range(number_Columns, 2*number_Columns):
            returnable[i].append(Inversed_Matrix[i][j])
    return returnable

print(Inverse(mx1))

#using numpy
import numpy as np
  
# Calculating the inverse of the matrix
print(np.linalg.inv(mx1))
