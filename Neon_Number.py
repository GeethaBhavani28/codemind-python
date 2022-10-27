n=int(input())
d=n*n
count=0
while(d>0):
    a=d%10
    count+=a
    d=d//10
if(count==n):print("Neon Number")
else:print("Not Neon Number")