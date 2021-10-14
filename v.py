m = int(input("Enter the number of objects:: "))
n = int(input("Enter the number of features:: "))

datamatrix = []
for i in range(m):
    datamatrix.append([])
for i in range(m):
    for j in range(n):
        datamatrix[i].append(j)
        datamatrix[i][j] = ""

dist = []
for i in range(m):
    dist.append([])
for i in range(m):
    for j in range(m):
        dist[i].append(j)
        dist[i][j] = 0

for i in range(m):
    for j in range(n):
        print("Enter feature", j + 1, "for object", i + 1, end=" :: ")
        datamatrix[i][j] = input()

print("\nThe Data Matrix is:: ")
for i in range(m):
    for j in range(n):
        print(datamatrix[i][j], end="   ")
    print(end="\n")

for i in range(m):
    for j in range(m):
        distance=0
        for k in range(n):
            if datamatrix[i][k] == datamatrix[j][k]:
                distance+=1
        dist[i][j]=(n-distance)/n

print("\nThe Distance Matrix is:: ")
for i in range(m):
    for j in range(m):
        print(dist[i][j], end="   ")
    print(end="\n")

distance=10000000
for i in range(m):
    for j in range(m):
        if i==j:
            continue
        if distance>dist[i][j]:
            distance=dist[i][j]
            obj1=i
            obj2=j

print("\n\nThe Most Alike Objects are object number ", obj1+1, " and Object number ", obj2+1)
print("The Distance is ", distance)

