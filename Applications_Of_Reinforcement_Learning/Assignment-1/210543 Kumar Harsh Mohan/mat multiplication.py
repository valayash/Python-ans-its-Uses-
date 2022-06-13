(m, n) = input("Please enter the dimensions of the first matrix, separated by a space ").split(" ")
m = int(m)
n = int(n)
print("Please enter the elements of the first matrix, separating elements in a row by spaces and rows by newlines")
matrix1 = []
matrix2 = []
matrix3 = []
for i in range(0,m):
	temp = input("").split(" ")
	for j in range(0, n):
		temp[j] = int(temp[j])
	matrix1.append(temp)

(o, p) = input("Please enter the dimensions of the second matrix, separated by a space").split(" ")
o = int(o)
p = int(p)
print("Please enter the elements of the second matrix, separating elements in a row by spaces and rows by newlines")
for i in range(0,o):
	temp = input("").split(" ")
	for j in range(0, p):
		temp[j] = int(temp[j])
	matrix2.append(temp)

if n!= o:
    print("Multiplication not possible")
else:  
	summ = 0
	for i in range(0,m):
		temp = []
		for j in range(0,p):
			for k in range(0,n):
				summ += matrix1[i][k]*matrix2[k][j]
			temp.append(summ)
			summ =0
		matrix3.append(temp)
print("The resultant matrix after multiplication is")
for stuff in matrix3:
	print(stuff)