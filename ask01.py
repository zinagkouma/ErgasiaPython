from random import *
from array import *
n = input('Δώσε διάσταση τετραγώνου')
n=int(n)
sum=0
for z in range(100):
    if (n*n)%2==0:
        d=(n*n)//2
    else:
        d=((n*n)//2)+1
    a=[[0]*n]*n
    b=sample([0, 1], counts=[d, (n*n)-d], k=n*n)
    k=0
    for i in range(n):
        for j in range(n):
            a[i][j]=b[k]
            k=k+1
    c=0
    for i in range(n):
        for j in range(0,n,4):
            if j+3<n:
                if (a[i][j]==1 and a[i][j+1]==1 and a[i][j+2]==1 and a[i][j+3]==1):
                    c+=1
    for j in range(n):
        for i in range(0,n,4):
            if i+3<n:
                if (a[i][j]==1 and a[i+1][j]==1 and a[i+2][j]==1 and a[i+3][j]==1):
                    c+=1
    for i in range(0,n,4):
        if i+3<n:
            if (a[i][i]==1 and a[i+1][i+1]==1 and a[i+2][i+2]==1 and a[i+3][i+3]==1):
                c+=1
    for i in range(0,n,4):
        if i+3<n:
            if (a[i][(n-1)-i]==1 and a[i+1][(n-1)-(i+1)]==1 and a[i+2][(n-1)-(i+2)]==1 and a[i+3][(n-1)-(i+3)]==1):
                c+=1
    sum+=c
mo=sum/100
print (mo)
