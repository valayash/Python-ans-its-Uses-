import time
start=time.time() 
def addition():
    matrix1=[]
    m=int(input("Enter the no. of rows of your matrix1 : "))
    n=int(input("Enter the no. of columns of your matrix1 :"))
    for i in range(m) :
            str1=input()
            matrix1.append(str1.split())
    matrix2=[]
    x=int(input("Enter the no. of rows of your matrix2 : "))
    y=int(input("Enter the no. of columns of your matrix2 :"))
    for i in range(x) :
            str1=input()
            matrix2.append(str1.split())
    print("Added matrix is : ",end="\n")
    if(m==x and n==y):
        for i in range(m) :
            for j in range(n) :
                print(int(matrix1[i][j])+int(matrix2[i][j]),end=" " )
            print(end="\n")
    else:
        print("They cannot be added")
def multiplication():
    matrix1=[]
    m=int(input("Enter the no. of rows of your matrix1 : "))
    n=int(input("Enter the no. of columns of your matrix1 :"))
    for i in range(m) :
            str1=input()
            matrix1.append(str1.split())
    matrix2=[]
    x=int(input("Enter the no. of rows of your matrix2 : "))
    y=int(input("Enter the no. of columns of your matrix2 :"))
    for i in range(x) :
            str1=input()
            matrix2.append(str1.split())
    if(n==x):
        sum=0
        print("Your multiplicated result is : ",end="\n")
        for i in range(m):
            for j in range(n) :
                for k in range(n) :
                    sum+=(int(matrix1[i][k])*int(matrix2[k][j]))
                print(sum,end=" ")
                sum=0
            print(end="\n")
    else:
        print("They cannot be multiplied")
def arr_br(array,x,y):
    array1 = []
    for i in range(len(array)):
        if i!=x:
            row=[]
            for j in range(len(array)):
                if j!=y :
                    row.append(array[i][j])
            array1.append(row)
    return array1
def det(array):
    if len(array)==2 :
        return (int(array[0][0])*int(array[1][1]))-int((array[0][1])*int(array[1][0]))
    elif len(array)==1:
        return array[0][0]
    else:
        sum=0
        for i in range(len(array)):
            sum+=(((-1)**i)*int(array[0][i])*det(arr_br(array,0,i)))
        return sum
def inverse():
    m=int(input("Enter the no. of rows of your matrix : "))
    n=int(input("Enter the no. of columns of your matrix :"))
    if(m!=n):
        print("Your matrix will be invertible")
    else:
        matrix=[]
        for i in range(m) :
                str1=input()
                matrix.append(str1.split())
        if det(matrix)==0:
            print("Your matrix is invertible")
        else:
            print("Inverted matrix is :",end="\n")
            for i in range(m):
                for j in range(m):
                    print((1/det(matrix))*det(arr_br(matrix,j,i)),end=" " )
                print(end="\n")
flag='y'
while(True):
    if(flag=='y'):
        print("What do you want to perform : ")
        print("1.Addition")
        print("2.Multiplication")
        print("3.Inverse")
        a=int(input("Enter your response : "))
        if(a==1) :
            addition()
            end=time.time()
            print("Runtime of this program is ",end-start)
        elif(a==2) :
            multiplication()
            end=time.time()
            print("Runtime of this program is ",end-start)
        elif(a==3):
            inverse()
            end=time.time()
            print("Runtime of this program is ",end-start)
        else:
            print("Invalid input")
        flag=input("\nDo you want to run one more time (y/n) ? ")
    else:
        break
    



