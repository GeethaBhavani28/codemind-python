n=int(input())
d=pow(n,2) 
rev=0
while(n>0):
    u=n%10
    rev=rev*10+u
    n=n//10
r=pow(rev,2) 
x=str(r)
z=x[::-1] 
if(d==int(z)):
    print("True")
else:
    print("False")
