import timeit
a=timeit.timeit()
m1=int(input("enter rows:"))
n1=int(input("enter columns:"))
arr1=[[int(input()) for i in range (m1)]for j in  range (n1)]
m2=int(input("enter rows:"))
n2=int(input("enter columns:"))
if((m1!=m2) or (n1!=n2) ):
    print("Cannot Add")

else:
    arr2=[[int(input()) for i in range (m2)]for j in  range (n2)]
    arr3=[[0 for i in range (m1)]for j in  range (n2)]
    for i in range (m1):
        for j in range (n2):
            arr3[i][j]= arr1[i][j]+arr2[i][j]

    for i in range(m1):
        for j in range(n2):
            print(arr3[i][j], end = "")
        print()
b=timeit.timeit()
print("Time Elasped=,",abs(b-a))