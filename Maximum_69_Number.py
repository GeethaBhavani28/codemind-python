n=int(input())
b=list(str(n))
l1=[ ]
count=0
for i in b:
    if(i=='9'):
        l1.append(i)
    elif(i=='6'):
        count+=1
        if(count==1):
            l1.append("9")
            continue
        l1.append(i)
for j in l1:
    print(j,end="")
        




