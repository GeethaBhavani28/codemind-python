n=int(input())
d=list(str(n))
ec=0
oc=0
for i in d:
    if(int(i)%2==0):
        ec+=1
    else:
        oc+=1
if(ec==len(d)):
    print("Even")
elif(oc==len(d)):
    print("Odd")
elif(ec<len(d) or od<len(d)):
    print("Mixed")