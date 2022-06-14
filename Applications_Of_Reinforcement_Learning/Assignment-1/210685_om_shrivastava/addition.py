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
  
# Initialize matrix
matrix2 = []
print("Enter the entries rowwise:")
  
# For user input
for i in range(R2):          # A for loop for row entries
    a =[]
    for j in range(C2):      # A for loop for column entries
         a.append(int(input()))
    matrix2.append(a)

if R1 != R2 or C1 != C2:
    print("Invalid Entries")
else:
    for i in range(R1):
        for j in range(C1):
            matrix1[i][j] = matrix1[i][j] + matrix2[i][j]     
# For printing the matrix
for i in range(R1):
    for j in range(C1):
        print(matrix1[i][j], end = " ")
    print()
   
print("Seconds since epoch =", seconds)