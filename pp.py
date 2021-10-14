m = int(input("Enter the number of objects:: "))
n = int(input("Enter the number of features:: "))

q, r, s = 0, 0, 0

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
        try:
            for k in range(n):
                if datamatrix[i][k]==1 and datamatrix[j][k]==1:
                    q+=1
                if datamatrix[i][k]==1 and datamatrix[j][k]==0:
                    r+=1
                if datamatrix[i][k]==0 and datamatrix[j][k]==1:
                    s+=1
        except ZeroDivisionError:
            dist[i][j]=(r+s)/(q+r+s)

print("\nThe Distance Matrix is:: ")
for i in range(m):
    for j in range(m):
        print(dist[i][j], end="   ")
    print(end="\n")
