n=int(input())
d=list(str(n))
e=1
count=0
for i in d:
    x=int(i)
    y=pow(x,e)
    e+=1
    count+=y
if(count==n):
    print("True")
else:
    print("False")