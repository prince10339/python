import  numpy as np
m=int(input("enter number of object :\n"))
n=int(input("enter number of features :\n"))
datamatrix=np.zeros((m,n),dtype=float,order='c')
dist=np.zeros((m,m),dtype=float,order='c')

for i in range(len(dist)):
    for j in range(len(datamatrix)):
        print("enter feature ",j+1," ","for object", i+1)
        data=int(input("enter number of features :\n"))
        datamatrix[i][j]=data
print("the data matrix is :\n")
for i in range(len(dist)):
    for j in range(len(datamatrix)):
        print(datamatrix[i][j])
print("\n")

for i in range(len(dist)):
    for j in range(len(datamatrix)):
        distance=0
        for k in range(len(datamatrix)):
            if datamatrix[i][j]==datamatrix[j][k]:
                distance +=distance
        dist[i][j]=(n-distance)/n
print("distance matrix is :\n")

for i in range(len(dist)):
    for j in range(len(datamatrix)):
        print(dist[i][j])
print("\n")

for i in range(len(dist)):
    distance=1000000
    for j in range(len(datamatrix)):
        if i==j:
            continue
        if distance > dist[i][j]:
            distance=dist[i][j]
            obj1=i
            obj2=j
print('\n')
obj1=int(input("enter number of features :\n"))
obj2=int(input("enter number of features :\n"))
print("The most alike object are ",obj1,obj2)
print("distance is :",distance)