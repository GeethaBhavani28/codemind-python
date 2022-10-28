n=int(input())
num=str(n)
l1=[ ]
l2=[ ]
for i in num:
    if(i>="5"):
        l1.append(i)
    elif(i<"5"):
        l2.append(i)
print(max(l1))
        
    