import time
seconds = time.time()


def getCofactor(A, temp,  p,  q,  n):
    i = 0 
    j = 0
    for row in range(n):
        for col in range(n):
            if row!=p and col!=q:
                temp[i][j] = A[row][col]
                j = j+1
                if j==n-1:
                    j=0
                    i = i+1



def determinant(n, matrix):
    d = 0
    if n==1:
        return matrix[0][0]
    temp =[]
    sign = 1
    for i in range(n):          # A for loop for row entries
        a =[]
        for j in range(n):      # A for loop for column entries
            a.append(int(0))
        temp.append(a)
    for f in range(n):
        getCofactor(matrix,temp,0,f,n)
        d += sign*matrix[0][f]*determinant(n-1,temp)
        sign = -1*sign
    return d

def adjoin(A , adjoint,n):
    if n==1:
        adjoint[0][0] = 1
        return
    temp =[]
    sign = 1
    for i in range(n):          # A for loop for row entries
        a =[]
        for j in range(n):      # A for loop for column entries
            a.append(int(0))
        temp.append(a)
    for i in range(n):
        for j in range(n):
            getCofactor(A,temp,i,j,n)
            if (i+j)%2 == 0:
                sign = 1
            else:
                sign = -1
            adjoint[j][i] = sign*(determinant(n-1,temp))
n = int(input("Enter the order of matrix:"))
matrix = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(n):          # A for loop for row entries
    a =[]
    for j in range(n):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)

det = determinant(n,matrix)
if det == 0:
    print("Singular matrix")
    quit()
adjoint = []
for i in range(n):          # A for loop for row entries
    a =[]
    for j in range(n):      # A for loop for column entries
         a.append(int(0))
    adjoint.append(a)
adjoin(matrix,adjoint,n)
for i in range(n):
    for j in range(n):
        t = adjoint[i][j]/det
        print(t , end = " ")
    print()
print("Seconds since epoch =", seconds)