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

#(o, p) = input("Please enter the dimensions of the second matrix, separated by a space").split(" ")
#o = int(o)
#p = int(p)
print("Please enter the elements of the second matrix, separating elements in a row by spaces and rows by newlines")
for i in range(0,m):
	temp = input("").split(" ")
	for j in range(0, n):
		temp[j] = int(temp[j])
	matrix2.append(temp)
for i in range(0,m):
	add = 0
	temp = []
	for j in range(0,n):
		add = matrix1[i][j] + matrix2[i][j]
		temp.append(add)
	matrix3.append(temp)
for i in matrix3:
	print(i)