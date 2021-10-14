import matplotlib.pyplot as plt

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('DDA Algorithm')

x1=int(input('Enter the starting point x1: '))
y1=int(input('Enter the starting point y1: '))
x2=int(input('Enter the end point x2: '))
y2=int(input('Enter the end point y2:'))

dx=x2-x1
dy=y2-y1

if abs(dx)> abs(dy):
    steps=abs(dx)
else:
    steps=abs(dy)
xincrement=dx/steps
yincrement=dy/steps

i=0
xcordinates=[]
ycordinates=[]

while i < steps:
    i=i+1
    x1=x1+xincrement
    y1=y1+yincrement
    print('x1:',x1,'y1:',y1)
    xcordinates.append(x1)
    ycordinates.append(y1)

plt.plot(xcordinates,ycordinates)
plt.show()    