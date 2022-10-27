N=int(input())
summ=0
mul=1
while(N>0):
    a=N%10
    summ+=a
    mul=mul*a
    N=N//10
if(summ == mul):print("Spy Number")
else:print("Not Spy Number")