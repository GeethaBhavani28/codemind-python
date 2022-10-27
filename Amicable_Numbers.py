n=int(input())
m=int(input())
count=0
summ=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        count+=i
        
for j in range(1,(m//2)+1):
            if(m%j==0):
                summ+=j
if(summ==n and count==m):
    print("Amicable")
else:
    print("Not Amicable")
         
