n=int(input())
i=0
for i in range(1,n+1):
    if(i*(i+1)==n):
        print("YES")
        break
else:
    print("NO")