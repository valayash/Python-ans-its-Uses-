import timeit
a=timeit.timeit()
def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    matrix_T = []
    for j in range(columns):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        matrix_T.append(row)

    return matrix_T


def submatrix(arr, a, b):
    return[x[:b]+x[b+1:] for x in (arr[:a]+arr[a+1:])]


def determinant(arr):
    if(len(arr) == 2):
        return arr[0][0]*arr[1][1]-arr[0][1]*arr[1][0]
    det = 0
    for i in range(len(arr)):
        det = det+pow(-1, i)*arr[0][i]*determinant(submatrix(arr, 0, i))
    return det


# def cofactor(arr, i, j):
#     # for i in range(m1):
#     #     for j in range(n1):
#     return pow(-1, i+j)*determinant(submatrix(arr, 0, i))


m1 = int(input("enter rows:"))
n1 = int(input("enter columns:"))
arr = [[float(input()) for i in range(m1)]for j in range(n1)]

if(determinant(arr)==0):
    print("Not Possible")
else:
    adj = []
    for i in range(len(arr)):
            cofactors = []
            for j in range(len(arr)):
                minor = submatrix(arr, i, j)
                cofactors.append((pow(-1, i+j)) * determinant(minor))
            adj.append(cofactors)
    adj = transpose(adj)
    for r in range(len(adj)):
            for c in range(len(adj)):
                adj[r][c] = (adj[r][c]+0.0)/(determinant(arr)+0.0)
                print(str(adj[r][c])+" ", end="")
            print("")
b=timeit.timeit()
print("Time Elasped=,",abs(b-a))