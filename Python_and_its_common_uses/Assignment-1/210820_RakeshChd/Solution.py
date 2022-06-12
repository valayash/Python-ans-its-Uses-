import numpy as np 
import time
n = int(input('Value of n is: '))
A = np.random.randint(2*n+1, size = (n, n)) #Random Matrix of size 3X3
print ('Matrix A: \n', A)
B = np.random.randint(2*n+1, size = (n, n)) #Random Matrix of size 3X3
print ('Matrix B: \n', B)
print()

# Multipling Matrix A and B without NumPy
Resultant_Matrix = [[0,0,0],
                    [0,0,0],
                    [0,0,0]]   
a = time.time()
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            Resultant_Matrix[i][j] += A[i][k]*B[k][j]
print('AxB without NumPy: ')
for r in Resultant_Matrix:
    print(r)
b = time.time()
print('Time Taken: ', b-a)
print('\n')


# Multipling Matrix A and B with NumPy
AxB = np.dot(A, B)
print('AxB with NumPy : \n', AxB)
c = time.time()
print('Time Taken: ', c-b)
print('\n')


# Addition Of Matrix A and B without NumPy
print ('A+B without NumPy: ')
for i in range(len(A)):
    for j in range(len(A[0])):
        Resultant_Matrix[i][j] = A[i][j] + B[i][j]
for x in Resultant_Matrix :
    print (x)
d = time.time()
print('Time Taken: ', d-c)
print('\n')


# Addition Of Matrix A and B with NumPy
print('A+B with NumPy: \n', np.add(A, B))
e = time.time()
print('Time Taken: ', e-d)
print('\n')


# Inverse Of Matrix without NumPy
def nx2n(n_Rows, n_Columns):
    Zeros = []
    for i in range(n_Rows):
        Zeros.append([])
        for j in range(n_Columns*2):
            Zeros[i].append(0)
    return Zeros
def update_M(inputs, n_Rows, n_Columns, Zero):
    for i in range(n_Rows):
        for j in range(n_Columns):
            Zero[i][j] = inputs[i][j]
    return Zero
def identity_M(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
        for j in range(n_Columns):
            if i == j:
                Matrix[i][j+n_Columns] = 1
    return Matrix
# GJ Elimination Method
def GJE(n_Rows, n_Columns, Matrix):
    for i in range(n_Rows):
        if Matrix[i][i] == 0:
            print('ERROR - Cannot Divide By "0"')
            break
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
        GJE(number_Rows, number_Columns, 
        identity_M(number_Rows, number_Columns, 
        update_M(Matrix, number_Rows, number_Columns, 
        nx2n(number_Rows, number_Columns))))))
    for i in range(number_Rows):
        returnable.append([])
        for j in range(number_Columns, 2*number_Columns):
            returnable[i].append(Inversed_Matrix[i][j])
    return returnable

print('Inverse Of A without NumPy: \n', Inverse(A))
f = time.time()
print('Time Taken: ', f-e)
print()
print('Inverse Of A with NumPy: \n', np.linalg.inv(A))
g = time.time()
print('Time Taken: ', g-f)
print()
print('Inverse Of B without NumPy: \n', Inverse(B))
i = time.time()
print('Time Taken: ', i-g)
print()
print('Inverse Of B with NumPy: \n', np.linalg.inv(B))
j = time.time()
print('Time Taken: ', j-i)
