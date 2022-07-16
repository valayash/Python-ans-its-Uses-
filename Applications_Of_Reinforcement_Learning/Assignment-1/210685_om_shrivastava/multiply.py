import time
seconds = time.time()

print("FIRST MATRIX")
R1 = int(input("Enter the number of rows:"))
C1 = int(input("Enter the number of columns:"))
  
# Initialize matrix
matrix1 = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R1):          # A for loop for row entries
    a =[]
    for j in range(C1):      # A for loop for column entries
         a.append(int(input()))
    matrix1.append(a)

print("SECOND MATRIX:")
R2 = int(input("Enter the number of rows:"))
C2 = int(input("Enter the number of columns:"))

if C1 != R2:
    print("Invalid Entries")
    quit()


# Initialize matrix
matrix2 = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R2):          # A for loop for row entries
    a =[]
    for j in range(C2):      # A for loop for column entries
         a.append(int(input()))
    matrix2.append(a)

matrix = []
for i in range(R1):
    a = []
    for j in range(C2):
        a.append(int(0))
    matrix.append(a)


for i in range(R1):
    for j in range(C2):
        for k in range(C1):
            matrix[i][j] += matrix1[i][k] * matrix2[k][j]

for i in range(R1):
    for j in range(C2):
        print(matrix[i][j], end = " ")
    print()


print("Seconds since epoch =", seconds)