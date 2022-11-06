import math
X,Y,M=map(int,input().split())
d=math.pow(X,Y)
b=d%M
print(int(b))
