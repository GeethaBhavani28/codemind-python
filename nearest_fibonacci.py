n=int(input())
a=0
b=1
l1=[ ]
l2=[ ]
for i in range(1,n+1):
    c=a+b
    a=b
    b=c
    if(c<n):
        l1.append(b)
    else:
        l2.append(b)
d=n-max(l1)
e=min(l2)-n
if(d>e):print(min(l2))
elif(d<e):print(max(l1))
elif(d==e):print(max(l1),min(l2))